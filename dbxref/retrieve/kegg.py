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


def retrieve(dbxrefs, basics = True, pathway = True, brite = True, dbxrefs_links = True, genes = False, reference = True, orthology = True, motif = True, formula = True, reaction = True):
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
              logger.warn("No Entry")
        if pathway:
            if "PATHWAY" in kegg_information:
                output.update({"pathways": read_information(kegg_information["PATHWAY"])})
            else:
              logger.warn("No Pathway")
        if genes:
            if "GENES" in kegg_information:
                output.update({"genes": read_information(kegg_information["GENES"])})
            else:
              logger.warn("No Genes")
        if orthology:
            if "ORTHOLOGY" in kegg_information:
                output.update({"ortholog genes": read_information(kegg_information["ORTHOLOGY"])})
            else:
              logger.warn("No orthology")
        if motif:
            if "MOTIF" in kegg_information:
                output.update({"motif": read_information(kegg_information["MOTIF"])})
            else:
              logger.warn("No motif")
        if formula:
            if "FORMULA" in kegg_information:
                output.update({"chemical formula": read_information(kegg_information["FORMULA"][0])})
            else:
              logger.warn("No formula")
        if reaction:
            if "REACTION" in kegg_information:
                output.update({"reaction partners": read_information(kegg_information["REACTION"])})
            else:
              logger.warn("No reaction")
        if brite:
            if "BRITE" in kegg_information:
                output.update({"brite": read_brite(kegg_information["BRITE"])})
            else:
              logger.warn("No brite")
        if reference:
            if "REFERENCE" in kegg_information:
                output.update({"reference": read_reference(kegg_information["REFERENCE"])})
            else:
              logger.warn("No reference")
        if dbxrefs_links:
            if "DBLINKS" in kegg_information:
                output.update({"dbxref_links": read_dbxrefs(kegg_information["DBLINKS"])})
            else:
              logger.warn("No dbxref_links")
        documents.append(output)
    return documents


def parse_entry(lines):
    """Parses the entire entry document (text) and returns a dictionary containing the left indented titles as keys with
    the corresponding lines in a list of strings as values. "kegg_information" contains the entire information of the
    given text document, no information is dismissed, even when it might not be used later (f.e. it was not requested).
    """
    # expected input (example):
    # ENTRY       K00768                      KO
    # NAME        E2.4.2.21, cobU, cobT
    # DEFINITION  nicotinate-nucleotide--dimethylbenzimidazole phosphoribosyltransferase [EC:2.4.2.21]
    # PATHWAY     ko00860  Porphyrin and chlorophyll metabolism
    #             ko01100  Metabolic pathways
    # MODULE      M00122  Cobalamin biosynthesis, cobinamide => cobalamin
    # BRITE       KEGG Orthology (KO) [BR:ko00001]
    #              09100 Metabolism
    #               09108 Metabolism of cofactors and vitamins
    #                00860 Porphyrin and chlorophyll metabolism
    #                 K00768  E2.4.2.21, cobU, cobT; nicotinate-nucleotide--dimethylbenzimidazole phosphoribosyltransferase
    #
    # expected output (example):
    # kegg_information = {
    #                       'ENTRY': ['ENTRY       K00768                      KO']
    #                       'NAME': ['NAME        E2.4.2.21, cobU, cobT']
    #                       'DEFINITION': [DEFINITION  nicotinate-nucleotide--dimethylbenzimidazole phosphoribosyltransferase [EC:2.4.2.21]]
    #                       'PATHWAY': ['PATHWAY     ko00860  Porphyrin and chlorophyll metabolism',
    #                                   '            ko01100  Metabolic pathways']
    #                       'MODULE': ['MODULE      M00122  Cobalamin biosynthesis, cobinamide => cobalamin']
    #                       'BRITE': ['BRITE       KEGG Orthology (KO) [BR:ko00001',
    #                                 '             09100 Metabolism',
    #                                 '              09108 Metabolism of cofactors and vitamins',
    #                                 '               00860 Porphyrin and chlorophyll metabolism',
    #                                 '                K00768  E2.4.2.21, cobU, cobT; nicotinate-nucleotide--dimethylbenzimidazole phosphoribosyltransferase']
    #                     }

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
    # expected input (example):
    # kegg_information['ENTRY']: [
    #                               'ENTRY       10458             CDS       T01001'
    #                             ]
    #
    # expected output (example):
    # entry_id = ['10458']
    # entry_type = ['CDS']
    # associated_organism = "T01001"

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
    # kegg_information['REFERENCE']:
    #                               [
    #                               'REFERENCE   PMID:11939774'
    #                               'AUTHORS   Cheong CG, Bauer CB, Brushaber KR, Escalante-Semerena JC, Rayment I'
    #                               'TITLE     Three-dimensional structure of the L-threonine-O-3-phosphate
    #                               decarboxylase (CobD) enzyme from Salmonella enterica.'
    #                               'JOURNAL   Biochemistry 41:4798-808 (2002)'
    #                               'DOI:10.1021/bi012111w'
    #                               ],
    #                               [
    #                               'REFERENCE   PMID:11939774',
    #                               'AUTHORS   Cheong CG, Bauer CB, Brushaber KR, Escalante-Semerena JC, Rayment I'
    #                               'TITLE     Three-dimensional structure of the L-threonine-O-3-phosphate
    #                               decarboxylase (CobD) enzyme from Salmonella enterica.'
    #                               'JOURNAL   Biochemistry 41:4798-808 (2002)'
    #                               'DOI:10.1021/bi012111w'
    #                               ]
    #
    # expected output (example):
    # reference output = [
    #                       {
    #                       'dbxref': 'PMID:11939774',
    #                       'authors': ['Cheong CG', 'Bauer CB', 'Brushaber KR', 'Escalante-Semerena JC', 'Rayment I']
    #                       'title': 'Three-dimensional structure of the L-threonine-O-3-phosphate decarboxylase (CobD)
    #                                 enzyme from Salmonella enterica.'
    #                       'journal': 'Biochemistry 41:4798-808 (2002)'
    #                       'DOI': '10.1021/bi012111w'
    #                        },
    #                       {
    #                       'dbxref': 'PMID:11939774',
    #                       'authors': ['Cheong CG', 'Bauer CB', 'Brushaber KR', 'Escalante-Semerena JC', 'Rayment I']
    #                       'title': 'Three-dimensional structure of the L-threonine-O-3-phosphate decarboxylase (CobD)
    #                                 enzyme from Salmonella enterica.'
    #                       'journal': 'Biochemistry 41:4798-808 (2002)'
    #                       'DOI': '10.1021/bi012111w'
    #                        }
    #                    ]

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


def read_brite(entry):
    """Parse brite information as an adjacency dictionary containing a list of vertices and a list of edges.
    The combination of the two lists yields a directed, unweighted, acyclic and labeled Graph g=(v,e). The labels of
    the vertices are included in the list of vertices ("vertices) and include the scientific name"""
    # expected input (example):
    # kegg_information["BRITE"] = [
    #                               ["BRITE       KEGG Orthology (KO) [BR:hsa00001]"],
    #                               ["             09140 Cellular Processes"],
    #                               ["              09144 Cellular community - eukaryotes"],
    #                               ["               04520 Adherens junction"],
    #                               ["                10458 (BAIAP2)"],
    #                               ["              09142 Cell motility"]
    #                               ["               04810 Regulation of actin cytoskeleton"]
    #                               ["                10458 (BAIAP2)"]
    #                              ]
    #
    # expected output (example):
    # tree = {"vertices": ["KEGG Orthology (KO) [BR:hsa00001]", "09140 Cellular Processes",
    #                                       "09144 Cellular community - eukaryotes", "04520 Adherens junction",
    #                                       "04520 Adherens junction", "10458 (BAIAP2)", "09142 Cell motility",
    #                                       "04810 Regulation of actin cytoskeleton", "10458 (BAIAP2)"],
    #         "edges": {"0": ["1"],
    #                   "1": ["2", "5"],
    #                   "2": ["3"],
    #                   "3": ["4"],
    #                   "4": ["],
    #                   "5": ["6"]
    #                   "6": ["7"]
    #                   "7": []
    #                   }
    #        }

    tree = {}
    # create list of vertices containing the labels of the graph
    vertices = []
    for lines in entry:
        for line in lines:
            vertices.append(" ".join(line.replace("BRITE", "").split()))

    # create a dictionary 'edges' containing a key for every label in 'vertices' with an empty list[] as value that
    # gets filled in the following progress
    edges = {str(i): [] for i, _ in enumerate(vertices)}
    stack = []  # create a list that will be used as a stack (first in, last out)
    for lines in entry:
        for line in lines:
            depth = get_depth(line)-12  # save amount of whitespace as depth, depth 0 means 12 whitespaces in front
            if depth <= 0:  # new root
                stack = [(" ".join(line.replace("BRITE", "").split()), len(stack))]  # empty entire stack, set new root
            else:  # not a root = is a branch
                new_branch = (" ".join(line.split()), len(stack))  # save branch with label and depth
                if depth <= len(stack):  # line is a branch not from the line above
                    stack = stack[:depth]  # stack is emptied until depth > len(stack)
                else:  # line is a new branch of the branch above
                    pass
                stack.append(new_branch)
            if len(stack) == 1:  # only root in stack
                pass
            else:  # more than root in stack
                # new adjacency is saved in 'edges' under the corresponding key that has the connection to a new branch
                edges[str(vertices.index(stack[-2][0]))].append(str(vertices.index(stack[-1][0])))
    tree.update({"vertices": vertices})
    tree.update({"edges": edges})
    return tree


def read_dbxrefs(entry):
    """Parse db_links and return a list of dbxrefs"""
    # expected input (example):
    # kegg_information["DBLINKS"] = [
    #                                'DBLINKS     PubChem: 4509',
    #                                'ChEBI: 17950',
    #                                'LIPIDMAPS: LMSP0501AB00',
    #                                'LipidBank: GSG1147'
    #                                ]
    #
    # expected output (example):
    # dbxref_id = [
    #              'PubChem:4509',
    #              'ChEBI:17950',
    #              'LIPIDMAPS:LMSP0501AB00',
    #              'LipidBank:GSG1147'
    #              ]

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
    # expected input (example):
    # kegg_information[""]: [
    #                        'PATHWAY     ko00860  Porphyrin and chlorophyll metabolism'
    #                        '            ko01100  Metabolic pathways'
    #                        ]
    #
    # expected output (example):
    # information = ['ko00860  Porphyrin and chlorophyll metabolism',
    #                'ko01100  Metabolic pathways'
    #                ]

    information = []
    for lines in entry:
        for line in lines:
            information.append(" ".join(line.replace("NAME", "").replace("DEFINITION", "").replace("", "")
                                        .replace("ORGANISM", "").replace("PATHWAY", "").replace("GENES", "")
                                        .replace("ORTHOLOGY", "").replace("MOTIF", "").replace("FORMULA", "")
                                        .replace("REACTION", "").split()))
    return information


def get_depth(string):
    """Calculates amount of whitespaces leading the given string and returns int"""
    # expected input (example):
    # string = ['             09140 Cellular Processes']
    #
    # expected output (example):
    # depth = 13

    depth = len(string) - len(string.lstrip(' '))
    return depth


if __name__ == "__main__":
    main()
