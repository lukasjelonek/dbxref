#!/usr/bin/env python3

import dbxref.resolver
import requests
import logging
import json
import argparse
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)


def main():
    """main()method for script usage"""
    parser = argparse.ArgumentParser(description="Retrieves Nucleotide or Protein Sequences data from RefSeq")
    parser.add_argument("--basics", "-b", action="store_true", help="Include basic information")
    parser.add_argument("--taxonomy", "-ta", action="store_true", help="Include taxonomy")
    parser.add_argument("--references", "-r", action="store_true", help="Include references")
    parser.add_argument("--source_db", "-s", action="store_true", help="Include source database")
    parser.add_argument("--features_table", "-f", action="store_true", help="Include table of features")
    parser.add_argument("dbxrefs", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    # when not specified include all data available
    if None not in (args.basics, args.taxonomy, args.references, args.source_db, args.features_table):
        args.basics = True
        args.taxonomy = True
        args.references = True
        args.source_db = True
        args.features_table = True

    dbxrefs = dbxref.resolver.convert_to_dbxrefs(args.dbxrefs)
    documents = retrieve(dbxrefs, basics=args.basics, taxonomy=args.taxonomy,
                         references=args.references, source_db=args.source_db, features_table=args.features_table)
    print(json.dumps(documents, sort_keys=True, indent=4))


def retrieve(dbxrefs, basics=True, taxonomy=False, references=False, source_db=False, features_table=False):
    """Retrieves Nucleotide or Protein Sequence data from RefSeq as xml and convert it to json format."""
    # expected xml input (example):
    # <GBSet>
    #    <GBSeq>
    #        <GBSeq_locus>X52740</GBSeq_locus>
    #        <GBSeq_length>1762</GBSeq_length>
    #        <GBSeq_strandedness>single</GBSeq_strandedness>
    #        [.....]
    #        <GBSeq_moltype>mRNA</GBSeq_moltype>
    #        <GBSeq_sequence></GBSeq_sequence>
    #    </GBSeq>
    # </GBSet>
    #
    # expected xml output (example):
    # [
    #     {
    #         "locus": "3269",
    #         "sequence_length": "322",
    #         "molecular_type": "AA",
    #     }
    # ]

    resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
    documents = []
    xml_url = ""
    r = None
    for entry in resolved:
        nucleotide_xml_url = entry["locations"]["xml"][0]
        logger.debug("URL: %s", nucleotide_xml_url)
        protein_xml_url = entry["locations"]["xml"][1]
        logger.debug("URL: %s", protein_xml_url)
        r_n = requests.get(nucleotide_xml_url)
        r_p = requests.get(protein_xml_url)
        if r_n.status_code == 200:
            r = r_n
        elif r_p.status_code == 200:
            r = r_p
        else:
            return print("There is no entry for the given ID. Please check the ID.")
        refseq = r.text
        logger.debug("Content: %s", refseq)
        output = {"id": entry["dbxref"]}
        try:
            root = ET.fromstring(refseq)
            for child in root.findall("./GBSeq"):  # iterate over children and perform parsing tasks
                if basics:
                    try:
                        output.update(read_basics(child))
                    except AttributeError:
                        logger.warning("One ore more of the basic information were not available for given dbxref. "
                              "Please check the dbxref.")
                        raise
                    try:
                        output.update(read_topology(child))
                    except AttributeError:
                        logger.warning("No topology available for given dbxref")
                        raise
                if taxonomy:
                    try:
                        output.update(read_taxonomy(child))
                    except AttributeError:
                        logger.warning("No taxonomy available for given dbxref")
                        raise
                if references:
                    try:
                        output.update(read_references(child))
                    except AttributeError:
                        logger.warning("No references available for given dbxref")
                        raise
                if source_db:
                    try:
                        output.update(read_source_db(child))
                    except AttributeError:
                        logger.warning("No source database available for given dbxref")
                        raise
                if features_table:
                    try:
                        output.update(read_features(child))
                    except AttributeError:
                        logger.warning("No table of features available for given dbxref")
                        raise
        except (RuntimeError, ET.ParseError):
            logger.warning("An error occurred")
            raise
        documents.append(output)
    return documents


def read_basics(entry):
    """Receives child (xml) and converts information into a dictionary (json format compatible)"""
    locus = entry.find("GBSeq_locus").text
    seq_length = entry.find("GBSeq_length").text
    mol_type = entry.find("GBSeq_moltype").text
    definition = entry.find("GBSeq_definition").text
    other_seq_ids = []
    for child in entry.findall("GBSeq_other-seqids/GBSeqid"):
        other_seq_ids.append(child.text)
    dbxref_id = entry.find("GBSeq_primary-accession").text
    organism = entry.find("GBSeq_organism").text
    accession_version = entry.find("GBSeq_accession-version").text
    return {"locus": locus, "sequence_length": seq_length, "molecular_type": mol_type, "definition": definition,
            "other_sequence_ids": other_seq_ids, "dbxref": "RefSeq:" + dbxref_id, "organism": organism,
            "accession_version": accession_version}


def read_references(entry):
    """Receives child (xml) and converts information into a dictionary (json format compatible)"""
    references_list = []
    authors = []
    for child in entry.findall("GBSeq_references/GBReference"):
        for grandchild in child.find("GBReference_authors"):
            authors.append(grandchild.text)
        single_reference = {"authors": authors,
                            "title": child.find("GBReference_title").text,
                            "journal": child.find("GBReference_journal").text}
        references_list.append(single_reference)
        single_reference = {}
        authors = []
    return {"references": references_list}


def read_features(entry):
    """Receives child (xml) and converts information into a dictionary (json format compatible)"""
    features_table = []
    for feature in entry.findall("GBSeq_feature-table/GBFeature"):
        key = feature.find("GBFeature_key").text
        location = feature.find("GBFeature_location").text
        intervals = []
        for child in feature.find("GBFeature_intervals"):
            single_interval = {"from": child.find("GBInterval_from").text, "to": child.find("GBInterval_to").text,
                               "accession": child.find("GBInterval_accession").text}
            intervals.append(single_interval)
        qualifier = []
        for child in feature.find("GBFeature_quals"):
            single_qualifier = {"name": child.find("GBQualifier_name").text, "value": child.find("GBQualifier_value").text}
            qualifier.append(single_qualifier)
        features_table.append({"key": key, "location": location, "intervals": intervals, "qualifier": qualifier})
    return {"features_table": features_table}


# Following functions could also be written in retrieve()-function for more compact code
def read_taxonomy(entry):
    return {"taxonomy": entry.find("GBSeq_taxonomy").text}


def read_topology(entry):
    return {"topology": entry.find("GBSeq_topology").text}


def read_source_db(entry):
    return {"source_databank": entry.find("GBSeq_source-db").text}


if __name__ == "__main__":
    main()
