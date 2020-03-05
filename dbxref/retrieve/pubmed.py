#!/usr/bin/env python3
import dbxref.resolver
import requests
import logging
import json
import argparse

logger = logging.getLogger(__name__)


def main():
    """main()method for script usage"""
    parser = argparse.ArgumentParser(description="Retrieve Pubmed json documents and parse into dbxref json format")
    parser.add_argument("--basics", "-b", action="store_true", help="Include basic information such as title, language,"
                                                                    " dbxref-id, and day of publishment on pubmed.")
    parser.add_argument("dbxrefs", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    if None not in (args.basics):
        args.basics = True

    dbxrefs = dbxref.resolver.convert_to_dbxrefs(args.dbxrefs)
    documents = retrieve(dbxrefs, basics=args.basics)
    print(json.dumps(documents, sort_keys=True, indent=4))

def _get(result, field, mandatory=False, default="", transform=lambda x: x):
  """Retrieve a given field if available, return default or exception otherwise. Result may be manipulated by transformation function"""
  if field in result:
    return transform(result[field])
  else:
    if mandatory:
      raise KeyError("Field '"+field+"' not found in dictionary")
    else:
      return default

def find_id(list, type):
  """Find id of given type in pubmed islist"""
  matches = [x for x in list if x['idtype'] == type]
  if matches:
    return matches[0]["value"]
  else:
    raise KeyError("Id of type '" + type + "' not found in idlist.")

def join_authors(list):
  """Joins pubmed entry authors to a single string"""
  return ", ".join([x["name"] for x in list])

def retrieve(dbxrefs, basics=True):
    """Retrieve Pubmed json documents and parse into dbxref json format"""
    resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
    documents = []
    for entry in resolved:
        # Construct URL for retrival
        json_url = entry["locations"]["json"][0]
        logger.debug("URL: %s", json_url)
        r = requests.get(json_url)
        logger.debug("Content: %s", r.text)
        pm = json.loads(r.text)
        output = {"id": entry["dbxref"]}
        entry_id = dbxrefs[0]["id"]
        # Parse basic information
        result = pm["result"][entry_id]
        if basics:
            output["publication-date"] = _get(result, "epubdate")
            output["dbxref"] = "Pubmed:" + _get(result, "uid")
            output["title"] = _get(result, "title")
            output["language"] = _get(result, "lang", transform=lambda x: ", ".join(x))
            output["authors"] = _get(result, "authors", transform=lambda x: join_authors(x))
            output["source"] = _get(result, "source")
            output["volume"] = _get(result, "volume")
            output["issue"] = _get(result, "issue")
            output["doi"] = _get(result, "articleids", transform=lambda x: find_id(x, "doi"))
        documents.append(output)
    return documents


if __name__ == '__main__':
    main()
