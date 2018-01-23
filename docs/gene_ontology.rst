.. highlight:: yaml

Gene Ontology
=============

Retrieve gene ontology documents for dbxrefs and convert them into json.

Options
-------

  * ``--basic`` - include id, definition, name and synonyms
  * ``--relations`` - include id, parents and children

Input
-----

example: ``GO:0006915``


Output
------

output scheme::

  default output:

  [
      {
          "definition": "definition of the GO term",
          "id": "dbxref of the GO term",
          "name": "GO term name",
          "relations": {
              "children": [
                  {
                      "id": "child dbxref",
                      "type": "type of child"
                  }
              ],
              "parents": [
                  {
                      "id": "parent dbxref",
                      "type": "type of parent"
                  }
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
          "definition": "definition of the GO term",
          "id": "dbxref of the GO term",
          "name": "GO term name",
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
          "id": "dbxref of the GO term",
          "relations": {
              "children": [
                  {
                      "id": "child dbxref",
                      "type": "type of child"
                  }
              ],
              "parents": [
                  {
                      "id": "parent dbxref",
                      "type": "type of parent"
                  }
              ]
          }
      }
  ]


example output::

  [
      {
          "definition": "A programmed cell death process which begins when a cell receives an internal (e.g. DNA damage) or external signal (e.g. an extracellular death ligand), and proceeds through a series of biochemical events (signaling pathway phase) which trigger an execution phase. The execution phase is the last step of an apoptotic process, and is typically characterized by rounding-up of the cell, retraction of pseudopodes, reduction of cellular volume (pyknosis), chromatin condensation, nuclear fragmentation (karyorrhexis), plasma membrane blebbing and fragmentation of the cell into apoptotic bodies. When the execution phase is completed, the cell has died.",
          "id": "GO:0006915",
          "name": "apoptotic process",
          "relations": {
              "children": [
                  {
                      "id": "GO:0043066",
                      "type": "negatively_regulates"
                  },
                  {
                      "id": "GO:0016505",
                      "type": "part_of"
                  },
                  {
                      "id": "GO:1904606",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:0051402",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:1902110",
                      "type": "part_of"
                  },
                  {
                      "id": "GO:0097190",
                      "type": "part_of"
                  },
                  {
                      "id": "GO:0006925",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:0071887",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:0042981",
                      "type": "regulates"
                  },
                  {
                      "id": "GO:1902362",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:0097194",
                      "type": "part_of"
                  },
                  {
                      "id": "GO:0097153",
                      "type": "part_of"
                  },
                  {
                      "id": "GO:1904019",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:0033028",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:0034349",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:0010657",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:1902489",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:1902108",
                      "type": "part_of"
                  },
                  {
                      "id": "GO:1990009",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:0043065",
                      "type": "positively_regulates"
                  },
                  {
                      "id": "GO:1902109",
                      "type": "part_of"
                  },
                  {
                      "id": "GO:0097152",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:1902742",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:0071839",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:0043276",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:0043027",
                      "type": "part_of"
                  },
                  {
                      "id": "GO:0044346",
                      "type": "is_a"
                  },
                  {
                      "id": "GO:0008637",
                      "type": "part_of"
                  },
                  {
                      "id": "GO:1904516",
                      "type": "is_a"
                  }
              ],
              "parents": [
                  {
                      "id": "GO:0012501",
                      "type": "is_a"
                  }
              ]
          },
          "synonyms": [
              {
                  "name": "commitment to apoptosis",
                  "type": "related"
              },
              {
                  "name": "apoptosis",
                  "type": "narrow"
              },
              {
                  "name": "cell suicide",
                  "type": "broad"
              },
              {
                  "name": "cellular suicide",
                  "type": "broad"
              },
              {
                  "name": "apoptotic program",
                  "type": "narrow"
              },
              {
                  "name": "caspase-dependent programmed cell death",
                  "type": "related"
              },
              {
                  "name": "apoptosis signaling",
                  "type": "narrow"
              },
              {
                  "name": "induction of apoptosis by p53",
                  "type": "related"
              },
              {
                  "name": "apoptosis activator activity",
                  "type": "related"
              },
              {
                  "name": "activation of apoptosis",
                  "type": "narrow"
              },
              {
                  "name": "apoptotic cell death",
                  "type": "exact"
              },
              {
                  "name": "induction of apoptosis",
                  "type": "related"
              },
              {
                  "name": "type I programmed cell death",
                  "type": "narrow"
              },
              {
                  "name": "signaling (initiator) caspase activity",
                  "type": "related"
              },
              {
                  "name": "programmed cell death by apoptosis",
                  "type": "exact"
              },
              {
                  "name": "apoptotic programmed cell death",
                  "type": "exact"
              }
          ]
      }
  ]
