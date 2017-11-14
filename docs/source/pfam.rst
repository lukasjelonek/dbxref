.. highlight:: yaml

Pfam
====

Retrieve pfam xml documents for dbxrefs and convert them into json.

Options
-------

  * ``--basic`` - include id and description
  * ``--annotation`` - include id and annotation

Input
-----

example: ``PFAM:PF00002``


Output
------

output scheme::

  default output:

  [
      {
          "accession": "dbxref accession of the protein family",
          "comment": "comment to protein family",
          "description": "description of the protein family",
          "domain": "protein domain",
          "id": "dbxref of the protein family",
          "terms": [
              {
                  "description": "term description",
                  "id": "term dbxref"
              }
          ]
      }
  ]


  --basic output:

  [
      {
          "description": "description of the protein family",
          "id": "dbxref of the protein family"
      }
  ]


  --annotation output:

  [
      {
          "accession": "dbxref accession of the protein family",
          "comment": "comment to protein family",
          "domain": "protein domain",
          "id": "dbxref of the protein family",
          "terms": [
              {
                  "description": "term description",
                  "id": "term dbxref"
              }
          ]
      }
  ]

example output::

  [
      {
          "accession": "PF00002",
          "comment": "This family is known as Family B, the secretin-receptor family or family 2 of the G-protein-coupled receptors (GCPRs).They have been described in many animal species, but not in plants, fungi or prokaryotes. Three distinct sub-families are recognised. Subfamily B1 contains classical hormone receptors, such as receptors for secretin and glucagon, that are all involved in cAMP-mediated signalling pathways. Subfamily B2 contains receptors with long extracellular N-termini, such as the leukocyte cell-surface antigen CD97 (Swiss:P48960); calcium-independent receptors for latrotoxin (such as Swiss:O94910), and brain-specific angiogenesis inhibitors (such as Swiss:O14514) amongst others. Subfamily B3 includes Methuselah and other Drosophila proteins (e.g. Swiss:P83119). Other than the typical seven-transmembrane region, characteristic structural features include an amino-terminal extracellular domain involved in ligand binding, and an intracellular loop (IC3) required for specific G-protein coupling [1].",
          "description": "7 transmembrane receptor (Secretin family)",
          "domain": "7tm_2",
          "id": "PFAM:PF00002",
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

