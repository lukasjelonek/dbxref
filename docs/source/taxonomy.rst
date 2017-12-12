.. highlight:: yaml

Taxonomy
=============

Retrieve gene ontology documents for dbxrefs and convert them into json.

Options
-------

  * ``--basic`` - include id, scientificName, commonName, lineage and rank
  * ``--geneticCodes`` - include id, geneticCode and mitochondrialGeneticCode

Input
-----

example: ``Taxon:7227``


Output
------

output scheme::

  default output:

  [
      {
          "commonName": "common name of the Taxon",
          "geneticCodes": {
              "geneticCode": "genetic code of the Taxon",
              "mitochondrialGeneticCode": "mitochondrial genetic code of the Taxon"
          },
          "id": "dbxref of the Taxon",
          "lineage": "lineage of the Taxon",
          "rank": "rank of the Taxon",
          "scientificName": "scientific name of the Taxon"
      }
  ]


  --basic output:

  [
      {
          "commonName": "common name of the Taxon",
          "id": "dbxref of the Taxon",
          "lineage": "lineage of the Taxon",
          "rank": "rank of the Taxon",
          "scientificName": "scientific name of the Taxon"
      }
  ]


  --geneticCodes output:

  [
      {
          "geneticCodes": {
              "geneticCode": "genetic code of the Taxon",
              "mitochondrialGeneticCode": "mitochondrial genetic code of the Taxon"
          },
          "id": "dbxref of the Taxon"
      }
  ]


example output::

  [
      {
          "commonName" : "fruit fly",
          "geneticCodes" : {
              "geneticCode" : "1",
              "mitochondrialGeneticCode" : "5"
          },
          "id" : "Taxon:7227",
          "lineage" : "Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota; Neoptera; Holometabola; Diptera; Brachycera; Muscomorpha; Ephydroidea; Drosophilidae; Drosophila; Sophophora; ",
          "rank" : "species",
          "scientificName" : "Drosophila melanogaster"
      }
  ]

