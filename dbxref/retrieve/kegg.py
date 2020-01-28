#!/usr/bin/env python3

import dbxref.resolver
import requests
import logging
import json
import argparse

logger = logging.getLogger(__name__)


def main():
    """main()method for script usage"""
    parser = argparse.ArgumentParser(description="Retrieve KEGG kgml documents and convert them into json")
    parser.add_argument("--basics", "-b", action="store_true", help="Includes ID/Entry, name/aliases and definition,")
    parser.add_argument("--pathway", "-p", action="store_true", help="Includes metabolic pathway")
    parser.add_argument("--brite", "-br", action="store_true", help="Includes hierarchical classifications")
    parser.add_argument("--dblinks", "-db", action="store_true", help="Includes database links")
    parser.add_argument("--genes", "-g", action="store_true", help="Includes assciated genes")
    parser.add_argument("--reference", "-ref", "-r", action="store_true", help="Includes paper reference ID, authors,"
                                                                               "title and published journal")
    parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
    args = parser.parse_args()

    if None not in (args.basics, args.pathway, args.brite, args.dblinks, args.genes, args.reference):
        args.basics = True
        args.pathway = True
        args.brite = True
        args.dblinks = True
        args.genes = True
        args.reference = True

    dbxrefs = dbxref.resolver.convert_to_dbxrefs(args.dbxrefs)

    documents = retrieve(dbxrefs, basics=args.basics, pathway=args.pathway, brite=args.brite,
                         dblinks=args.dblinks, genes=args.genes, reference=args.reference)
    print(json.dumps(documents))


def retrieve(dbxrefs, basics, pathway, brite, dblinks, genes, reference):
    """parse kegg html-file (text format) and return a list for dbxref"""
    resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
    documents = []

    for entry in resolved:
        text_url = entry['locations']['text'][0]
        logger.debug('URL: %s', text_url)
        r = requests.get(text_url)
        logger.debug('Content: %s', r.text)
        lines = r.text.strip().split('\n')
        output = {'id': entry['dbxref']}
        glc = 0  # GlobalLineCounter

        for line in lines:
            if "ENTRY" in line:
                read_basics(lines, glc)
            if "PATHWAY" in line:
                read_information(lines, glc)
            if "BRITE" in line:
                read_brite(lines, glc)
            if "GENES" in line:
                read_information(lines, glc)
            if "REFERENCE" in line:
                read_reference(lines, glc)
            if "DBLINKS" in line:
                read_information(lines, glc)
            if "ORTHOLOGY" in line:
                read_information(lines, glc)
            if "MOTIF" in line:
                read_information(lines, glc)
            if "FORMULA" in line:
                read_information(lines, glc)
            if "REACTION" in line:
                read_information(lines, glc)
            else:
                pass
            glc += 1
        documents.append(output)
    return documents


def read_basics(lines, glc):
    """parse available basic information of entry such as ID, common name, definition, organism, as a list"""
    llc = glc
    entry = []
    names = []
    organism = []
    definition = ""
    for line in lines:
        if "ENTRY" in line:
            entry = read_information(lines, llc)
            llc += 1
        if "NAME" in line:
            names = read_information(lines, llc)
            llc += 1
        if "ORGANISM" in line:
            organism = read_information(lines, llc)
            llc += 1
        if "DEFINITION" in line:
            definition = "".join(read_information(lines, llc))
            llc += 1
        else:
            pass
    return entry, definition, names, organism


def read_brite(lines, glc):
    """parse brite information as a tree"""
    llc = glc
    return


def read_reference(lines, glc):
    """parse references of entry, such as Author, release date and Journal, as a list"""
    llc = glc
    reference = ""
    author = []
    for line in lines[llc]:
        if "REFERENCE" in line:
            ref_index = read_information(lines, llc)
            print(ref_index)
            if len(ref_index) < 1:
                reference = ref_index[1]
            else:
                reference = ref_index[0]

    print(reference)
    return


def read_information(lines, glc):
    """parse information of ONE keyword as a list"""
    llc = glc
    # first line of the information, deleting the keyword
    information = [" ".join(lines[llc].split()[1:])]
    llc += 1
    # following lines belonging to they keyword are added to list
    while lines[llc][0:5].isspace():
        information.append(" ".join(lines[llc].split()))
        llc += 1
    else:
        pass
    return information


if __name__ == "__main__":
    main()
