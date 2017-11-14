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
              "P07327",
              "P28469",
              "Q5RBP7",
              "P25405",
              "P00325",
              "Q5R1W2",
              "P14139",
              "P25406",
              "P00327",
              "P00326",
              "O97959",
              "P00328",
              "P80222",
              "P30350",
              "P49645",
              "P06525",
              "P41747",
              "Q17334",
              "P43067",
              "P85440",
              "P48814",
              "Q70UN9",
              "P23991",
              "P86883",
              "P19631",
              "P23236",
              "P48586",
              "P09370",
              "P22246",
              "P07161",
              "P12854",
              "P08843",
              "P26325",
              "Q9Z2M2",
              "Q64413",
              "Q64415",
              "P12311",
              "P05336",
              "P20369",
              "Q07288",
              "P00333",
              "P86885",
              "P00329",
              "P80512",
              "Q9P6C8",
              "Q75ZX4",
              "Q2R8Z5",
              "P12886",
              "P22797",
              "P14219",
              "P41680",
              "P25141",
              "O00097",
              "Q03505",
              "P06757",
              "P14673",
              "P80338",
              "P13603",
              "P00330",
              "Q07264",
              "P20368",
              "O45687",
              "O94038",
              "P48815",
              "Q70UP5",
              "Q70UP6",
              "P27581",
              "P25720",
              "P23237",
              "P48587",
              "P09369",
              "P07160",
              "P24267",
              "P37686",
              "P54202",
              "Q24803",
              "P42327",
              "P10847",
              "P49383",
              "Q9P4C2",
              "P04707",
              "Q4R1E8",
              "Q0ITW7",
              "O13309",
              "P28032",
              "P14674",
              "F2Z678",
              "P00331",
              "F8DVL8",
              "P0DJA2",
              "P07754",
              "P42328",
              "P10848",
              "P49384",
              "P14675",
              "P07246",
              "P08319",
              "P49385",
              "Q9QYY9",
              "Q64563",
              "Q09669",
              "P80468",
              "A6ZTT5",
              "P10127",
              "Q6XQ67",
              "P38113",
              "P28332",
              "P41681",
              "Q5R7Z8",
              "Q5XI95",
              "P40394",
              "Q64437",
              "P41682",
              "P9WQC0",
              "P9WQC1",
              "O31186",
              "Q7U1B9",
              "P9WQC6",
              "P9WQC7",
              "P9WQB8",
              "P9WQB9",
              "P33744",
              "P0A9Q8",
              "P0A9Q7",
              "P81600",
              "P72324",
              "Q9SK86",
              "Q9SK87",
              "A1L4Y2",
              "Q8VZ49",
              "Q0V7W6",
              "Q8LEB2",
              "Q9FH04",
              "P81601",
              "P39451",
              "O46649",
              "O46650",
              "Q96533",
              "Q3ZC42",
              "Q17335",
              "Q54TC2",
              "P46415",
              "P19854",
              "P11766",
              "P93629",
              "P28474",
              "P80360",
              "P81431",
              "A2XAZ3",
              "Q0DWH1",
              "P80572",
              "O19053",
              "P12711",
              "P80467",
              "P86884",
              "P79896",
              "Q9NAR7",
              "P14940",
              "Q0KDL6",
              "Q00669",
              "P21518",
              "P25139",
              "Q50L96",
              "P48584",
              "P22245",
              "Q9NG42",
              "P28483",
              "P48585",
              "P51551",
              "Q09009",
              "P51549",
              "P21898",
              "Q07588",
              "Q9NG40",
              "Q27404",
              "P10807",
              "P07162",
              "Q09010",
              "P00334",
              "Q00671",
              "P25721",
              "Q00672",
              "P07159",
              "P84328",
              "P37473",
              "P23361",
              "P23277",
              "Q6LCE4",
              "Q9U8S9",
              "Q9GN94",
              "Q24641",
              "P23278",
              "Q03384",
              "P28484",
              "P51550",
              "B4M8Y0",
              "Q05114",
              "P26719",
              "P17648",
              "P48977",
              "P81786",
              "P9WQC2",
              "P9WQC3",
              "P25988",
              "Q00670",
              "P00332",
              "Q2FJ31",
              "Q2G0G1",
              "Q2YSX0",
              "Q5HI63",
              "Q99W07",
              "Q7A742",
              "Q6GJ63",
              "Q6GBM4",
              "Q8NXU1",
              "Q5HRD6",
              "Q8CQ56",
              "Q4J781",
              "P39462",
              "P50381",
              "Q96XE0",
              "P51552",
              "Q5AR48",
              "A5JYX5",
              "P32771",
              "A7ZIA4",
              "Q8X5J4",
              "A7ZX04",
              "A1A835",
              "Q0TKS7",
              "Q8FKG1",
              "B1J085",
              "P25437",
              "B1LIP1",
              "Q1RFI7",
              "P44557",
              "P39450",
              "Q3Z550",
              "P73138",
              "P71017",
              "N4WE73",
              "A1CFL1",
              "N4WE43",
              "N4WW42",
              "P33010",
              "O07737"
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
