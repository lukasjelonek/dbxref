#!/usr/bin/env python3

import dbxref.resolver
import requests
import logging
import json
import argparse
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)

ns = {'RefSeq': 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?'}

def main():
    """main()method for script usage"""
    parser = argparse.ArgumentParser(description="Retrieves Nucleotide or Protein Sequences data from RefSeq")
    parser.add_argument("--basics", "-b", action="store_true", help="Include basic information")
    parser.add_argument("--topology", "-to", action="store_true", help="Include topology")
    parser.add_argument("--taxonomy", "-ta", action="store_true", help="Include taxonomy")
    parser.add_argument("--references", "-r", action="store_true", help="Include references")
    parser.add_argument("--source_db", "-s", action="store_true", help="Include source database")
    parser.add_argument("dbxrefs", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    # when not specified include all data available
    if None not in (args.basics, args.topology, args.taxonomy, args.references, args.source_db):
        args.basics = True
        args.topology = True
        args.taxonomy = True
        args.references = True
        args.source_db = True

    dbxrefs = dbxref.resolver.convert_to_dbxrefs(args.dbxrefs)
    documents = retrieve(dbxrefs, basics=args.basics, topology=args.topology, taxonomy=args.taxonomy,
                         references=args.references, source_db=args.source_db)
    print(json.dumps(documents))


def retrieve(dbxrefs, basics, topology, taxonomy, references, source_db):
    """Retrieves Nucleotide or Protein Sequence data from RefSeq as xml and convert it to json format."""
    resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
    documents = []
    xml_url = ""
    for entry in resolved:

        nucleotide_xml_url = entry["locations"]["xml"][0]
        protein_xml_url = entry["locations"]["xml"][1]
        r_n = requests.get(nucleotide_xml_url)
        r_p = requests.get(protein_xml_url)
        if r_n.status_code == 200:
            xml_url = nucleotide_xml_url
        elif r_p.status_code == 200:
            xml_url = protein_xml_url
        print(xml_url)

        logger.debug("URL: %s", xml_url)
        r = requests.get(xml_url)
        refseq = r.text
        logger.debug("Content: %s", refseq)
        output = {"id": entry["dbxref"]}
        try:
            root = ET.fromstring(refseq)
            for child in root.findall("./GBSeq"):
                if basics:
                    output.update(read_basics(child))
                if topology:
                    output.update(read_topology(child))
                if taxonomy:
                    output.update(read_taxonomy(child))
                if references:
                    output.update(read_references(root))
                if source_db:
                    output.update(read_source_db(child))
        except (RuntimeError, ET.ParseError):
            print("An error occurred")
        documents.append(output)
    return documents


def read_basics(entry):
    locus = entry.find("GBSeq_locus").text
    seq_length = entry.find("GBSeq_length").text
    mol_type = entry.find("GBSeq_moltype").text
    definition = entry.find("GBSeq_definition").text
    other_seq_ids = entry.find("GBSeq_other-seqids").text
    return {"locus": locus, "sequence_length": seq_length, "molecular_type": mol_type, "definition": definition,
            "other_sequence_ids": other_seq_ids}


def read_taxonomy(entry):
    taxonomy = entry.find("GBSeq_taxonomy").text
    return {"taxonomy": taxonomy}


def read_references(root):
    references = []
    for child in root.findall("./GBSeq/GBSeq_other-seqids"):
        references.append(child.find("GBSeqid")).text
    return {"references": references}


def read_topology(entry):
    topology = entry.find("GBSeq_topology").text
    return {"topology": topology}


def read_source_db(entry):
    source_db = entry.find("GBSeq_source-db").text
    return {"source_databank": source_db}


if __name__ == "__main__":
    main()
