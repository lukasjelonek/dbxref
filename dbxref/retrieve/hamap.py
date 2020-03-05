#!/usr/bin/env python3

import dbxref.resolver
import requests
import logging
import json
import argparse

logger = logging.getLogger(__name__)


def main():
    """main()method for script usage"""
    parser = argparse.ArgumentParser(description="Retrieve HAMAP text documents and convert them into dbxref json "
                                                 "format.")
    parser.add_argument("--basics", "-b", action="store_true", help="Include basic information such as name, type, "
                                                                    "dbxref, definition and dates")
    parser.add_argument("--matrix", "-m", action="store_true", help="Include matrix data")
    parser.add_argument("dbxrefs", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    dbxrefs = dbxref.resolver.convert_to_dbxrefs(args.dbxrefs)
    documents = retrieve(dbxrefs, basics=args.basics, matrix=args.matrix)
    print(json.dumps(documents, sort_keys=True, indent=4))


def retrieve(dbxrefs, matrix=False, basics=True):
    """Retrieve text document from expasy/hamap api and parse into json format."""
    # example list input:
    # [
    #  'ID   16SrRNA_methyltr_A; MATRIX.',
    #  'AC   MF_00607;',
    #  'DT   28-FEB-2005 CREATED; 10-MAY-2017 DATA UPDATE; 01-DEC-2013 INFO UPDATE.',
    #  'DE   Ribosomal RNA small subunit methyltransferase A [rsmA].',
    #  'CC   /VERSION=10;',
    #  'MA   /GENERAL_SPEC: ALPHABET='ACDEFGHIKLMNPQRSTVWY'; LENGTH=311; LOG_BASE=1.071779; P0=0.9972;
    #  'MA      P=   7.552363,   1.698108,   5.303439,   6.320015,   4.078187,   6.844419,   2.240667,   5.731561,'
    #   5.941916,   9.343274,   2.356961,   4.531310,   4.927747,   4.024831,   5.158416,   7.224652,   5.747474,
    #   6.524775,   1.251734,   3.199681;',
    #  'MA   /DISJOINT: DEFINITION=PROTECT; N1=6; N2=306;'
    # ]
    #
    # example json output:
    # [
    #     {
    #         "dates": {
    #             "created": "28-FEB-2005",
    #             "last_data_update": "10-MAY-2017",
    #             "last_info_update": "01-DEC-2013"
    #         },
    #         "dbxref": "HM:MF_00607;",
    #         "definition": "Ribosomal RNA small subunit methyltransferase A [rsmA].",
    #         "matrix": [
    #             "/GENERAL_SPEC: ALPHABET='ACDEFGHIKLMNPQRSTVWY'; LENGTH=311; LOG_BASE=1.071779; P0=0.9972;",
    #             "P=   7.552363,   1.698108,   5.303439,   6.320015,   4.078187,   6.844419,   2.240667,   5.731561,
    #             5.941916,   9.343274,   2.356961,   4.531310,   4.927747,   4.024831,   5.158416,   7.224652,
    #             5.747474,   6.524775,   1.251734,   3.199681;",
    #         ],
    #         "name": "16SrRNA_methyltr_A",
    #         "type": "MATRIX"
    #     }
    # ]

    resolved = dbxref.resolver.resolve(dbxrefs, check_existence=False)
    documents = []
    for entry in resolved:
        text_url = entry['locations']['text'][0]
        logger.debug('URL: %s', text_url)
        r = requests.get(text_url)
        logger.debug('Content: %s', r.text)
        lines = r.text.strip().split('\n')
        output = {"id": entry["dbxref"]}
        matrix_list = []
        for line in lines:
            if basics:
                try:
                    if line.startswith("ID"):
                        output.update({"name": line[3:].split(";", 1)[0].strip(),
                                       "type": line[3:].split(";", 1)[1].replace(".", "").strip()
                                       })
                    if line.startswith("AC"):
                        output.update({"dbxref": "HM:" + line[3:].strip()})
                    if line.startswith("DE"):
                        output.update({"definition": line[3:].strip()})
                    if line.startswith("DT"):
                        output.update({"dates": read_date(line)})
                except RuntimeError:
                    logger.warning("Basic information were not or only partly available.")
                    raise
            if matrix:
                try:
                    if line.startswith("MA") and matrix:
                        matrix_list.append(line.replace("MA", "").strip())
                except RuntimeError:
                    logger.warning("Matrix was not available.")
                    raise
        if matrix and matrix_list:
            try:
                output.update({"matrix": matrix_list})
            except RuntimeError:
                logger.warning("An error occurred regarding the matrix.")
                raise
        documents.append(output)
    return documents


def read_date(line):
    """Function that reads the lines given and parses date of creation and last updates."""
    # example string input:
    #
    # DT   28-FEB-2005 CREATED; 10-MAY-2017 DATA UPDATE; 01-DEC-2013 INFO UPDATE.
    #
    # example dictionary output:
    # dates: {
    #         "created": "28-FEB-2005",
    #         "last_data_update": "10-MAY-2017",
    #         "last_info_update": "01-DEC-2013"
    #         }

    dates = line.split(";")
    dates_dic = {}
    for date in dates:
        if "CREATED" in date:
            dates_dic.update({"created": date.replace("DT", " ").replace("CREATED", " ").strip()})
        if "DATA UPDATE" in date:
            dates_dic.update({"last_data_update": date.split("DATA", 1)[0].strip()})
        if "INFO UPDATE" in date:
            dates_dic.update({"last_info_update": date.split("INFO", 1)[0].strip()})
    return dates_dic


if __name__ == "__main__":
    main()
