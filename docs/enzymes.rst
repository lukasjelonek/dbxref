.. highlight:: yaml

Enzyme
======

Retrieve enzyme text documents for dbxrefs and convert them into json.

Options
-------

  * ``--basic`` - include id, definition, name and synonyms
  * ``--references`` - include id and uniprot dbxrefs

Input
-----

example: ``EC:1.1.1.1``


Output
------

output scheme::

  default output:

  [
      {
          "dbxrefs": [
              "list of dbxrefs"
          ]
          "deifinition": {
              "cofactors": [
                  "list of cofactors"
              ],
              "comments": [
                  "list of comments"
              ],
              "reaction_catalyzed": [
                  "list of catalyzed reactions"
              ]
          },
          "id": "dbxref of enzyme",
          "name": "enzyme name",
          "synonyms": [
              "list of synonyms"
          ]
      }
  ]


  --basic output:

  [
      {
          "deifinition": {
              "cofactors": [
                  "list of cofactors"
              ],
              "comments": [
                  "list of comments"
              ],
              "reaction_catalyzed": [
                  "list of catalyzed reactions"
              ]
          },
          "id": "dbxref of enzyme",
          "name": "enzyme name",
          "synonyms": [
              "list of synonyms"
          ]
      }
  ]


  --references output:

  [
      {
          "dbxrefs": [
              "list of dbxrefs"
          ]
          "id": "dbxref of enzyme"
      }
  ]


example output::

  [
      {
          "dbxrefs": [
              "UniProtKB/Swiss-Prot:P07327",
              "UniProtKB/Swiss-Prot:P28469",
              "UniProtKB/Swiss-Prot:Q5RBP7",
              "UniProtKB/Swiss-Prot:P25405",
              "UniProtKB/Swiss-Prot:P00325",
              "UniProtKB/Swiss-Prot:Q5R1W2",
              "UniProtKB/Swiss-Prot:P14139",
              "UniProtKB/Swiss-Prot:P25406",
              "UniProtKB/Swiss-Prot:P00327",
              "UniProtKB/Swiss-Prot:P00326",
              "UniProtKB/Swiss-Prot:O97959",
              "UniProtKB/Swiss-Prot:P00328",
              "UniProtKB/Swiss-Prot:P80222",
              "UniProtKB/Swiss-Prot:P30350",
              "UniProtKB/Swiss-Prot:P49645",
              "UniProtKB/Swiss-Prot:P06525",
              "UniProtKB/Swiss-Prot:P41747",
              "UniProtKB/Swiss-Prot:Q17334",
              "UniProtKB/Swiss-Prot:P43067",
              "UniProtKB/Swiss-Prot:P85440",
              "UniProtKB/Swiss-Prot:P48814",
              "UniProtKB/Swiss-Prot:Q70UN9",
              "UniProtKB/Swiss-Prot:P23991",
              "UniProtKB/Swiss-Prot:P86883",
              "UniProtKB/Swiss-Prot:P19631",
              "UniProtKB/Swiss-Prot:P23236",
              "UniProtKB/Swiss-Prot:P48586",
              "UniProtKB/Swiss-Prot:P09370",
              "UniProtKB/Swiss-Prot:P22246",
              "UniProtKB/Swiss-Prot:P07161",
              "UniProtKB/Swiss-Prot:P12854",
              "UniProtKB/Swiss-Prot:P08843",
              "UniProtKB/Swiss-Prot:P26325",
              "UniProtKB/Swiss-Prot:Q9Z2M2",
              "UniProtKB/Swiss-Prot:Q64413",
              "UniProtKB/Swiss-Prot:Q64415",
              "UniProtKB/Swiss-Prot:P12311",
              "UniProtKB/Swiss-Prot:P05336",
              "UniProtKB/Swiss-Prot:P20369",
              "UniProtKB/Swiss-Prot:Q07288",
              "UniProtKB/Swiss-Prot:P00333",
              "UniProtKB/Swiss-Prot:P86885",
              "UniProtKB/Swiss-Prot:P00329",
              "UniProtKB/Swiss-Prot:P80512",
              "UniProtKB/Swiss-Prot:Q9P6C8",
              "UniProtKB/Swiss-Prot:Q75ZX4",
              "UniProtKB/Swiss-Prot:Q2R8Z5",
              "UniProtKB/Swiss-Prot:P12886",
              "UniProtKB/Swiss-Prot:P22797",
              "UniProtKB/Swiss-Prot:P14219",
              "UniProtKB/Swiss-Prot:P41680",
              "UniProtKB/Swiss-Prot:P25141",
              "UniProtKB/Swiss-Prot:O00097",
              "UniProtKB/Swiss-Prot:Q03505",
              "UniProtKB/Swiss-Prot:P06757",
              "UniProtKB/Swiss-Prot:P14673",
              "UniProtKB/Swiss-Prot:P80338",
              "UniProtKB/Swiss-Prot:P13603",
              "UniProtKB/Swiss-Prot:P00330",
              "UniProtKB/Swiss-Prot:Q07264",
              "UniProtKB/Swiss-Prot:P20368",
              "UniProtKB/Swiss-Prot:O45687",
              "UniProtKB/Swiss-Prot:O94038",
              "UniProtKB/Swiss-Prot:P48815",
              "UniProtKB/Swiss-Prot:Q70UP5",
              "UniProtKB/Swiss-Prot:Q70UP6",
              "UniProtKB/Swiss-Prot:P27581",
              "UniProtKB/Swiss-Prot:P25720",
              "UniProtKB/Swiss-Prot:P23237",
              "UniProtKB/Swiss-Prot:P48587",
              "UniProtKB/Swiss-Prot:P09369",
              "UniProtKB/Swiss-Prot:P07160",
              "UniProtKB/Swiss-Prot:P24267",
              "UniProtKB/Swiss-Prot:P37686",
              "UniProtKB/Swiss-Prot:P54202",
              "UniProtKB/Swiss-Prot:Q24803",
              "UniProtKB/Swiss-Prot:P42327",
              "UniProtKB/Swiss-Prot:P10847",
              "UniProtKB/Swiss-Prot:P49383",
              "UniProtKB/Swiss-Prot:Q9P4C2",
              "UniProtKB/Swiss-Prot:P04707",
              "UniProtKB/Swiss-Prot:Q4R1E8",
              "UniProtKB/Swiss-Prot:Q0ITW7",
              "UniProtKB/Swiss-Prot:O13309",
              "UniProtKB/Swiss-Prot:P28032",
              "UniProtKB/Swiss-Prot:P14674",
              "UniProtKB/Swiss-Prot:F2Z678",
              "UniProtKB/Swiss-Prot:P00331",
              "UniProtKB/Swiss-Prot:F8DVL8",
              "UniProtKB/Swiss-Prot:P0DJA2",
              "UniProtKB/Swiss-Prot:P07754",
              "UniProtKB/Swiss-Prot:P42328",
              "UniProtKB/Swiss-Prot:P10848",
              "UniProtKB/Swiss-Prot:P49384",
              "UniProtKB/Swiss-Prot:P14675",
              "UniProtKB/Swiss-Prot:P07246",
              "UniProtKB/Swiss-Prot:P08319",
              "UniProtKB/Swiss-Prot:P49385",
              "UniProtKB/Swiss-Prot:Q9QYY9",
              "UniProtKB/Swiss-Prot:Q64563",
              "UniProtKB/Swiss-Prot:Q09669",
              "UniProtKB/Swiss-Prot:P80468",
              "UniProtKB/Swiss-Prot:A6ZTT5",
              "UniProtKB/Swiss-Prot:P10127",
              "UniProtKB/Swiss-Prot:Q6XQ67",
              "UniProtKB/Swiss-Prot:P38113",
              "UniProtKB/Swiss-Prot:P28332",
              "UniProtKB/Swiss-Prot:P41681",
              "UniProtKB/Swiss-Prot:Q5R7Z8",
              "UniProtKB/Swiss-Prot:Q5XI95",
              "UniProtKB/Swiss-Prot:P40394",
              "UniProtKB/Swiss-Prot:Q64437",
              "UniProtKB/Swiss-Prot:P41682",
              "UniProtKB/Swiss-Prot:P9WQC0",
              "UniProtKB/Swiss-Prot:P9WQC1",
              "UniProtKB/Swiss-Prot:O31186",
              "UniProtKB/Swiss-Prot:Q7U1B9",
              "UniProtKB/Swiss-Prot:P9WQC6",
              "UniProtKB/Swiss-Prot:P9WQC7",
              "UniProtKB/Swiss-Prot:P9WQB8",
              "UniProtKB/Swiss-Prot:P9WQB9",
              "UniProtKB/Swiss-Prot:P33744",
              "UniProtKB/Swiss-Prot:P0A9Q8",
              "UniProtKB/Swiss-Prot:P0A9Q7",
              "UniProtKB/Swiss-Prot:P81600",
              "UniProtKB/Swiss-Prot:P72324",
              "UniProtKB/Swiss-Prot:Q9SK86",
              "UniProtKB/Swiss-Prot:Q9SK87",
              "UniProtKB/Swiss-Prot:A1L4Y2",
              "UniProtKB/Swiss-Prot:Q8VZ49",
              "UniProtKB/Swiss-Prot:Q0V7W6",
              "UniProtKB/Swiss-Prot:Q8LEB2",
              "UniProtKB/Swiss-Prot:Q9FH04",
              "UniProtKB/Swiss-Prot:P81601",
              "UniProtKB/Swiss-Prot:P39451",
              "UniProtKB/Swiss-Prot:O46649",
              "UniProtKB/Swiss-Prot:O46650",
              "UniProtKB/Swiss-Prot:Q96533",
              "UniProtKB/Swiss-Prot:Q3ZC42",
              "UniProtKB/Swiss-Prot:Q17335",
              "UniProtKB/Swiss-Prot:Q54TC2",
              "UniProtKB/Swiss-Prot:P46415",
              "UniProtKB/Swiss-Prot:P19854",
              "UniProtKB/Swiss-Prot:P11766",
              "UniProtKB/Swiss-Prot:P93629",
              "UniProtKB/Swiss-Prot:P28474",
              "UniProtKB/Swiss-Prot:P80360",
              "UniProtKB/Swiss-Prot:P81431",
              "UniProtKB/Swiss-Prot:A2XAZ3",
              "UniProtKB/Swiss-Prot:Q0DWH1",
              "UniProtKB/Swiss-Prot:P80572",
              "UniProtKB/Swiss-Prot:O19053",
              "UniProtKB/Swiss-Prot:P12711",
              "UniProtKB/Swiss-Prot:P80467",
              "UniProtKB/Swiss-Prot:P86884",
              "UniProtKB/Swiss-Prot:P79896",
              "UniProtKB/Swiss-Prot:Q9NAR7",
              "UniProtKB/Swiss-Prot:P14940",
              "UniProtKB/Swiss-Prot:Q0KDL6",
              "UniProtKB/Swiss-Prot:Q00669",
              "UniProtKB/Swiss-Prot:P21518",
              "UniProtKB/Swiss-Prot:P25139",
              "UniProtKB/Swiss-Prot:Q50L96",
              "UniProtKB/Swiss-Prot:P48584",
              "UniProtKB/Swiss-Prot:P22245",
              "UniProtKB/Swiss-Prot:Q9NG42",
              "UniProtKB/Swiss-Prot:P28483",
              "UniProtKB/Swiss-Prot:P48585",
              "UniProtKB/Swiss-Prot:P51551",
              "UniProtKB/Swiss-Prot:Q09009",
              "UniProtKB/Swiss-Prot:P51549",
              "UniProtKB/Swiss-Prot:P21898",
              "UniProtKB/Swiss-Prot:Q07588",
              "UniProtKB/Swiss-Prot:Q9NG40",
              "UniProtKB/Swiss-Prot:Q27404",
              "UniProtKB/Swiss-Prot:P10807",
              "UniProtKB/Swiss-Prot:P07162",
              "UniProtKB/Swiss-Prot:Q09010",
              "UniProtKB/Swiss-Prot:P00334",
              "UniProtKB/Swiss-Prot:Q00671",
              "UniProtKB/Swiss-Prot:P25721",
              "UniProtKB/Swiss-Prot:Q00672",
              "UniProtKB/Swiss-Prot:P07159",
              "UniProtKB/Swiss-Prot:P84328",
              "UniProtKB/Swiss-Prot:P37473",
              "UniProtKB/Swiss-Prot:P23361",
              "UniProtKB/Swiss-Prot:P23277",
              "UniProtKB/Swiss-Prot:Q6LCE4",
              "UniProtKB/Swiss-Prot:Q9U8S9",
              "UniProtKB/Swiss-Prot:Q9GN94",
              "UniProtKB/Swiss-Prot:Q24641",
              "UniProtKB/Swiss-Prot:P23278",
              "UniProtKB/Swiss-Prot:Q03384",
              "UniProtKB/Swiss-Prot:P28484",
              "UniProtKB/Swiss-Prot:P51550",
              "UniProtKB/Swiss-Prot:B4M8Y0",
              "UniProtKB/Swiss-Prot:Q05114",
              "UniProtKB/Swiss-Prot:P26719",
              "UniProtKB/Swiss-Prot:P17648",
              "UniProtKB/Swiss-Prot:P48977",
              "UniProtKB/Swiss-Prot:P81786",
              "UniProtKB/Swiss-Prot:P9WQC2",
              "UniProtKB/Swiss-Prot:P9WQC3",
              "UniProtKB/Swiss-Prot:P25988",
              "UniProtKB/Swiss-Prot:Q00670",
              "UniProtKB/Swiss-Prot:P00332",
              "UniProtKB/Swiss-Prot:Q2FJ31",
              "UniProtKB/Swiss-Prot:Q2G0G1",
              "UniProtKB/Swiss-Prot:Q2YSX0",
              "UniProtKB/Swiss-Prot:Q5HI63",
              "UniProtKB/Swiss-Prot:Q99W07",
              "UniProtKB/Swiss-Prot:Q7A742",
              "UniProtKB/Swiss-Prot:Q6GJ63",
              "UniProtKB/Swiss-Prot:Q6GBM4",
              "UniProtKB/Swiss-Prot:Q8NXU1",
              "UniProtKB/Swiss-Prot:Q5HRD6",
              "UniProtKB/Swiss-Prot:Q8CQ56",
              "UniProtKB/Swiss-Prot:Q4J781",
              "UniProtKB/Swiss-Prot:P39462",
              "UniProtKB/Swiss-Prot:P50381",
              "UniProtKB/Swiss-Prot:Q96XE0",
              "UniProtKB/Swiss-Prot:P51552",
              "UniProtKB/Swiss-Prot:Q5AR48",
              "UniProtKB/Swiss-Prot:A5JYX5",
              "UniProtKB/Swiss-Prot:P32771",
              "UniProtKB/Swiss-Prot:A7ZIA4",
              "UniProtKB/Swiss-Prot:Q8X5J4",
              "UniProtKB/Swiss-Prot:A7ZX04",
              "UniProtKB/Swiss-Prot:A1A835",
              "UniProtKB/Swiss-Prot:Q0TKS7",
              "UniProtKB/Swiss-Prot:Q8FKG1",
              "UniProtKB/Swiss-Prot:B1J085",
              "UniProtKB/Swiss-Prot:P25437",
              "UniProtKB/Swiss-Prot:B1LIP1",
              "UniProtKB/Swiss-Prot:Q1RFI7",
              "UniProtKB/Swiss-Prot:P44557",
              "UniProtKB/Swiss-Prot:P39450",
              "UniProtKB/Swiss-Prot:Q3Z550",
              "UniProtKB/Swiss-Prot:P73138",
              "UniProtKB/Swiss-Prot:P71017",
              "UniProtKB/Swiss-Prot:N4WE73",
              "UniProtKB/Swiss-Prot:A1CFL1",
              "UniProtKB/Swiss-Prot:N4WE43",
              "UniProtKB/Swiss-Prot:N4WW42",
              "UniProtKB/Swiss-Prot:P33010",
              "UniProtKB/Swiss-Prot:O07737"
          ]
          "deifinition": {
              "cofactors": [
                  "Zn(2+) or Fe cation."
              ],
              "comments": [
                  "Acts on primary or secondary alcohols or hemi-acetals with very broad specificity; however the enzyme oxidizes methanol much more poorly than ethanol.",
                  "The animal, but not the yeast, enzyme acts also on cyclic secondary alcohols."
              ],
              "reaction_catalyzed": [
                  "An alcohol + NAD(+) = an aldehyde or ketone + NADH.",
                  "A secondary alcohol + NAD(+) = a ketone + NADH."
              ]
          },
          "id": "EC:1.1.1.1",
          "name": "Alcohol dehydrogenase.",
          "synonyms": [
              "Aldehyde reductase."
          ]
      }
  ]
