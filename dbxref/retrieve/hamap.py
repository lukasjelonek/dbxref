import dbxref.resolver
import requests
import logging
import json
import argparse

logger = logging.getLogger(__name__)


def main():
    """main()method for script usage"""

    parser = argparse.ArgumentParser(description="Retrieve HAMAP text documents and convert them into dbxref json "
                                                 "format.")
    parser.add_argument("dbxrefs", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    dbxrefs = dbxref.resolver.convert_to_dbxrefs(args.dbxrefs)
    documents = retrieve(dbxrefs)
    print(json.dumps(documents, sort_keys=True, indent=4))


def retrieve(dbxref):
    """Retrieve text document from expasy/hamap api and parse into json format."""
    resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
    documents = []
    for entry in resolved:
        # Construct URL for retrieve
        text_url = entry['locations']['text'][0]
        logger.debug('URL: %s', text_url)
        r = requests.get(text_url)
        logger.debug('Content: %s', r.text)
        hamap_text = r.text
        print(hamap_text)

    return documents

