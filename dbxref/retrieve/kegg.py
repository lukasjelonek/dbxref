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
    parser.add_argument("--basics", "-b", action="store_true", help="Include ID/Entry, name/aliases and definition,")
    parser.add_argument("--pathway", "-p", action="store_true", help="Include metabolic pathway")
    parser.add_argument("--brite", "-br", action="store_true", help="Include hierarchical classifications")
    parser.add_argument("--dbxref_links", "-db", action="store_true", help="Include database links in dbxref format")
    parser.add_argument("--genes", "-g", action="store_true", help="Include associated genes")
    parser.add_argument("--reference", "-ref", action="store_true", help="Include paper reference ID, authors,title "
                                                                         "and published journal")
    parser.add_argument("--orthology", "-o", action="store_true", help="Include ortholog genes")
    parser.add_argument("--motif", "-m", action="store_true", help="Include motif")
    parser.add_argument("--formula", "-f", action="store_true", help="Include chemical formula")
    parser.add_argument("--reaction", "-r", action="store_true", help="Include chemical reaction partners")
    parser.add_argument('dbxrefs', nargs=argparse.REMAINDER)
    args = parser.parse_args()

    if None not in (args.basics, args.pathway, args.brite, args.dbxref_links, args.genes, args.reference,
                    args.orthology, args.motif, args.formula, args.reaction):
        args.basics = True
        args.pathway = True
        args.brite = True
        args.dbxref_links = True
        args.genes = True
        args.reference = True
        args.orthology = True
        args.motif = True
        args.formula = True
        args.reaction = True

    dbxrefs = dbxref.resolver.convert_to_dbxrefs(args.dbxrefs)

    documents = retrieve(dbxrefs, basics=args.basics, pathway=args.pathway, brite=args.brite, genes=args.genes,
                         reference=args.reference, orthology=args.orthology, motif=args.motif, formula=args.formula,
                         reaction=args.reaction, dbxrefs_links=args.dbxref_links)
    # print(json.dumps(documents))


def retrieve(dbxrefs, basics, pathway, brite, dbxrefs_links, genes, reference, orthology, motif, formula, reaction):
    """parse kegg text file and return a list of the extracted information"""
    resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
    documents = []

    for entry in resolved:
        text_url = entry['locations']['text'][0]
        logger.debug('URL: %s', text_url)
        r = requests.get(text_url)
        logger.debug('Content: %s', r.text)
        lines = r.text.strip().split('\n')
        output = {}

        # Sorting the received list 'line' in a dictionary with the terms (f.e.: 'ENTRY', 'NAMES') as keys
        kegg_information = {}
        keyword = ""
        information = []
        keyword_repeater = 0
        for line in lines:
            if line[:2].isspace():
                information.append(line)
            else:
                if line.startswith("///"):  # last line of document is always "///"
                    kegg_information.update({keyword: information})
                elif line[0:3].isupper():
                    if len(keyword) and len(information) != 0:
                        if keyword in kegg_information:  # prevents overwrite of Reference, Author, Journal, Title if multiple
                            keyword = keyword.join("_" + keyword_repeater)
                        else:
                            pass
                        kegg_information.update({keyword: information})
                    else:
                        pass
                    split_line = line.split(" ", 1)  # slice the keyword
                    keyword = split_line[0]
                    information = [split_line[1]]
        # Search dictionary for existence of keywords requested by user.
        # If the keyword is present the data receiving function() is started and is put into the output file
        # Every keyword is a single search, to make the code more robust if keywords are missing
        basic_informations = {}
        reference_informations = []
        if "ENTRY" in kegg_information and basics:
            entry_information = read_entry(kegg_information["ENTRY"])
            basic_informations.update({"id": entry_information[0]})
            basic_informations.update({"type": entry_information[1]})
            if len(entry_information) > 2:
                basic_informations.update({"associated organism": entry_information[2]})
        if "NAME" in kegg_information and basics:
            basic_informations.update({"names": read_information(kegg_information["NAME"])[0].split()})
        if "DEFINITION" in kegg_information and basics:
            basic_informations.update({"definition": read_information(kegg_information["DEFINITION"])[0]})
        if "ORGANISM" in kegg_information and basics:
            basic_informations.update({"organism": read_information(kegg_information["ORGANISM"])[0]})
        output.update({"basics:": basic_informations})
        if "PATHWAY" in kegg_information and pathway:
            output.update({"pathways": read_pathway(kegg_information["PATHWAY"])})
        if "GENES" in kegg_information and genes:
            pass
            output.update({"genes": read_information(kegg_information["GENES"])})  # outcommented to lower the outprint
        if "ORTHOLOGY" in kegg_information and orthology:
            output.update({"ortholog genes": read_information(kegg_information["ORTHOLOGY"])})
        if "MOTIF" in kegg_information and motif:
            output.update({"motif": read_information(kegg_information["MOTIF"])})
        if "FORMULA" in kegg_information and formula:
            output.update({"chemical formula": read_information(kegg_information["FORMULA"][0])})
        if "REACTION" in kegg_information and reaction:
            output.update({"reaction partners": read_information(kegg_information["REACTION"])})
        if "BRITE" in kegg_information and brite:
            output.update({"brite": read_brite(kegg_information["BRITE"])})
        if "REFERENCE" in kegg_information and reference:
            reference_informations.append(read_reference(kegg_information["REFERENCE"]))
            output.update({"reference": reference_informations})
        if "DBLINKS" in kegg_information and dbxrefs_links:
            output.update({"dbxref_links": read_dbxrefs(kegg_information["DBLINKS"])})
        else:
            pass
        documents.append(output)
    return documents


def read_entry(lines):
    information = read_information(lines)[0].split()
    entry_id = information[0]
    entry_type = information[1]
    associated_organism = ""
    if len(information) > 2:
        associated_organism = information[2]
        return entry_id, entry_type, associated_organism
    else:
        return entry_id, entry_type


# placeholder, if "pathways" should be in a different format. If not, delete. Consult Lukas for solution!
def read_pathway(lines):
    pathways = read_information(lines)
    return pathways


def read_reference(lines):
    reference_dictionary = {}
    reference_id = []
    authors = []
    title = []
    journal = []
    for line in lines:
        if line.startswith("  PMID"):
            reference_id.append(" ".join(line.split()))
        if line.startswith("  AUTHORS"):
            authors.append(" ".join(line.split()[1:]))
        if line.startswith("  TITLE"):
            title.append(" ".join(line.split()[1:]))
        if line.startswith("  JOURNAL"):
            journal.append(" ".join(line.split()[1:]))
    reference_dictionary.update({"reference_id": reference_id[0], "authors": authors[0].split(","), "title": title[0],
                                 "journal": journal[0]})
    return reference_dictionary


def read_brite(lines):
    """parse brite information as a tree"""
    tree = []
    vertices = []  # list of tuples of labels and count of vertices
    edges = []  # list of edges from roots to branches
    vertices_counter = 0
    stack = []
    for line in lines:
        depth = get_depth(line)-12
        if depth <= 0:
            stack = [(" ".join(line.split()), vertices_counter)]
        else:  # line is a branch
            new_branch = (" ".join(line.split()), vertices_counter)
            if depth <= len(stack):  # line is a new branch not from the line above, stack is emptied until depth fits
                stack = stack[:depth]
            else:  # line is a new branch of the branch above
                pass
            stack.append(new_branch)
        vertices.append(stack[-1])
        if len(stack) == 1:  # only root in stack
            pass
        else:  # more than root in stack
            edges.append({stack[-2][1]: stack[-1][1]})
        vertices_counter += 1
    tree.append(vertices)
    tree.append(edges)
    return tree


def read_dbxrefs(lines):
    for line in lines:
        print(line)


def read_information(lines):
    """parse given key-values information by deleting whitespace and joining the information into a list"""
    information = []
    for line in lines:
        information.append(" ".join(line.split()))
    return information


def get_depth(string):
    """calculates amount of whitespaces, at the start of a string and returns int"""
    spacecount = len(string) - len(string.lstrip(' '))
    return spacecount


if __name__ == "__main__":
    main()
