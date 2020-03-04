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
    parser = argparse.ArgumentParser(description="Retrieves Protein Information from NCBIs Gene Identifier. "
                                                 "Database: Protein")
    parser.add_argument("--basics", "-b", action="store_true", help="Include basic informations such as "
                                                                    "dbxref/accession-nr., locus, source organism and "
                                                                    "definition.")
    parser.add_argument("--dbsource", "-db", action="store_true", help="Include source database information.")
    parser.add_argument("--references", "-r", action="store_true", help="Include reference information.")
    parser.add_argument("dbxref", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    # When not specified, include all information available
    if None not in (args.basics, args.dbsource, args.references):
        args.basics = True
        args.dbsource = True
        args.references = True

    dbxrefs = dbxref.resolver.convert_to_dbxrefs(args.dbxref)
    documents = retrieve(dbxrefs, basics=args.basics, dbsource=args.dbsource, references=args.references)
    print(json.dumps(documents, sort_keys=True, indent=4))


def retrieve(dbxrefs, basics=True, dbsource=True, references=True):
    """Retrieve Protein data as xml and parse into json format"""
    resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
    documents = []
    for entry in resolved:
        xml_url = entry["locations"]["xml"][0]
        logger.debug("URL: %s", xml_url)
        gi = requests.get(xml_url)
        logger.debug("Content: %s", gi.text)
        output = {"id": entry["dbxref"]}
        try:
            root = ET.fromstring(gi.text)
            if basics:
                try:
                    output.update(read_basics(root))
                except KeyError:
                    print("One ore more of the basic information were not available for given dbxref. "
                          "Please check the source data.")
                    raise
            if dbsource:
                try:
                    output.update(read_dbsource(root))
                except KeyError:
                    print("Source database information wasn't or wasn't fully available. Please check the source data")
                    raise
            if references:
                try:
                    output.update(read_references(root))
                except KeyError:
                    print("reference information wasn't or wasn't fully available. Please check the source data")
                    raise
        except (RuntimeError, ET.ParseError):
            print("An error occurred")
            raise
        documents.append(output)
    return documents


def read_basics(root):
    """Finds basic information such as locus, dbxref, definition, organism, molecular information and representational
    structure, if available, and puts out a dictionary containing the information"""
    locus = root.find("Seq-entry_seq/Bioseq/Bioseq_id/Seq-id/Seq-id_swissprot/Textseq-id/Textseq-id_name").text
    dbxref_id = "GI:" + root.find("Seq-entry_seq/Bioseq/Bioseq_id/Seq-id/Seq-id_swissprot/Textseq-id/"
                                  "Textseq-id_accession").text
    definition = root.find("Seq-entry_seq/Bioseq/Bioseq_descr/Seq-descr/Seqdesc/Seqdesc_title").text
    organism = {"name": root.find("Seq-entry_seq/Bioseq/Bioseq_descr/Seq-descr/Seqdesc/Seqdesc_source/BioSource/"
                                  "BioSource_org/Org-ref/Org-ref_orgname/OrgName/OrgName_name/"
                                  "OrgName_name_binomial/BinomialOrgName/BinomialOrgName_genus").text + " " +
                root.find("Seq-entry_seq/Bioseq/Bioseq_descr/Seq-descr/Seqdesc/Seqdesc_source/BioSource/"
                          "BioSource_org/Org-ref/Org-ref_orgname/OrgName/OrgName_name/OrgName_name_binomial/"
                          "BinomialOrgName/BinomialOrgName_species").text,
                "taxonomy": root.find("OrgName_lineage")}
    mol_info = root.find("MolInfo_biomol")
    structure = root.find("Seqdesc_comment")
    return {"locus": locus, "dbxref": dbxref_id, "definition": definition, "organism": organism,
            "molecular_info": mol_info, "structure": structure}


def read_dbsource(root):
    """Finds databank sources in the xmland puts out a list with all dbxrefs found."""
    dbxref_list = []
    for dbtag in root.findall("Seq-entry_seq/Bioseq/Bioseq_descr/Seq-descr/Seqdesc/Seqdesc_sp/SP-block/SP-block_dbref/"
                              "Dbtag"):
        dbxref_list.append(dbtag.find("Dbtag_db").text + ":" + dbtag.find("Dbtag_tag/Object-id/Object-id_str").text)
    return {"source databases": dbxref_list}


def read_references(root):
    """Finds reference information in the xml and puts out a list containing information for authors, title, journal
    and pubmed DOI"""
    references = []
    for cit_art in root.findall("Seq-entry_seq/Bioseq/Bioseq_descr/Seq-descr/Seqdesc/Seqdesc_pub/Pubdesc/Pubdesc_pub/"
                                "Pub-equiv/Pub/Pub_article/Cit-art"):
        author_list = []
        journal = {}
        title = ""
        doi = ""
        # Find Authors
        for author in cit_art.findall("Cit-art_authors/Auth-list/Auth-list_names/Auth-list_names_std/Author"):
            author_list.append(author.find("Author_name/Person-id/Person-id_name/Name-std/Name-std_last").text + ", " +
                               author.find("Author_name/Person-id/Person-id_name/Name-std/Name-std_initials").text)
        # Find Title
        title = cit_art.find("Cit-art_title/Title/Title_E/Title_E_name").text
        # Find Journal
        journal = {"name": cit_art.find("Cit-art_from/Cit-art_from_journal/Cit-jour/Cit-jour_title/Title/Title_E/"
                                        "Title_E_iso-jta").text,
                   "date": cit_art.find("Cit-art_from/Cit-art_from_journal/Cit-jour/Cit-jour_imp/Imprint/Imprint_date/"
                                        "Date/Date_std/Date-std/Date-std_day").text + "." +
                           cit_art.find("Cit-art_from/Cit-art_from_journal/Cit-jour/Cit-jour_imp/Imprint/Imprint_date/"
                                        "Date/Date_std/Date-std/Date-std_month").text + "." +
                           cit_art.find("Cit-art_from/Cit-art_from_journal/Cit-jour/Cit-jour_imp/Imprint/Imprint_date/"
                                        "Date/Date_std/Date-std/Date-std_year").text
                   }
        # Find Pubmed DOI
        doi = cit_art.find("Cit-art_ids/ArticleIdSet/ArticleId/ArticleId_doi/DOI").text
        # Put into dictionary
        references.append({"authors": author_list,
                           "title": title,
                           "journal": journal,
                           "doi": doi
                           })
    return {"references": references}


if __name__ == "__main__":
    main()
