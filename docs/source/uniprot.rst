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

example: ``UniProtKB/Swiss-Prot:Q5XI95``

Output
------

output scheme::

  default output:

  [
      {
          "accessions": [
              "list of accession numbers"
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
                  "description": "description of feature",
                  "position": "position of feature",
                  "type": "type of feature"
              }
              or
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
              "list of accession numbers"
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
                  "description": "description of feature",
                  "position": "position of feature",
                  "type": "type of feature"
              }
              or
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
              "Q5XI95"
          ],
          "alternative_names": [],
          "dbxrefs": [
              "EC:1.1.1.1",
              "EMBL:BC083792",
              "RefSeq:NP_001012084.1",
              "UniGene:Rn.214994",
              "ProteinModelPortal:Q5XI95",
              "SMR:Q5XI95",
              "STRING:10116.ENSRNOP00000030638",
              "PhosphoSitePlus:Q5XI95",
              "PaxDb:Q5XI95",
              "PRIDE:Q5XI95",
              "Ensembl:ENSRNOT00000036993",
              "GeneID:310903",
              "KEGG:rno:310903",
              "CTD:130",
              "RGD:1306313",
              "eggNOG:KOG0022",
              "eggNOG:COG1062",
              "GeneTree:ENSGT00430000030800",
              "HOGENOM:HOG000294674",
              "HOVERGEN:HBG000195",
              "InParanoid:Q5XI95",
              "KO:K13952",
              "PhylomeDB:Q5XI95",
              "TreeFam:TF300429",
              "Reactome:R-RNO-2161541",
              "Reactome:R-RNO-5365859",
              "Reactome:R-RNO-71384",
              "PRO:PR:Q5XI95",
              "Proteomes:UP000002494",
              "Bgee:ENSRNOG00000012436",
              "ExpressionAtlas:Q5XI95",
              "GO:0005737",
              "GO:0004022",
              "GO:0008270",
              "InterPro:IPR013149",
              "InterPro:IPR013154",
              "InterPro:IPR002328",
              "InterPro:IPR011032",
              "InterPro:IPR036291",
              "InterPro:IPR020843",
              "Pfam:PF08240",
              "Pfam:PF00107",
              "SMART:SM00829",
              "SUPFAM:SSF50129",
              "SUPFAM:SSF51735",
              "PROSITE:PS00059"
          ],
          "description": "Alcohol dehydrogenase 6",
          "features": [
              {
                  "begin": "1",
                  "description": "Alcohol dehydrogenase 6",
                  "end": "376",
                  "type": "chain"
              },
              {
                  "begin": "200",
                  "description": "NAD",
                  "end": "205",
                  "type": "nucleotide phosphate-binding region"
              },
              {
                  "begin": "293",
                  "description": "NAD",
                  "end": "295",
                  "type": "nucleotide phosphate-binding region"
              },
              {
                  "description": "Zinc 1; catalytic",
                  "position": "47",
                  "type": "metal ion-binding site"
              },
              {
                  "description": "Zinc 1; catalytic",
                  "position": "69",
                  "type": "metal ion-binding site"
              },
              {
                  "description": "Zinc 2",
                  "position": "99",
                  "type": "metal ion-binding site"
              },
              {
                  "description": "Zinc 2",
                  "position": "102",
                  "type": "metal ion-binding site"
              },
              {
                  "description": "Zinc 2",
                  "position": "105",
                  "type": "metal ion-binding site"
              },
              {
                  "description": "Zinc 2",
                  "position": "113",
                  "type": "metal ion-binding site"
              },
              {
                  "description": "Zinc 1; catalytic",
                  "position": "175",
                  "type": "metal ion-binding site"
              },
              {
                  "description": "NAD",
                  "position": "224",
                  "type": "binding site"
              },
              {
                  "description": "NAD",
                  "position": "229",
                  "type": "binding site"
              },
              {
                  "description": "NAD",
                  "position": "371",
                  "type": "binding site"
              }
          ],
          "id": "UniProtKB/Swiss-Prot:Q5XI95",
          "keywords": [
              "Complete proteome",
              "Cytoplasm",
              "Metal-binding",
              "NAD",
              "Oxidoreductase",
              "Reference proteome",
              "Zinc"
          ],
          "organism": "Taxon:10116",
          "recommended_name": {
              "full": "Alcohol dehydrogenase 6"
          },
          "sequence": "MGTQGKVIRCKATVLWKPGAPLAIEEIEVAPPKAKEVRIKMVATGVCGTDIKHLDTQELSKFCPMIMGHEGVGIVESVGEGVSSVRTGDKVILLCIPQCGECKTCLNSKNNICTEIRLSKTHLASEGTSRITCKGKLVHQYIALGSFSEYTVLKEISVAKIDEGAPLEKVCIIGCGFATGYGAAINSAKVTPGSTCAVFGLGGVGLSVIIGCKAAGAARIIAVDINKDRFAKAKTVGATDCVDPRDFEKPIEEVLSDMIDGGVDFCFEVTGNTEAVGAALGSCHKDHGVCVTVGALASFTSTLSIRSHLFFSGRILKGSILGGWKTKEEIPKLVSDYMAKKFNIDPLITHTLTLSEANEAVQLMKSGQCIRCVLLL"
      }
  ]
