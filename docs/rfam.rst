.. highlight:: yaml

Rfam
====

Retrieve rfam json documents for dbxrefs and convert them into dbxref format json.

Options
-------

  * ``--basics`` - Include basic informations such as dbxref_id, name, description and comment.
  * ``--references`` - Include reference information.

Input
-----

example: ``RFAM:RF03094``


Output
------

output scheme::

[
    {
        "comment": "Halobacteria (Archaea). Nearby to self-splicing intron genes",
        "dbxref": "RF03094",
        "description": "LAGLIDADG-2 RNA",
        "name": "LAGLIDADG-2",
        "references": {
            "DOI": "Published; PMID:28977401;",
            "author": "Weinberg Z",
            "type": "Gene; sRNA;"
        }
    }
]
