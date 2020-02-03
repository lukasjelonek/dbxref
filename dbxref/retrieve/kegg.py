#!/usr/bin/env python3

import dbxref.resolver
import requests
import logging
import json
import argparse

logger = logging.getLogger(__name__)
NO_INFO = "NULL"

def main():
    """main()method for script usage"""
    parser = argparse.ArgumentParser(description="Retrieve Kegg text documents and convert them into json")
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

        # kegginfo = {
        #   'REFERENCE' : [
        #     [
        #       'REFERENCE   PMID:11939774',
        #       'AUTHORS   Cheong CG, Bauer CB, Brushaber KR, Escalante-Semerena JC, Rayment I',
        #       'TITLE     Three-dimensional structure of the L-threonine-O-3-phosphate decarboxylase (CobD) enzyme from Salmonella enterica.',
        #       'JOURNAL   Biochemistry 41:4798-808 (2002)',
        #       'DOI:10.1021/bi012111w'
        #      ],
        #      [
        #        'REFERENCE   PMID:11939774',
        #         #       'AUTHORS   Cheong CG, Bauer CB, Brushaber KR, Escalante-Semerena JC, Rayment I',
        #         #       'TITLE     Three-dimensional structure of the L-threonine-O-3-phosphate decarboxylase (CobD) enzyme from Salmonella enterica.',
        #         #       'JOURNAL   Biochemistry 41:4798-808 (2002)',
        #         #       'DOI:10.1021/bi012111w'
        #      ]
        #    ]
        # }

        # Sorting the received list 'line' in a dictionary with the terms (f.e.: 'ENTRY', 'NAMES') as keys
        kegg_information = parse_entry(lines)
        # Search dictionary for existence of keywords requested by user.
        # If the keyword is present the data receiving function() is started and is put into the output file
        # Every keyword is a single search, to make the code more robust if keywords are missing
        if basics:
            if "ENTRY" in kegg_information:
                entry_information = read_id(kegg_information["ENTRY"])
                output.update({"id": entry_information[0]})
                output.update({"type": entry_information[1]})
                if len(entry_information) > 3:
                    output.update({"associated organism": entry_information[2]})
            if "NAME" in kegg_information:
                output.update({"names": read_information(kegg_information["NAME"])[0].replace(",", "").split()})
            if "DEFINITION" in kegg_information:
                output.update({"definition": read_information(kegg_information["DEFINITION"])[0]})
            if "ORGANISM" in kegg_information:
                output.update({"organism": read_information(kegg_information["ORGANISM"])[0]})
            else:
                print("Entry: " + NO_INFO)
        if pathway:
            if "PATHWAY" in kegg_information:
                output.update({"pathways": read_information(kegg_information["PATHWAY"])})
            else:
                print("Pathway: " + NO_INFO)
        if genes:
            if "GENES" in kegg_information:
                output.update({"genes": read_information(kegg_information["GENES"])})
            else:
                print("Genes: " + NO_INFO)
        if orthology:
            if "ORTHOLOGY" in kegg_information:
                output.update({"ortholog genes": read_information(kegg_information["ORTHOLOGY"])})
            else:
                print("Orthology: " + NO_INFO)
        if motif:
            if "MOTIF" in kegg_information:
                output.update({"motif": read_information(kegg_information["MOTIF"])})
            else:
                print("Motif: " + NO_INFO)
        if formula:
            if "FORMULA" in kegg_information:
                output.update({"chemical formula": read_information(kegg_information["FORMULA"][0])})
            else:
                print("Formula: " + NO_INFO)
        if reaction:
            if "REACTION" in kegg_information:
                output.update({"reaction partners": read_information(kegg_information["REACTION"])})
            else:
                print("Reaction: " + NO_INFO)
        if brite:
            if "BRITE" in kegg_information:
                output.update({"brite": read_brite(kegg_information["BRITE"])})
            else:
                print("Brite: " + NO_INFO)
        if reference:
            if "REFERENCE" in kegg_information:
                output.update({"reference": read_reference(kegg_information["REFERENCE"])})
            else:
                print("Reference: " + NO_INFO)
        if dbxrefs_links:
            if "DBLINKS" in kegg_information:
                output.update({"dbxref_links": read_dbxrefs(kegg_information["DBLINKS"])})
            else:
                print("dbxref_links: " + NO_INFO)
        documents.append(output)
    return documents


def parse_entry(lines):
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
            elif line[0:4].isupper():
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
    """Parse entry information (id, type and associated organism) as dictionaries"""
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
    # expected input (example):
    #  [
    #       'REFERENCE   PMID:11939774',
    #       'AUTHORS   Cheong CG, Bauer CB, Brushaber KR, Escalante-Semerena JC, Rayment I',
    #       'TITLE     Three-dimensional structure of the L-threonine-O-3-phosphate decarboxylase (CobD) enzyme from Salmonella enterica.',
    #       'JOURNAL   Biochemistry 41:4798-808 (2002)',
    #       'DOI:10.1021/bi012111w'
    #      ],

    # output:
    # [
    #   {
    #     'title': '..',

    #   }
    # ]
    reference_output = []
    for lines in entry:
        next_reference = {"dbxref": "", "authors": "", "title": "", "journal": "",
                          "doi": ""}  # Create a new Dictionary with empty values
        for line in lines:
            if line.startswith("REFERENCE"):
                next_reference["dbxref"] = "".join(line.strip().split(" ", )[-1].replace("[", "").replace("]", ""))
            if line.startswith("  AUTHORS"):
                next_reference["authors"] = " ".join(line.split()[1:])
            if line.startswith("  TITLE"):
                next_reference["title"] = " ".join(line.split()[1:])
            if line.startswith("  JOURNAL"):
                next_reference["journal"] = " ".join(line.split()[1:])
            if line.strip().startswith("DOI:"):
                next_reference["DOI"] = line.split(":")[1:]
        reference_output.append(next_reference)
    return reference_output


def test(entry):
    """Parse brite information as an adjacency dictionary containing a list of vertices and a list of edges.
     The combination of the two lists yields a directed, unweighted, acyclic and labeled Graph g=(v,e). The labels of
     the vertices are included in the list of vertices ("vertices) and include the scientific name"""
    tree = {}
    vertices = []  # list of tuples of labels and count of vertices
    edges = {}  # list of edges from roots to branches
    vertices_counter = 0
    stack = []
    for lines in entry:
        for line in lines:
            depth = get_depth(line)-12
            if depth <= 0:
                stack = [(" ".join(line.split()), vertices_counter)]
            else:  # line is a branch
                new_branch = (" ".join(line.split()), vertices_counter)
                if depth <= len(stack):  # line is a branch not from the line above, stack is emptied until depth fits
                    stack = stack[:depth]
                else:  # line is a new branch of the branch above
                    pass
                stack.append(new_branch)
            vertices.append(stack[-1][0])  # append name of v. only, v-counter unnecessary because equals position
            if len(stack) == 1:  # only root in stack
                pass
            else:  # more than root in stack
                edges[stack[-2]][1].append(stack[-1][1])
            vertices_counter += 1
        tree.update({"vertices": vertices})
        tree.update({"edges": edges})
    return tree


def read_brite(entry):
    tree = {}
    # create list of vertices
    vertices = []
    for lines in entry:
        for line in lines:
            vertices.append(" ".join(line.replace("BRITE", "").split()))

    # create list of edges
    stack = []
    edges = {str(i): [] for i, _ in enumerate(vertices)}
    for lines in entry:
        for line in lines:
            depth = get_depth(line)-12
            if depth <= 0:
                stack = [(" ".join(line.replace("BRITE", "").split()), len(stack))]
            else:
                new_branch = (" ".join(line.split()), len(stack))
                if depth <= len(stack):  # line is a branch not from the line above, stack is emptied until depth fits
                    stack = stack[:depth]
                else:  # line is a new branch of the branch above
                    pass
                stack.append(new_branch)
            if len(stack) == 1:  # only root in stack
                pass
            else:  # more than root in stack
                edges[str(vertices.index(stack[-2][0]))].append(str(vertices.index(stack[-1][0])))
    tree.update({"vertices": vertices})
    tree.update({"edges": edges})
    return tree


def read_dbxrefs(entry):
    """Parse db_links and return a list of dbxrefs"""
    dbxref_id = []
    for lines in entry:
        for line in lines:
            line = line.strip().split()
            if "DBLINKS" in line[0]:
                for word in line[2:]:
                    dbxref_tuple = (line[1], word)
                    dbxref_id.append("".join(dbxref_tuple))
            else:
                for word in line[1:]:
                    dbxref_tuple = (line[0], word)
                    dbxref_id.append("".join(dbxref_tuple))
    return dbxref_id


def read_information(entry):
    """Parse given key-values information by deleting whitespace and joining the information into a list"""
    information = []
    for lines in entry:
        for line in lines:
            information.append(" ".join(line.replace("NAME", "").replace("DEFINITION", "").replace("", "")
                                        .replace("ORGANISM", "").replace("PATHWAY", "").replace("GENES", "")
                                        .replace("ORTHOLOGY", "").replace("MOTIF", "").replace("FORMULA", "")
                                        .replace("REACTION", "").split()))
    return information


def get_depth(string):
    """Calculates amount of whitespaces, at the start of a string and returns int"""
    spacecount = len(string) - len(string.lstrip(' '))
    return spacecount


if __name__ == "__main__":
    main()
