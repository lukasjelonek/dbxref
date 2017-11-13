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
  * ``--features`` - include id and features (NOT IMPLEMENTED YET)

Input
-----

example: ``UniProtKB/Swiss-Prot:Q01219``

Output
------

output scheme::

  default output:

  "acessions":		["", ...]
  "alternative_names":	["", ...]
  "dbxrefs":		["", ...]
  "description":	""
  "id":			""
  "keywords":		["", ...]
  "organism":		""
  "recommended_names":	{"full": ""}
  "sequence":		""


  --basic output:

  "description":	""
  "id":			""


  --sequence output:

  "id":			""
  "sequence":		""


  --organism output:

  "id":			""
  "organism":		""


  --annotation output:

  "acessions":		["", ...]
  "alternative_names":	["", ...]
  "dbxrefs":		["", ...]
  "id":			""
  "keywords":		["", ...]
  "recommended_names":	{"full": ""}


  --features output:

  "id":			""

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
