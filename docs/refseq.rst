.. highlight:: yaml

RefSeq
====

Retrieve RefSeq xml documents for dbxrefs and convert them into json.

Options
-------

    * ``--basics`` - Include basic information
    * ``--topology`` - Include topology
    * ``--taxonomy`` - Include taxonomy
    * ``--references`` - Include references
    * ``--source_db`` - Include source database
    * ``--features_table`` - Include table of features

Input
-----

example: ``RefSeq:3269``


Output
------

output scheme::

[
    {
        "accession_version": null,
        "dbxref": "RefSeq:3269",
        "definition": "ornithine carbamoyltransferase (AA 1 - 322)",
        "features_table": [
            {
                "intervals": [
                    {
                        "accession": "3269",
                        "from": "1",
                        "to": "322"
                    }
                ],
                "key": "source",
                "location": "1..322",
                "qualifier": [
                    {
                        "name": "organism",
                        "value": "unknown"
                    }
                ]
            },
            {
                "intervals": [
                    {
                        "accession": "3269",
                        "from": "1",
                        "to": "322"
                    }
                ],
                "key": "Protein",
                "location": "1..322",
                "qualifier": [
                    {
                        "name": "name",
                        "value": "ornithine carbamoyltransferase (AA 1 - 322)"
                    },
                    {
                        "name": "calculated_mol_wt",
                        "value": "35456"
                    }
                ]
            },
            {
                "intervals": [
                    {
                        "accession": "3269",
                        "from": "1",
                        "to": "322"
                    }
                ],
                "key": "CDS",
                "location": "1..322",
                "qualifier": [
                    {
                        "name": "coded_by",
                        "value": "X15412.3:1047..2015"
                    },
                    {
                        "name": "transl_table",
                        "value": "1"
                    }
                ]
            }
        ],
        "id": "RefSeq:3269",
        "locus": "3269",
        "molecular_type": "AA",
        "organism": "Unknown.",
        "other_sequence_ids": [
            "gi|3269"
        ],
        "references": [
            {
                "authors": [
                    "Maleszka,R."
                ],
                "journal": "Submitted (07-DEC-1989) to the EMBL/GenBank/DDBJ databases. Maleszka R., Molecular & Population Genetics Group, Research School of Biological Sciences, Australian National University, GPO Box 475, Canberra A C T 2601, Australia",
                "title": "Direct Submission"
            },
            {
                "authors": [
                    "Skrzypek,M.",
                    "Borsuk,P.",
                    "Maleszka,R."
                ],
                "journal": "Yeast 6 (2), 141-148 (1990)",
                "title": "Cloning and sequencing of the ornithine carbamoyltransferase gene from Pachysolen tannophilus"
            }
        ],
        "sequence_length": "322",
        "source_databank": "embl locus PTOTC, accession X15412.3",
        "taxonomy": "Unclassified",
        "topology": "linear"
    }
]
