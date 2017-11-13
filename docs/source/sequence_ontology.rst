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

  "definition": ""
  "id":		""
  "name":	""
  "namespace":	""
  "relations":	{"children": ["", ...], "parents": ["", ...]}
  "synonyms":	[{"name": "", "type": ""}, ...]


  --basic output:

  "definition": ""
  "id":		""
  "name":	""
  "namespace":	""
  "synonyms":	[{"name": "", "type": ""}, ...]


  --references output:

  "id":		""
  "relations":	{"children": ["", ...], "parents": ["", ...]}

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
