.. highlight:: yaml

Kegg
====

Retrieve kegg text documents for dbxref and convert them into json.

Options
-------

  * ``--basic`` -Include ID/Entry, names/aliases and definition
  * ``--pathway`` -Include metabolic pathway
  * ``--brite`` -Include hierarchical classifications
  * ``--dbxref_links`` -Include database links in dbxref format
  * ``--genes`` -Include associated genes
  * ``--reference`` -Include paper reference ID, authors,title and published journal
  * ``--orthology`` -Include ortholog genes
  * ``--motif`` -Include motif
  * ``--formula`` -Include chemical formula
  * ``--reaction`` -Include chemical reaction partners

Input
-----

example: ``KEGG:K05859``


Output
------

Entry: NULL
Orthology: NULL
Motif: NULL
Formula: NULL
Reaction: NULL
[
    {
        "brite": {
            "edges": {
                "0": [
                    "1",
                    "5",
                    "23",
                    "55",
                    "90"
                ],
                "1": [
                    "2"
                ],
                "10": [],
                "100": [
                    "101",
                    "105"
                ],
                "101": [
                    "102"
                ],
                "102": [
                    "103"
                ],
                "103": [
                    "4"
                ],
                "104": [],
                "105": [
                    "106"
                ],
                "106": [
                    "107"
                ],
                "107": [
                    "4"
                ],
                "108": [],
                "11": [
                    "4"
                ],
                "12": [],
                "13": [
                    "4"
                ],
                "14": [],
                "15": [
                    "4"
                ],
                "16": [],
                "17": [
                    "4"
                ],
                "18": [],
                "19": [
                    "4"
                ],
                "2": [
                    "3"
                ],
                "20": [],
                "21": [
                    "4"
                ],
                "22": [],
                "23": [
                    "24",
                    "39",
                    "44",
                    "47",
                    "50"
                ],
                "24": [
                    "25",
                    "27",
                    "29",
                    "31",
                    "33",
                    "35",
                    "37"
                ],
                "25": [
                    "4"
                ],
                "26": [],
                "27": [
                    "4"
                ],
                "28": [],
                "29": [
                    "4"
                ],
                "3": [
                    "4"
                ],
                "30": [],
                "31": [
                    "4"
                ],
                "32": [],
                "33": [
                    "4"
                ],
                "34": [],
                "35": [
                    "4"
                ],
                "36": [],
                "37": [
                    "4"
                ],
                "38": [],
                "39": [
                    "40",
                    "42"
                ],
                "4": [],
                "40": [
                    "4"
                ],
                "41": [],
                "42": [
                    "4"
                ],
                "43": [],
                "44": [
                    "45"
                ],
                "45": [
                    "4"
                ],
                "46": [],
                "47": [
                    "48"
                ],
                "48": [
                    "4"
                ],
                "49": [],
                "5": [
                    "6"
                ],
                "50": [
                    "51",
                    "53"
                ],
                "51": [
                    "4"
                ],
                "52": [],
                "53": [
                    "4"
                ],
                "54": [],
                "55": [
                    "56",
                    "63",
                    "70",
                    "73",
                    "80",
                    "87"
                ],
                "56": [
                    "57",
                    "59",
                    "61"
                ],
                "57": [
                    "4"
                ],
                "58": [],
                "59": [
                    "4"
                ],
                "6": [
                    "7",
                    "9",
                    "11",
                    "13",
                    "15",
                    "17",
                    "19",
                    "21"
                ],
                "60": [],
                "61": [
                    "4"
                ],
                "62": [],
                "63": [
                    "64",
                    "66",
                    "68"
                ],
                "64": [
                    "4"
                ],
                "65": [],
                "66": [
                    "4"
                ],
                "67": [],
                "68": [
                    "4"
                ],
                "69": [],
                "7": [
                    "4"
                ],
                "70": [
                    "71"
                ],
                "71": [
                    "4"
                ],
                "72": [],
                "73": [
                    "74",
                    "76",
                    "78"
                ],
                "74": [
                    "4"
                ],
                "75": [],
                "76": [
                    "4"
                ],
                "77": [],
                "78": [
                    "4"
                ],
                "79": [],
                "8": [],
                "80": [
                    "81",
                    "83",
                    "85"
                ],
                "81": [
                    "4"
                ],
                "82": [],
                "83": [
                    "4"
                ],
                "84": [],
                "85": [
                    "4"
                ],
                "86": [],
                "87": [
                    "88"
                ],
                "88": [
                    "4"
                ],
                "89": [],
                "9": [
                    "4"
                ],
                "90": [
                    "91"
                ],
                "91": [
                    "92"
                ],
                "92": [
                    "4"
                ],
                "93": [],
                "94": [
                    "95"
                ],
                "95": [
                    "96"
                ],
                "96": [
                    "97"
                ],
                "97": [
                    "98"
                ],
                "98": [
                    "4"
                ],
                "99": []
            },
            "vertices": [
                "KEGG Orthology (KO) [BR:ko00001]",
                "09100 Metabolism",
                "09101 Carbohydrate metabolism",
                "00562 Inositol phosphate metabolism",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "09130 Environmental Information Processing",
                "09132 Signal transduction",
                "04014 Ras signaling pathway",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "04012 ErbB signaling pathway",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "04370 VEGF signaling pathway",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "04064 NF-kappa B signaling pathway",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "04066 HIF-1 signaling pathway",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "04020 Calcium signaling pathway",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "04070 Phosphatidylinositol signaling system",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "04072 Phospholipase D signaling pathway",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "09150 Organismal Systems",
                "09151 Immune system",
                "04611 Platelet activation",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "04625 C-type lectin receptor signaling pathway",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "04650 Natural killer cell mediated cytotoxicity",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "04662 B cell receptor signaling pathway",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "04664 Fc epsilon RI signaling pathway",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "04666 Fc gamma R-mediated phagocytosis",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "04670 Leukocyte transendothelial migration",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "09152 Endocrine system",
                "04935 Growth hormone synthesis, secretion and action",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "04919 Thyroid hormone signaling pathway",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "09156 Nervous system",
                "04722 Neurotrophin signaling pathway",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "09157 Sensory system",
                "04750 Inflammatory mediator regulation of TRP channels",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "09158 Development and regeneration",
                "04360 Axon guidance",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "04380 Osteoclast differentiation",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "09160 Human Diseases",
                "09161 Cancer: overview",
                "05200 Pathways in cancer",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "05206 MicroRNAs in cancer",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "05205 Proteoglycans in cancer",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "09162 Cancer: specific types",
                "05225 Hepatocellular carcinoma",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "05214 Glioma",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "05223 Non-small cell lung cancer",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "09167 Endocrine and metabolic disease",
                "04933 AGE-RAGE signaling pathway in diabetic complications",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "09171 Infectious disease: bacterial",
                "05110 Vibrio cholerae infection",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "05120 Epithelial cell signaling in Helicobacter pylori infection",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "05131 Shigellosis",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "09172 Infectious disease: viral",
                "05170 Human immunodeficiency virus 1 infection",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "05167 Kaposi sarcoma-associated herpesvirus infection",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "05169 Epstein-Barr virus infection",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "09176 Drug resistance: antineoplastic",
                "01521 EGFR tyrosine kinase inhibitor resistance",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "09180 Brite Hierarchies",
                "09182 Protein families: genetic information processing",
                "04131 Membrane trafficking",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "Enzymes [BR:ko01000]",
                "3. Hydrolases",
                "3.1 Acting on ester bonds",
                "3.1.4 Phosphoric-diester hydrolases",
                "3.1.4.11 phosphoinositide phospholipase C",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "Membrane trafficking [BR:ko04131]",
                "Exocytosis",
                "Calcium ion-dependent exocytosis",
                "Phospholipases",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2",
                "Endocytosis",
                "Macropinocytosis",
                "Phospholipase C",
                "K05859 PLCG2; phosphatidylinositol phospholipase C, gamma-2"
            ]
        },
        "dbxref_links": [
            "RN:R03332",
            "RN:R03435",
            "RN:R10952",
            "GO:0004435"
        ],
        "definition": "phosphatidylinositol phospholipase C, gamma-2 [EC:3.1.4.11]",
        "genes": [
            "HSA: 5336(PLCG2)",
            "PTR: 454268(PLCG2)",
            "PPS: 100984694(PLCG2)",
            "GGO: 101133643(PLCG2)",
            "PON: 100457650(PLCG2)",
            "NLE: 100604145(PLCG2)",
            "MCC: 714173(PLCG2)",
            "MCF: 102117471(PLCG2)",
            "CSAB: 103233371(PLCG2)",
            "RRO: 104671624(PLCG2)",
            "RBB: 108539491(PLCG2)",
            "CJC: 100390347(PLCG2)",
            "SBQ: 101030999(PLCG2)",
            "MMU: 234779(Plcg2)",
            "MCAL: 110300336(Plcg2)",
            "MPAH: 110337392(Plcg2)",
            "RNO: 29337(Plcg2)",
            "MUN: 110550263(Plcg2)",
            "CGE: 100752475(Plcg2)",
            "NGI: 103725694 103748739",
            "HGL: 101714597 101715321(Plcg2)",
            "CCAN: 109696649(Plcg2)",
            "OCU: 100340139(PLCG2)",
            "TUP: 102483786(PLCG2)",
            "CFA: 489692(PLCG2)",
            "VVP: 112911890 112912331",
            "AML: 100481994(PLCG2)",
            "UMR: 103662093(PLCG2)",
            "UAH: 113252535(PLCG2)",
            "ORO: 101378505(PLCG2)",
            "ELK: 111152978",
            "FCA: 101080675(PLCG2)",
            "PTG: 102963653(PLCG2)",
            "PPAD: 109245637(PLCG2)",
            "AJU: 106984018(PLCG2)",
            "BTA: 100337091(PLCG2)",
            "BOM: 102285300(PLCG2)",
            "BIU: 109572707(PLCG2)",
            "BBUB: 102396307(PLCG2)",
            "CHX: 102180337(PLCG2)",
            "OAS: 101122126(PLCG2)",
            "SSC: 100518663(PLCG2)",
            "CFR: 102514470(PLCG2)",
            "CDK: 105089440(PLCG2)",
            "BACU: 103014764(PLCG2)",
            "LVE: 103070997(PLCG2)",
            "OOR: 101285216(PLCG2)",
            "DLE: 111179463(PLCG2)",
            "PCAD: 102983230(PLCG2)",
            "ECB: 100055670(PLCG2)",
            "EPZ: 103558212(PLCG2)",
            "EAI: 106832855(PLCG2)",
            "MYB: 102261553(PLCG2)",
            "MYD: 102773476(PLCG2)",
            "MNA: 107524904(PLCG2)",
            "HAI: 109378365(PLCG2)",
            "DRO: 112300725(PLCG2)",
            "PALE: 102883128(PLCG2)",
            "RAY: 107521319(PLCG2)",
            "MJV: 108400464(PLCG2)",
            "LAV: 100658990(PLCG2)",
            "TMU: 101346393",
            "MDO: 100027579(PLCG2)",
            "SHR: 100919206(PLCG2)",
            "PCW: 110212621(PLCG2)",
            "OAA: 100076776(PLCG2)",
            "GGA: 415805(PLCG2)",
            "MGP: 100549684(PLCG2)",
            "CJO: 107319403(PLCG2)",
            "NMEL: 110404260(PLCG2)",
            "APLA: 101799246(PLCG2)",
            "ACYG: 106033167 106044837",
            "TGU: 100219388(PLCG2)",
            "LSR: 110476350(PLCG2)",
            "SCAN: 103816730(PLCG2)",
            "GFR: 102039725(PLCG2)",
            "FAB: 101811465(PLCG2)",
            "PHI: 102103443(PLCG2)",
            "PMAJ: 107209788(PLCG2)",
            "CCAE: 111934454(PLCG2)",
            "CCW: 104691823(PLCG2)",
            "ETL: 114066562(PLCG2)",
            "FPG: 101914329(PLCG2)",
            "FCH: 102058636(PLCG2)",
            "CLV: 102095823(PLCG2)",
            "EGZ: 104133768(PLCG2)",
            "NNI: 104014569(PLCG2)",
            "ACUN: 113484485(PLCG2)",
            "PADL: 103923865(PLCG2)",
            "AAM: 106483269(PLCG2) 106489897",
            "ASN: 102378303(PLCG2)",
            "AMJ: 106736910(PLCG2)",
            "PSS: 102454220(PLCG2)",
            "CMY: 102930635(PLCG2)",
            "CPIC: 101932685(PLCG2)",
            "ACS: 100566814(plcg2)",
            "PVT: 110085508(PLCG2)",
            "PBI: 103052396(PLCG2)",
            "PMUR: 107292601(PLCG2)",
            "TSR: 106539149(PLCG2)",
            "PMUA: 114601931(PLCG2)",
            "GJA: 107105783(PLCG2)",
            "XLA: 108714087(plcg2.L)",
            "XTR: 100496686(plcg2)",
            "NPR: 108786572(PLCG2)",
            "DRE: 561747(plcg2)",
            "SRX: 107722471 107738392",
            "SANH: 107656933 107666218 107666222(plcg2) 107684680",
            "SGH: 107559804(plcg2) 107587040 107587041",
            "CCAR: 109047939 109057498",
            "IPU: 108264222(plcg2)",
            "PHYP: 113534527(plcg2)",
            "AMEX: 103036277(plcg2)",
            "EEE: 113577174(plcg2)",
            "TRU: 101072923(plcg2)",
            "TNG: GSTEN00016798G001",
            "LCO: 104932460(plcg2)",
            "NCC: 104955634 104957481",
            "MZE: 101479429(plcg2)",
            "ONL: 100697485(plcg2)",
            "OLA: 101157053(plcg2)",
            "XMA: 102220131(plcg2)",
            "XCO: 114137117(plcg2)",
            "PRET: 103466833(plcg2)",
            "CVG: 107084318(plcg2)",
            "NFU: 107389305(plcg2)",
            "KMR: 108237447(plcg2)",
            "ALIM: 106536649(plcg2)",
            "AOCE: 111563111(plcg2) 111586863",
            "CSEM: 103379748(plcg2)",
            "POV: 109641214(plcg2)",
            "LCF: 108902239(plcg2)",
            "SDU: 111229657(plcg2)",
            "SLAL: 111647676(plcg2)",
            "HCQ: 109513068(plcg2)",
            "BPEC: 110169397(plcg2)",
            "MALB: 109967271(plcg2)",
            "SASA: 106573684(plcg2)",
            "OTW: 112252303(plcg2)",
            "SALP: 111952198(plcg2)",
            "ELS: 105018577(plcg2)",
            "SFM: 108926548 108926652(plcg2)",
            "PKI: 111851875(plcg2)",
            "LCM: 102358132(PLCG2) 102358647",
            "CMK: 103175953(plcg2)",
            "RTP: 109923219 109928135 109928136",
            "API: 100161327"
        ],
        "id": "K05859",
        "names": [
            "PLCG2"
        ],
        "pathways": [
            "ko00562 Inositol phosphate metabolism",
            "ko01100 Metabolic pathways",
            "ko01521 EGFR tyrosine kinase inhibitor resistance",
            "ko04012 ErbB signaling pathway",
            "ko04014 Ras signaling pathway",
            "ko04020 Calcium signaling pathway",
            "ko04064 NF-kappa B signaling pathway",
            "ko04066 HIF-1 signaling pathway",
            "ko04070 Phosphatidylinositol signaling system",
            "ko04072 Phospholipase D signaling pathway",
            "ko04360 Axon guidance",
            "ko04370 VEGF signaling pathway",
            "ko04380 Osteoclast differentiation",
            "ko04611 Platelet activation",
            "ko04625 C-type lectin receptor signaling pathway",
            "ko04650 Natural killer cell mediated cytotoxicity",
            "ko04662 B cell receptor signaling pathway",
            "ko04664 Fc epsilon RI signaling pathway",
            "ko04666 Fc gamma R-mediated phagocytosis",
            "ko04670 Leukocyte transendothelial migration",
            "ko04722 Neurotrophin signaling pathway",
            "ko04750 Inflammatory mediator regulation of TRP channels",
            "ko04919 Thyroid hormone signaling pathway",
            "ko04933 AGE-RAGE signaling pathway in diabetic complications",
            "ko04935 Growth hormone synthesis, secretion and action",
            "ko05110 Vibrio cholerae infection",
            "ko05120 Epithelial cell signaling in Helicobacter pylori infection",
            "ko05131 Shigellosis",
            "ko05167 Kaposi sarcoma-associated herpesvirus infection",
            "ko05169 Epstein-Barr virus infection",
            "ko05170 Human immunodeficiency virus 1 infection",
            "ko05200 Pathways in cancer",
            "ko05205 Proteoglycans in cancer",
            "ko05206 MicroRNAs in cancer",
            "ko05214 Glioma",
            "ko05223 Non-small cell lung cancer",
            "ko05225 Hepatocellular carcinoma"
        ],
        "reference": [
            {
                "DOI": [
                    "10.1016/0014-5793(88)80979-7"
                ],
                "authors": "Ohta S, Matsui A, Nazawa Y, Kagawa Y",
                "dbxref": "PMID:2849563",
                "doi": "",
                "journal": "FEBS Lett 242:31-5 (1988)",
                "title": "Complete cDNA encoding a putative phospholipase C from transformed human lymphocytes."
            },
            {
                "DOI": [
                    "10.1371/journal.pone.0059842"
                ],
                "authors": "Bernal-Quiros M, Wu YY, Alarcon-Riquelme ME, Castillejo-Lopez C",
                "dbxref": "PMID:23555801",
                "doi": "",
                "journal": "PLoS One 8:e59842 (2013)",
                "title": "BANK1 and BLK act through phospholipase C gamma 2 in B-cell signaling."
            }
        ],
        "type": "KO"
    }
]

