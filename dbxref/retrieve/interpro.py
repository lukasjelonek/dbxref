#!/usr/bin/env python3

import dbxref.resolver
import requests
import logging
import json
import argparse

logger = logging.getLogger(__name__)

def main():
    """main()method for script usage"""
    # AVAILABLE for implementation:
    # 'go_terms', 'member_databases', 'integrated', 'entry_annotations', ''
    #
    # USED:
    # basics: 'accession', 'type', 'description', 'counters', 'entry_id', 'source_database', 'name'
    # hierarchy
    # wikipedia
    # literature
    # cross_references
    # overlaps_with

    parser = argparse.ArgumentParser(description="Retrieve InterPro documents and convert them into json")
    parser.add_argument("--basics", "-b", action="store_true", help="Include basic information such as accession, "
                                                                    "type, name, description, counters, entry_id and "
                                                                    "source_database")
    parser.add_argument("--hierarchy", "-hi", action="store_true", help="")
    parser.add_argument("--wikipedia", "-w", action="store_true", help="")
    parser.add_argument("--literature", "-l", action="store_true", help="")
    parser.add_argument("--cross_references", "-cr", action="store_true", help="")
    parser.add_argument("--overlaps", "-o", action="store_true", help="")
    parser.add_argument("dbxrefs", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    # if nothing specified, output all available information for the entry
    if None not in (args.basics, args.hierarchy, args.wikipedia, args.literature, args.cross_references, args.overlaps):
        args.basics = True
        args.hierarchy = True
        args.wikipedia = True
        args.literature = True
        args.cross_references = True
        args.overlaps = True

    dbxrefs = dbxref.resolver.convert_to_dbxrefs(args.dbxrefs)

    documents = retrieve(dbxrefs, basics=args.basics, hierarchy=args.hierarchy, wikipedia=args.wikipedia,
                         literature=args.literature, cross_references=args.cross_references, overlaps=args.overlaps)
    print(json.dumps(documents, sort_keys=True, indent=4))


def retrieve(dbxrefs, basics=True, hierarchy=True, wikipedia=True, literature=True, cross_references=True, overlaps=True):
    """Retrieve json document from InterPro REST api, filter information by selected Options and parse into new json"""
    resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
    documents = []
    for entry in resolved:
        # Construct URL for retrieve
        json_url = entry['locations']['json'][0]
        logger.debug('URL: %s', json_url)
        r = requests.get(json_url)
        logger.debug('Content: %s', r.text)
        ipro = json.loads(r.text)

        # Parse retrieved json file by selected Options
        output = {"id": entry["dbxref"]}
        if basics:
            try:
                output.update(accession=ipro["metadata"]["accession"], entry_type=ipro["metadata"]["type"],
                              description=ipro["metadata"]["description"], counters=ipro["metadata"]["counters"],
                              entry_id=ipro["metadata"]["entry_id"], name=ipro["metadata"]["name"],
                              source_database=ipro["metadata"]["source_database"])
            except KeyError:
                logger.warning("One or more basic information were not available for the given entry. Please check your output.")
        if hierarchy:
            try:
                output.update(hierarchy=ipro["metadata"]["hierarchy"])
            except KeyError:
                logger.warning("Hierarchy information was not available for the given entry.")
        if wikipedia:
            try:
                output.update(wikipedia=ipro["metadata"]["wikipedia"])
            except KeyError:
                logger.warning("Wikipedia articel were not available for the given entry.")
        if literature:
            try:
                output.update(literature=ipro["metadata"]["literature"])
            except KeyError:
                logger.warning("Literature was not available for the given entry.")
        if cross_references:
            try:
                output.update(cross_references=ipro["metadata"]["cross_references"])
            except KeyError:
                logger.warning("Cross_references were not available for the given entry.")
        if overlaps:
            try:
                output.update(overlaps=ipro["metadata"]["overlaps_with"])
            except KeyError:
                logger.warning("Overlap information was not available for the given entry.")
        documents.append(output)
    return documents


if __name__ == "__main__":
    main()
