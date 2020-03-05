#!/usr/bin/env python3

import dbxref.resolver
import requests
import logging
import json
import argparse
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)


def main():
    """main()method for script usage"""
    parser = argparse.ArgumentParser(description="Retrieve Rfam json documents and parse them into dbxref json format")
    parser.add_argument("--basics", "-b", action="store_true", help="Include basic informations such as dbxref_id, "
                                                                    "name, description and comment.")
    parser.add_argument("--references", "-r", action="store_true", help="Include reference information.")
    parser.add_argument("dbxref", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    if None not in (args.basics, args.references):
        args.basics = True
        args.references = True

    dbxrefs = dbxref.resolver.convert_to_dbxrefs(args.dbxref)
    documents = retrieve(dbxrefs, basics=args.basics, references=args.references)
    print(json.dumps(documents, sort_keys=True, indent=4))


def retrieve(dbxrefs, basics=True, references=True):
    """Retrieve rfam json documents and parse into dbxref json format"""
    resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
    documents = []
    for entry in resolved:
        # Construct URL for retrival
        json_url = entry["locations"]["json"][0]
        logger.debug("URL: %s", json_url)
        r = requests.get(json_url)
        logger.debug("Content: %s", r.text)
        rfam = json.loads(r.text)
        output = {"id": entry["dbxref"]}
        # Parse basic information
        if basics:
            try:
              output.update({"dbxref": "RFAM:" + rfam["rfam"]["acc"],
                               "name": rfam["rfam"]["id"],
                               "description": rfam["rfam"]["description"],
                               "comment": rfam["rfam"]["comment"]
                               })
            except KeyError:
                print("Basic information weren't fully or only partly available. "
                      "Please check the dbxref and the Rfam-site.")
                raise
        # Parse reference information
        if references:
            try:
                output.update({"references": {"author": rfam["rfam"]["curation"]["author"],
                                              "DOI": rfam["rfam"]["curation"]["structure_source"],
                                              "type": rfam["rfam"]["curation"]["type"]
                                              }
                               })
            except KeyError:
                print("References weren't fully or only partly available. "
                      "Please check the dbxref and the Rfam-site")
                raise
        documents.append(output)

    return documents


if __name__ == "__main__":
    main()
