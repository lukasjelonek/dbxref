#!/usr/bin/env python3

import dbxref.resolver
import requests
import logging
import json
import argparse

logger = logging.getLogger(__name__)

def main():
    """main()method for script usage"""
    parser = argparse.ArgumentParser(description="Retrieve InterPro documents and convert them into json")
    parser.add_argument("dbxrefs", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    dbxrefs = dbxref.resolver.convert_to_dbxrefs(args.dbxrefs)
    documents = retrieve(dbxrefs)
    print(documents)


def retrieve(dbxrefs):
    """Insert description here"""
    print(dbxrefs)
    resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
    print(resolved)
    documents = []
    for entry in resolved:
        print(entry)
        html_url = entry['locations']['html'][0]
        logger.debug('URL: %s', html_url)
        r = requests.get(html_url)
        logger.debug('Content: %s', r.text)
        lines = json.loads(r.text)
        for line in lines:
            print(line)
    return documents


if __name__ == "__main__":
    main()
