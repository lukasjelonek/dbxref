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
    parser.add_argument("--orthology", "-o", action="store_true", help="Includes ortholog genes")
    parser.add_argument("--motif", "-m", action="store_true", help="Includes motif")
    parser.add_argument("--formula", "-f", action="store_true", help="Includes chemical formula")
    parser.add_argument("--reaction", "-r", action="store_true", help="Includes chemical reaction partners")
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
                         dblinks=args.dblinks, genes=args.genes, reference=args.reference, reference=args.orthology,
                         reference=args.motif, reference=args.formula, reference=args.reaction)
    print(json.dumps(documents))


def retrieve(dbxrefs, basics, pathway, brite, dblinks, genes, reference, orthology, motif, formula, reaction):
    """parse kegg html-file (text format) and return a list for dbxref"""
    resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
    documents = []

    for entry in resolved:
        text_url = entry['locations']['text'][0]
        logger.debug('URL: %s', text_url)
        r = requests.get(text_url)
        logger.debug('Content: %s', r.text)
        lines = r.text.strip().split('\n')
        output = {}
        glc = 0  # GlobalLineCounter

        for line in lines:
            if "ENTRY" in line:  # should always be displayed
                output.update(read_basics(lines, glc))
            if "PATHWAY" in line and pathway:
                output.update({"pathways": read_pathway(lines, glc)})
            if "BRITE" in line and brite:
                output.update({"brite": read_brite(lines, glc)})
            if "GENES" in line and genes:
                output.update({"genes": read_information(lines, glc)})
            if "REFERENCE" in line and reference:
                output.update(read_reference(lines, glc))
            if "DBLINKS" in line and dblinks:
                output.update({"dbxrefs": read_dbxrefs(lines, glc)})
            if "ORTHOLOGY" in line and orthology:
                output.update({"orthology": read_information(lines, glc)})
            if "MOTIF" in line and motif:
                output.update({"motif": read_information(lines, glc)})
            if "FORMULA" in line and formula:
                output.update({"formula": read_information(lines, glc)[0]})
            if "REACTION" in line and reaction:
                output.update({"reaction": read_information(lines, glc)})
            else:
                pass
            glc += 1
        print(output["dbxrefs"])
        documents.append(output)
    return documents


def read_basics(lines, glc):
    """parse available basic information of entry such as ID, common name, definition, organism, as a list"""
    llc = glc  # LocalLineCounter
    basics = {}
    for line in lines:
        if "ENTRY" in line:
            entry = read_information(lines, llc)[0].split(" ")
            basics.update({"id": entry[0], "type": entry[1]})  # id and type of called entry
            if len(entry) > 2:
                basics.update({"associated genome": entry[2]})  # if entry (f.e.: proteins)mentions  associated genome
            llc += 1
        if "NAME" in line:
            names = {"names": read_information(lines, llc)}
            if len(names.get("names")) == 1:
                names["names"] = names.get("names")[0].split(",")
            else:
                pass
            llc += 1
        if "ORGANISM" in line:
            basics.update({"organism": read_information(lines, llc)})
            llc += 1
        if "DEFINITION" in line:
            basics.update({"definition": read_information(lines, llc)[0]})
            llc += 1
        else:
            pass
    return basics


def read_brite(lines, glc):
    """parse brite information as a tree"""
    sublines = lines[glc:]  # create sublist with relevant information only
    tree = []
    vertices_index = []  # list of tuples of labels and count of vertices
    edges = []  # list of edges from roots to branches
    vcounter = 0
    stack = []
    for line in sublines:
        if "BRITE" in line or get_depth(line) > 0:
            if get_depth(line) == 0:  # line is a root but begins with "BRITE", therefor depth = 0
                stack = [(" ".join(line.split()[1:]), vcounter)]  # cut "BRITE" out
            if get_depth(line) == 12:  # line is a root with depth = 12
                stack = [(" ".join(line.split()), vcounter)]
            else:  # line is a branch
                new_branch = (" ".join(line.split()), vcounter)
                if get_depth(line) == 0:  # line is a new branch of another branch than the branch in the line above
                    pass
                if get_depth(line)-12 <= len(stack):
                    stack = stack[:get_depth(line)-12]
                else:  # line is a new branch of the branch above
                    pass
                stack.append(new_branch)
            vertices_index.append(stack[-1])
            if len(stack) == 1:  # only root in stack
                pass
            else:  # more than root in stack
                edges.append({stack[-2][1]: stack[-1][1]})
            vcounter += 1
        else:
            break
    tree.append(vertices_index)
    tree.append(edges)
    return tree


def read_reference(lines, glc):
    """parse references of entry, such as Author, release date and Journal, as a list"""
    llc = glc  # LocalLineCounter
    refcounter = 0  # if more than 1 reference/author/journal is given
    references = {}
    for line in lines:
        if "REFERENCE" in line:
            references.update({"reference_" + str(refcounter): read_information(lines, llc)})
        if "AUTHOR" in line:
            references.update({"author_" + str(refcounter): read_information(lines, llc)})
        if "JOURNAL" in line:
            references.update({"journal_" + str(refcounter): read_information(lines, llc)})
        else:
            pass
        refcounter += 1
    return references


def read_pathway(lines, glc):
    pathways_index = read_information(lines, glc)
    pathways = []
    for path in pathways_index:
        pathways.append((path.split(" ")[0], " ".join(path.split(" ")[1:])))
    return pathways


def read_dbxrefs(lines, glc):
    dbxref_index = read_information(lines, glc)
    dbxrefs = []
    for ref in dbxref_index:
        dbxrefs.append("".join(ref.split(" ")))
    return dbxrefs


def read_information(lines, glc):
    """parse information of ONE keyword as a list"""
    llc = glc  # LocalLineCounter
    information = [" ".join(lines[llc].split()[1:])]  # first line of the information, deleting the keyword
    llc += 1
    while lines[llc][0:5].isspace():  # following lines belonging to they keyword are added to list
        information.append(" ".join(lines[llc].split()))  # deleting whitespace
        llc += 1
    else:
        pass
    return information


def get_depth(string):
    """calculates amount of whitespaces, at the start of a string and returns int"""
    spacecount = len(string) - len(string.lstrip(' '))
    return spacecount


if __name__ == "__main__":
    main()
