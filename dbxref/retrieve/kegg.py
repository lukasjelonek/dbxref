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
    parser.add_argument("--basics", "-b", action="store_true", help="Include ID/Entry, names/aliases and definition")
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
    parser.add_argument("dbxrefs", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    if None not in (args.basics, args.pathway, args.brite, args.dbxref_links, args.genes, args.reference,
                    args.orthology, args.motif, args.formula, args.reaction):
        # if nothing specified, output all available information for the entry
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
    print(json.dumps(documents))


def retrieve(dbxrefs, basics, pathway, brite, dbxrefs_links, genes, reference, orthology, motif, formula, reaction):
    """Parse kegg text file and return a list "documents" including the extracted information of the given entries. """

    resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
    documents = []
    for entry in resolved:
        text_url = entry['locations']['text'][0]
        logger.debug('URL: %s', text_url)
        r = requests.get(text_url)
        logger.debug('Content: %s', r.text)
        lines = r.text.strip().split('\n')
        output = {}  # dictionary with terms as keys and the information of given term as values
        # Sorting the received list 'line' in a dictionary with the terms (f.e.: 'ENTRY', 'NAMES') as keys
        kegg_information = parse_entry(lines)
        # Search dictionary for existence of keywords requested by user.
        # If the keyword is present the data receiving function() is started and is put into the output file
        # Every keyword is a single search, to make the code more robust if keywords are missing
        basic_informations = {}
        reference_informations = []
        if "ENTRY" in kegg_information and basics:
            entry_information = read_id(kegg_information["ENTRY"])
            basic_informations.update({"id": entry_information[0]})
            basic_informations.update({"type": entry_information[1]})
            if len(entry_information) > 3:
                basic_informations.update({"associated organism": entry_information[2]})
        if "NAME" in kegg_information and basics:
            basic_informations.update({"names": read_information(kegg_information["NAME"])[0].split()})
        if "DEFINITION" in kegg_information and basics:
            basic_informations.update({"definition": read_information(kegg_information["DEFINITION"])[0]})
        if "ORGANISM" in kegg_information and basics:
            basic_informations.update({"organism": read_information(kegg_information["ORGANISM"])[0]})
        output.update({"basics:": basic_informations})
        if "PATHWAY" in kegg_information and pathway:
            output.update({"pathways": read_information(kegg_information["PATHWAY"])})
        if "GENES" in kegg_information and genes:
            output.update({"genes": read_information(kegg_information["GENES"])})
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


def parse_entry(lines):
    """Parses the entire entry document (text) and yields a dictionary "kegg_information" with keywords as keys for the
    corresponding lines as values. "kegg_information" includes the entire entry document, even when some information
    might be dismissed later (f.e. if it was not requested)."""
    kegg_information = {}
    keyword = ""
    information = []
    for line in lines:
        if line[:2].isspace():
            information.append(line)
        else:
            if line.startswith("///"):  # last line of document is always "///"
                if keyword in kegg_information:
                    kegg_information[keyword].append(information)
                else:
                    kegg_information.update({keyword: [information]})
            elif line[0:3].isupper():
                if len(keyword) and len(information) != 0:
                    if keyword in kegg_information:
                        kegg_information[keyword].append(information)
                    else:
                        kegg_information.update({keyword: [information]})
                else:
                    pass
                split_line = line.split(" ", 1)  # slice the keyword
                keyword = split_line[0]
                information = [line]
    return kegg_information


def read_id(entry):
    """Parse basic informations (id, type and associated organism) as dictionaries"""
    information = read_information(entry)[0].split()
    entry_id = information[1]
    entry_type = information[2]
    associated_organism = ""
    if len(information) > 3:
        associated_organism = information[3]
        return entry_id, entry_type, associated_organism
    else:
        return entry_id, entry_type


def read_reference(entry):
    """Parse reference information(pmid, authors, title and journal as keys with corresponding value) as a dictionary"""
    # EXPECTED INPUT example:
    # kegg_information = {
    #                      'REFERENCE' : [
    #                                       [
    #                                       'REFERENCE   PMID:11939774',
    #                                       'AUTHORS   Cheong CG, Bauer CB, Brushaber KR, Escalante-Semerena JC,
    #                                       Rayment I',
    #                                       'TITLE     Three-dimensional structure of the L-threonine-O-3-phosphate
    #                                       decarboxylase (CobD) enzyme from Salmonella enterica.',
    #                                       'JOURNAL   Biochemistry 41:4798-808 (2002)',
    #                                       'DOI:10.1021/bi012111w'
    #                                       ],
    #                                       [
    #                                       'REFERENCE   PMID:23555801',
    #                                       'AUTHORS   Bernal-Quiros M, Wu YY, Alarcon-Riquelme ME, Castillejo-Lopez C',
    #                                       'TITLE     BANK1 and BLK act through phospholipase C gamma 2 in B-cell
    #                                       'signaling.',
    #                                       'JOURNAL   PLoS One 8:e59842 (2013)',
    #                                       'DOI:10.1371/journal.pone.0059842',
    #                                       ]
    #                                   ]
    #                   }
    #
    # EXPECTED OUTPUT example:
    # reference_dictionary = {
    #                           'dbxref': 'PMID:11939774'
    #                           'authors': ['Cheong CG', 'Bauer CB', 'Brushaber KR', 'Escalante-Semerena JC',
    #                                       'Rayment I']
    #                           'title': 'Three-dimensional structure of the L-threonine-O-3-phosphate decarboxylase
    #                                     (CobD) enzyme from Salmonella enterica.'
    #                           'journal': 'BANK1 and BLK act through phospholipase C gamma 2 in B-cell signaling.'
    #                           'DOI': 'DOI:10.1021/bi012111w'
    #
    #
    #
    #
    #
    #

    reference_dictionary = {}
    reference_id = []
    authors = []
    title = []
    journal = []
    for lines in entry:
        for line in lines:
            if line.startswith("REFERENCE"):
                reference_id.append("".join(line.split(":")[1]))
                # print(reference_id)  # ###############################################################################
            if line.startswith("  AUTHORS"):
                authors.append(" ".join(line.split()[1:]))
            if line.startswith("  TITLE"):
                title.append(" ".join(line.split()[1:]))
            if line.startswith("  JOURNAL"):
                journal.append(" ".join(line.split()[1:]))
        reference_dictionary.update({"dbxref": reference_id[0], "authors": authors[0].split(","),
                                     "title": title[0], "journal": journal[0]})
    # print(reference_dictionary)
    return reference_dictionary


def read_brite(entry):
    """Parse brite information as an adjacency dictionary containing a list of vertices and a list of edges.
     The combination of the two lists yields a directed, unweighted, acyclic and labeled Graph g=(v,e). The labels of
     the vertices are included in the list of vertices ("vertices) and include the scientific name as well as an
     assigned number (representing their number of addition to the list)."""
    tree = {}
    vertices = []  # list of tuples of labels and count of vertices
    edges = []  # list of edges from roots to branches
    vertices_counter = 0
    stack = []
    for lines in entry:
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
        tree.update({"vertices": vertices})
        tree.update({"edges": edges})
    return tree


def read_dbxrefs(entry):
    """Parse db_links and return a list of dbxrefs"""
    dbxref_id = []
    for lines in entry:
        for line in lines:
            line = line.strip().split()
            for word in line[1:]:
                dbxref_tuple = (line[0], word)
                dbxref_id.append("".join(dbxref_tuple))
    return dbxref_id


def read_information(entry):
    """Parse given key-values information by deleting whitespace and joining the information into a list"""
    information = []
    for lines in entry:
        for line in lines:
            information.append(" ".join(line.split()))
    return information


def get_depth(string):
    """Calculates amount of whitespaces, at the start of a string and returns int"""
    spacecount = len(string) - len(string.lstrip(' '))
    return spacecount


if __name__ == "__main__":
    main()
