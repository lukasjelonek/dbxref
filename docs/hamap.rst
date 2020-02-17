.. highlight:: yaml

HAMAP
======

Retrieve HAMAP text documents for dbxrefs and convert them into json.

Options
-------

  * ``--basics`` - Include basic information such as name, type, dbxref, definition and dates.
  * ``--matrix`` - Include matrix.

Input
-----

example: ``HM:MF_00607``


Output
------

output scheme::

[
    {
    "dates": {
                "created": "28-FEB-2005",
                "last_data_update": "10-MAY-2017",
                "last_info_update": "01-DEC-2013"
            },
    "dbxref": "HM:MF_00607;",
    "definition": "Ribosomal RNA small subunit methyltransferase A [rsmA].",
    "matrix": [
                "/GENERAL_SPEC: ALPHABET='ACDEFGHIKLMNPQRSTVWY'; LENGTH=311; LOG_BASE=1.071779; P0=0.9972;",
                "P=   7.552363,   1.698108,   5.303439,   6.320015,   4.078187,   6.844419,   2.240667,   5.731561,
                5.941916,   9.343274,   2.356961,   4.531310,   4.927747,   4.024831,   5.158416,   7.224652,
                5.747474,   6.524775,   1.251734,   3.199681;",
            ],
    "name": "16SrRNA_methyltr_A",
    "type": "MATRIX"
    }
]