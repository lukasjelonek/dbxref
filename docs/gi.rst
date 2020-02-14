.. highlight:: yaml

Gene Identifier
====

Retrieve GI xml documents for dbxrefs and convert them into json.

Options
-------

  * ``--basics`` - Include basic informations such as dbxref/accession-nr., locus, source organism and definition.
  * ``--dbsource`` - Include source database information.
  * ``--references`` - Include reference information.

Input
-----

example: ``GI:P0ABT0``


Output
------

output scheme::

[
    {
        "dbxref": "GI:P0ABT0",
        "definition": "RecName: Full=DNA polymerase III subunit theta",
        "locus": "HOLE_ECO57",
        "molecular_info": null,
        "organism": {
            "name": "Escherichia coli",
            "taxonomy": null
        },
        "references": [
            {
                "authors": [
                    "Perna, N.T.",
                    "Plunkett, G.",
                    "Burland, V.",
                    "Mau, B.",
                    "Glasner, J.D.",
                    "Rose, D.J.",
                    "Mayhew, G.F.",
                    "Evans, P.S.",
                    "Gregor, J.",
                    "Kirkpatrick, H.A.",
                    "Posfai, G.",
                    "Hackett, J.",
                    "Klink, S.",
                    "Boutin, A.",
                    "Shao, Y.",
                    "Miller, L.",
                    "Grotbeck, E.J.",
                    "Davis, N.W.",
                    "Lim, A.",
                    "Dimalanta, E.T.",
                    "Potamousis, K.D.",
                    "Apodaca, J.",
                    "Anantharaman, T.S.",
                    "Lin, J.",
                    "Yen, G.",
                    "Schwartz, D.C.",
                    "Welch, R.A.",
                    "Blattner, F.R."
                ],
                "doi": "10.1038/35054089",
                "journal": {
                    "date": "25.1.2001",
                    "name": "Nature"
                },
                "title": "Genome sequence of enterohaemorrhagic Escherichia coli O157:H7."
            },
            {
                "authors": [
                    "Hayashi, T.",
                    "Makino, K.",
                    "Ohnishi, M.",
                    "Kurokawa, K.",
                    "Ishii, K.",
                    "Yokoyama, K.",
                    "Han, C.G.",
                    "Ohtsubo, E.",
                    "Nakayama, K.",
                    "Murata, T.",
                    "Tanaka, M.",
                    "Tobe, T.",
                    "Iida, T.",
                    "Takami, H.",
                    "Honda, T.",
                    "Sasakawa, C.",
                    "Ogasawara, N.",
                    "Yasunaga, T.",
                    "Kuhara, S.",
                    "Shiba, T.",
                    "Hattori, M.",
                    "Shinagawa, H."
                ],
                "doi": "10.1093/dnares/8.1.11",
                "journal": {
                    "date": "28.2.2001",
                    "name": "DNA Res."
                },
                "title": "Complete genome sequence of enterohemorrhagic Escherichia coli O157:H7 and genomic comparison with a laboratory strain K-12."
            }
        ],
        "source databases": [
            "SMR:P0ABT0",
            "STRING:155864.EDL933_2815",
            "EnsemblBacteria:AAG56832",
            "EnsemblBacteria:AAG56832",
            "EnsemblBacteria:Z2891",
            "EnsemblBacteria:BAB35975",
            "EnsemblBacteria:BAB35975",
            "EnsemblBacteria:BAB35975",
            "GeneID:913059",
            "KEGG:ece:Z2891",
            "KEGG:ecs:ECs2552",
            "PATRIC:fig|386585.9.peg.2675",
            "eggNOG:ENOG4105MPK",
            "eggNOG:ENOG4111UZC",
            "HOGENOM:HOG000219272",
            "KO:K02345",
            "BioCyc:ECOO157:HOLE-MONOMER",
            "Proteomes:UP000000558",
            "Proteomes:UP000002519",
            "GO:GO:0003677",
            "GO:GO:0003887",
            "GO:GO:0006260",
            "Gene3D:1.20.58.250",
            "InterPro:IPR009052",
            "InterPro:IPR036745",
            "Pfam:PF06440"
        ],
        "structure": null
    }
]
