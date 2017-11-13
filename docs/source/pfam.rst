.. highlight:: yaml

Pfam
====

Retrieve pfam xml documents for dbxrefs and convert them into json.

Options
-------

  * ``--basic`` - include dbxref and description
  * ``--annotation`` - include dbxref and annotation

Input
-----

example: ``PFAM:PF00002``


Output
------

output scheme::

  default output:

  "acession":		""
  "comment":		""
  "dbxref":		""
  "description":	""
  "id":			""
  "terms":		[{"description": "", "id": ""}, ...]


  --basic output:

  "dbxref":		""
  "description":	""


  --annotation output:

  "acession":		""
  "comment":		""
  "dbxref":		""
  "id":			""
  "terms":		[{"description": "", "id": ""}, ...]

example output::

  [
      {
          "accession": "PF00002",
          "comment": "This family is known as Family B, the secretin-receptor family or family 2 of the G-protein-coupled receptors (GCPRs).They have been described in many animal species, but not in plants, fungi or prokaryotes. Three distinct sub-families are recognised. Subfamily B1 contains classical hormone receptors, such as receptors for secretin and glucagon, that are all involved in cAMP-mediated signalling pathways. Subfamily B2 contains receptors with long extracellular N-termini, such as the leukocyte cell-surface antigen CD97 (Swiss:P48960); calcium-independent receptors for latrotoxin (such as Swiss:O94910), and brain-specific angiogenesis inhibitors (such as Swiss:O14514) amongst others. Subfamily B3 includes Methuselah and other Drosophila proteins (e.g. Swiss:P83119). Other than the typical seven-transmembrane region, characteristic structural features include an amino-terminal extracellular domain involved in ligand binding, and an intracellular loop (IC3) required for specific G-protein coupling [1].",
          "dbxref": "PFAM:PF00002",
          "description": "7 transmembrane receptor (Secretin family)",
          "id": "7tm_2",
          "terms": [
              {
                  "description": "integral component of membrane",
                  "id": "GO:0016021"
              },
              {
                  "description": "G-protein coupled receptor activity",
                  "id": "GO:0004930"
              },
              {
                  "description": "G-protein coupled receptor signaling pathway",
                  "id": "GO:0007186"
              }
          ]
      }
  ]

