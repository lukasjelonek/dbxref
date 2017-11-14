.. highlight:: yaml

Sequence Ontology
=================

Retrieve sequence ontology csv documents for dbxrefs and convert them into json.

Options
-------

  * ``--basic`` - include id, definition, name and synonyms
  * ``--relations`` - include id, parents and children

Input
-----

example: ``SO:0000715``


Output
------

output scheme::

  default output:

  [
      {
          "definition": "definition of the SO term",
          "id": "dbxref of the SO term",
          "name": "SO term name",
          "namespace": "namespace of the SO term",
          "relations": {
              "children": [
                  "child dbxref"
              ],
              "parents": [
                  "parent dbxref"
              ]
          },
          "synonyms": [
              {
                  "name": "synonym name",
                  "type": "type of synonym"
              }
          ]
      }
  ]


  --basic output:

  [
      {
          "definition": "definition of the SO term",
          "id": "dbxref of the SO term",
          "name": "SO term name",
          "namespace": "namespace of the SO term",
          "synonyms": [
              {
                  "name": "synonym name",
                  "type": "type of synonym"
              }
          ]
      }
  ]


  --relations output:

  [
      {
          "id": "dbxref of the SO term",
          "relations": {
              "children": [
                  "child dbxref"
              ],
              "parents": [
                  "parent dbxref"
              ]
          }
      }
  ]

example output::

  [
      {
          "definition": "A motif that is active in RNA sequence.",
          "id": "SO:0000715",
          "name": "RNA motif",
          "namespace": "sequence",
          "relations": {
              "children": [
                  "SO:0000022",
                  "SO:0000380",
                  "SO:0000026",
                  "SO:0000020",
                  "SO:0001979"
              ],
              "parents": [
                  "SO:0000714"
              ]
          },
          "synonyms": [
              {
                  "name": "RNA motif",
                  "type": "exact"
              }
          ]
      }
  ]
