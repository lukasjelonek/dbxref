.. highlight:: yaml

Pubmed
=================

Retrieve Pubmed json documents for dbxrefs and convert them into dbxref json format.

Options
-------

  * ``--basics`` - Include basic information such as title, language, dbxref-id, and day of publishment on pubmed.
  * ``--references`` - Include reference information such as journal name, DOI, authors and day of publishment.
  * ``--article_ids`` - Include article-IDs.

Input
-----

example: ``PM:19393038``


Output
------

output scheme::

[
    {
        "article_IDs": [
            "pubmed: 19393038",
            "pii: gb-2009-10-4-r42",
            "doi: 10.1186/gb-2009-10-4-r42",
            "pmc: PMC2688933",
            "rid: 19393038",
            "eid: 19393038",
            "pmcid: pmc-id: PMC2688933;"
        ],
        "dbxref_id": "PM:19393038",
        "epublic-date": "24.Apr.2009",
        "language": [
            "eng"
        ],
        "references": {
            "DOI": "10.1186/gb-2009-10-4-r42",
            "authors": [
                "Zimin, AV",
                "Delcher, AL",
                "Florea, L",
                "Kelley, DR",
                "Schatz, MC",
                "Puiu, D",
                "Hanrahan, F",
                "Pertea, G",
                "Van, Tassell CP",
                "Sonstegard, TS",
                "Mar\u00e7ais, G",
                "Roberts, M",
                "Subramanian, P",
                "Yorke, JA",
                "Salzberg, SL"
            ],
            "journal": "Genome biology",
            "pubdate": "2009/01/01 00:00"
        },
        "title": "A whole-genome assembly of the domestic cow, Bos taurus."
    }
]
