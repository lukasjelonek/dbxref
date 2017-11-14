.. highlight:: yaml

Uniprot
=======

Retrieve uniprot xml documents for dbxrefs and convert them into json.

Options
-------

  * ``--basic`` - include id and description
  * ``--sequence`` - include id and sequence
  * ``--organism`` - include id and organism info
  * ``--annotation`` - include id and annotation
  * ``--features`` - include id and features

Input
-----

example: ``UniProtKB/Swiss-Prot:Q01219``

Output
------

output scheme::

  default output:

  [
      {
          "accessions": [
              "list of accessions"
          ],
          "alternative_names": [
              "list of alternative names"
          ],
          "dbxrefs": [
              "list of dbxrefs"
          ],
          "description": "protein description",
          "features": [
              {
                  "begin": "start position of feature",
                  "description": "description of feature",
                  "end": "end position of feature",
                  "type": "type of feature"
              }
          ],
          "id": "dbxref of protein",
          "keywords": [
              "list of keywords"
          ],
          "organism": "taxon dbxref",
          "recommended_name": {
              "full": "recommended name for protein"
          },
          "sequence": "amino acid sequence of protein"
      }
  ]


  --basic output:

  [
      {
          "description": "protein description",
          "id": "dbxref of protein"
      }
  ]
  "description":	""
  "id":			""


  --sequence output:

  [
      {
          "id": "dbxref of protein",
          "sequence": "amino acid sequence of protein"
      }
  ]


  --organism output:

  [
      {
          "id": "dbxref of protein",
          "organism": "taxon dbxref"
      }
  ]


  --annotation output:

  [
      {
          "accessions": [
              "list of accessions"
          ],
          "alternative_names": [
              "list of alternative names"
          ],
          "dbxrefs": [
              "list of dbxrefs"
          ],
          "id": "dbxref of protein",
          "keywords": [
              "list of keywords"
          ],
          "recommended_name": {
              "full": "recommended name for protein"
          }
      }
  ]


  --features output:

  [
      {
          "features": [
              {
                  "begin": "start position of feature",
                  "description": "description of feature",
                  "end": "end position of feature",
                  "type": "type of feature"
              }
          ],
          "id": "dbxref of protein"
      }
  ]

example output::

  [
      {
          "accessions": [
              "Q01219",
              "Q76ZM7"
          ],
          "alternative_names": [],
          "dbxrefs": [
              "EMBL:D11079",
              "EMBL:AY243312",
              "PIR:JQ1789",
              "RefSeq:YP_233059.1",
              "DIP:DIP-2178N",
              "IntAct:Q01219",
              "MINT:MINT-130825",
              "GeneID:3707706",
              "KEGG:vg:3707706",
              "OrthoDB:VOG090000DH",
              "Proteomes:UP000000344",
              "InterPro:IPR007032",
              "Pfam:PF04948"
          ],
          "description": "Protein A51",
          "features": [
              {
                  "begin": "1",
                  "description": "Protein A51",
                  "end": "334",
                  "type": "chain"
              },
              {
                  "begin": "89",
                  "description": "Poly-Asp",
                  "end": "92",
                  "type": "compositionally biased region"
              }
          ],
          "id": "UniProtKB/Swiss-Prot:Q01219",
          "keywords": [
              "Complete proteome",
              "Reference proteome"
          ],
          "organism": "Taxon:10254",
          "recommended_name": {
              "full": "Protein A51"
          },
          "sequence": "MDGVIVYCLNALVKHGEEINHIKNDFMIKPCCERVCEKVKNVHIGGQSKNNTVIADLPYMDNAVSDVCNSLYKKNVSRISRFANLIKIDDDDKTPTGVYNYFKPKDVIPVIISIGKDKDVCELLISSDISCACVELNSYHVAILPMDVSFFTKGNASLIILLFDFSIDAAPLLRSVTDNNVIISRHQRLHDELPSSNWFKFYISIKSDYCSILYMVVDGSVMHAIADNRTHAIISKNILDNTTINDECRCCYFEPQIRILDRDEMLNGSSCDMNRHCIMMNLPDVGKFGSSMLGKYEPDMIKIALSVAGNLIRNRDYIPGRRGYSYYVYGIASR"
      }
  ]
