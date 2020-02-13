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
    parser.add_argument("--references", "-r", action="store_true", help="Include reference information such as journal "
                                                                        "name, DOI, authors and day of publishment.")
    parser.add_argument("--article_ids", "-a", action="store_true", help="Include article-IDs.")
    parser.add_argument("dbxrefs", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    if None not in (args.basics, args.references, args.article_ids):
        args.basics = True
        args.references = True
        args.article_ids = True

    dbxrefs = dbxref.resolver.convert_to_dbxrefs(args.dbxrefs)
    documents = retrieve(dbxrefs, basics=args.basics, references=args.references, article_ids=args.article_ids)
    print(json.dumps(documents, sort_keys=True, indent=4))


def retrieve(dbxrefs, basics, references, article_ids):
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
        output = {}
        entry_id = dbxrefs[0]["id"]
        # Parse basic information
        if basics:
            try:
                output.update({"epublic-date": ".".join(pm["result"][entry_id]["epubdate"].split(" ")[::-1]),
                               "dbxref_id": "PM:" + pm["result"][entry_id]["uid"],
                               "title": pm["result"][entry_id]["title"],
                               "language": pm["result"][entry_id]["lang"]
                               })
            except KeyError:
                print("Basic information weren't fully or only partly available.")
        # Parse references
        if references:
            try:
                output.update({"references": {"authors": read_authors(pm["result"][entry_id]["authors"]),
                                              "journal": pm["result"][entry_id]["fulljournalname"],
                                              "DOI": pm["result"][entry_id]["elocationid"].split(": ", 1)[1],
                                              "pubdate": pm["result"][entry_id]["sortpubdate"]
                                              }
                               })
            except KeyError:
                print("References weren't fully or only partly available.")
        # Parse article-IDs
        if article_ids:
            try:
                output.update({"article_IDs": read_article_ids(pm["result"][entry_id]["articleids"])})
            except KeyError:
                print("Article-IDs weren't available.")
        documents.append(output)
    return documents


def read_authors(authors):
    author_list = []
    for author in authors:
        author_list.append(", ".join(author["name"].split(" ", 1)))
    return author_list


def read_article_ids(article_ids):
    id_list = []
    for article_id in article_ids:
        id_list.append(article_id["idtype"] + ": " + article_id["value"])
    return id_list


if __name__ == '__main__':
    main()
