.. highlight:: yaml

InterPro
====

Retrieve InterPro json documents for dbxref and select subjects of interest

Options
-------

  * ``--basic`` -"Include basic information such as accession, type, name, description, counters, entry_id and source_database"
  * ``--hierarchy`` -Include hierarchy information of given entry
  * ``--wikipedia`` -Include wikipedia links of given entry
  * ``--literature`` -Include literature treating given entry
  * ``--cross_references`` -Include cross-references of given entry
  * ``--overlaps`` -Include overlaps of given entry with other entries


Input
-----

example: ``InterPro:IPR000003``


Output
------

output scheme::

    [
        {
            "accession": "IPR000003",
            "counters": {
                "domain_architectures": 25,
                "matches": 9752,
                "proteins": 2664,
                "proteomes": 321,
                "sets": 0,
                "structures": 112,
                "taxa": 640
            },
            "cross_references": {
                "cath": {
                    "accessions": [
                        {
                            "accession": "1.10.565.10",
                            "url": "http://www.cathdb.info/version/latest/superfamily/1.10.565.10"
                        },
                        {
                            "accession": "3.30.50.10",
                            "url": "http://www.cathdb.info/version/latest/superfamily/3.30.50.10"
                        }
                    ],
                    "description": "CATH is a classification of protein structures downloaded from the Protein Data Bank.",
                    "displayName": "cath",
                    "rank": 25
                },
                "scop": {
                    "accessions": [
                        {
                            "accession": "g.39.1.2",
                            "url": "http://scop.berkeley.edu/search/?key=g.39.1.2"
                        },
                        {
                            "accession": "a.123.1.1",
                            "url": "http://scop.berkeley.edu/search/?key=a.123.1.1"
                        }
                    ],
                    "description": "The SCOP database, created by manual inspection and abetted by a battery of automated methods, aims to provide a detailed and comprehensive description of the structural and evolutionary relationships between all proteins whose structure is known.",
                    "displayName": "scop",
                    "rank": 24
                }
            },
            "description": [
                "<p>Steroid or nuclear hormone receptors (NRs) constitute an important superfamily of transcription regulators that are involved in widely diverse physiological functions, including control of embryonic development, cell differentiation and homeostasis. Members of the superfamily include the steroid hormone receptors and receptors for thyroid hormone, retinoids, 1,25-dihydroxy-vitamin D3 and a variety of other ligands [[cite:PUB00015853]]. The proteins function as dimeric molecules in nuclei to regulate the transcription of target genes in a ligand-responsive manner [[cite:PUB00004464], [cite:PUB00006168]]. In addition to C-terminal ligand-binding domains, these nuclear receptors contain a highly-conserved, N-terminal zinc-finger that mediates specific binding to target DNA sequences, termed ligand-responsive elements. In the absence of ligand, steroid hormone receptors are thought to be weakly associated with nuclear components; hormone binding greatly increases receptor affinity.</p>\r\n\r\n<p>NRs are extremely important in medical research, a large number of them being implicated in diseases such as cancer, diabetes, hormone resistance syndromes, etc. While several NRs act as ligand-inducible transcription factors, many do not yet have a defined ligand and are accordingly termed 'orphan' receptors. During the last decade, more than 300 NRs have been described, many of which are orphans, which cannot easily be named due to current nomenclature confusions in the literature. However, a new system has recently been introduced in an attempt to rationalise the increasingly complex set of names used to describe superfamily members.</p>",
                "<p>The retinoic acid (retinoid X) receptor consists of 3 functional and \r\n               structural domains: an N-terminal (modulatory) domain; a DNA binding domain\r\n               that mediates specific binding to target DNA sequences (ligand-responsive\r\n               elements); and a hormone binding domain. The N-terminal domain differs \r\n               between retinoic acid isoforms; the small highly-conserved DNA-binding\r\n               domain (~65 residues) occupies the central portion of the protein; and \r\n               the ligand binding domain lies at the receptor C terminus.</p>\r\n\r\n<p> This entry represents retinoid X receptors. It also represents hepatocyte nuclear factor 4 (HNF4), which is a nuclear receptor protein expressed in the liver and kidney, and functions as a key regulator of many metabolic pathways. HNF4 was originally classified as an orphan receptor. Linoleic acid has now been identified as the endogenous ligand for HNF4 in mammalian cells [[cite:PUB00057400]]. </p>"
            ],
            "entry_id": null,
            "entry_type": "family",
            "hierarchy": {
                "accession": "IPR001723",
                "children": [
                    {
                        "accession": "IPR001409",
                        "children": [],
                        "name": "Glucocorticoid receptor",
                        "type": "family"
                    },
                    {
                        "accession": "IPR024178",
                        "children": [
                            {
                                "accession": "IPR001292",
                                "children": [],
                                "name": "Oestrogen receptor",
                                "type": "family"
                            },
                            {
                                "accession": "IPR028355",
                                "children": [],
                                "name": "Estrogen receptor beta/gamma",
                                "type": "family"
                            },
                            {
                                "accession": "IPR027289",
                                "children": [],
                                "name": "Oestrogen-related receptor",
                                "type": "family"
                            }
                        ],
                        "name": "Oestrogen receptor/oestrogen-related receptor",
                        "type": "family"
                    },
                    {
                        "accession": "IPR000324",
                        "children": [],
                        "name": "Vitamin D receptor",
                        "type": "family"
                    },
                    {
                        "accession": "IPR023257",
                        "children": [],
                        "name": "Liver X receptor",
                        "type": "family"
                    },
                    {
                        "accession": "IPR000128",
                        "children": [],
                        "name": "Progesterone receptor",
                        "type": "family"
                    },
                    {
                        "accession": "IPR039067",
                        "children": [],
                        "name": "Hepatocyte nuclear factor 4-alpha",
                        "type": "family"
                    },
                    {
                        "accession": "IPR003069",
                        "children": [],
                        "name": "Ecdysteroid receptor",
                        "type": "family"
                    },
                    {
                        "accession": "IPR003070",
                        "children": [
                            {
                                "accession": "IPR003071",
                                "children": [],
                                "name": "Orphan nuclear receptor, HMR type",
                                "type": "family"
                            },
                            {
                                "accession": "IPR003072",
                                "children": [],
                                "name": "Orphan nuclear receptor, NOR1 type",
                                "type": "family"
                            },
                            {
                                "accession": "IPR003073",
                                "children": [],
                                "name": "Orphan nuclear receptor, NURR type",
                                "type": "family"
                            }
                        ],
                        "name": "Orphan nuclear receptor",
                        "type": "family"
                    },
                    {
                        "accession": "IPR003074",
                        "children": [
                            {
                                "accession": "IPR003075",
                                "children": [],
                                "name": "Peroxisome proliferator-activated receptor, beta",
                                "type": "family"
                            },
                            {
                                "accession": "IPR003076",
                                "children": [],
                                "name": "Peroxisome proliferator-activated receptor alpha",
                                "type": "family"
                            },
                            {
                                "accession": "IPR003077",
                                "children": [],
                                "name": "Peroxisome proliferator-activated receptor gamma",
                                "type": "family"
                            }
                        ],
                        "name": "Peroxisome proliferator-activated receptor",
                        "type": "family"
                    },
                    {
                        "accession": "IPR003078",
                        "children": [],
                        "name": "Retinoic acid receptor",
                        "type": "family"
                    },
                    {
                        "accession": "IPR003079",
                        "children": [],
                        "name": "Nuclear receptor ROR",
                        "type": "family"
                    },
                    {
                        "accession": "IPR000003",
                        "children": [],
                        "name": "Retinoid X receptor/HNF4",
                        "type": "family"
                    },
                    {
                        "accession": "IPR001728",
                        "children": [],
                        "name": "Thyroid hormone receptor",
                        "type": "family"
                    },
                    {
                        "accession": "IPR016355",
                        "children": [],
                        "name": "Nuclear hormone receptor family 5",
                        "type": "family"
                    },
                    {
                        "accession": "IPR033544",
                        "children": [],
                        "name": "Nuclear receptor subfamily 0 group B member 1",
                        "type": "family"
                    }
                ],
                "name": "Nuclear hormone receptor",
                "type": "family"
            },
            "literature": {
                "PUB00004464": {
                    "DOI_URL": "http://dx.doi.org/10.1093/nar/23.4.606",
                    "ISBN": null,
                    "ISO_journal": "Nucleic Acids Res.",
                    "PMID": 7899080,
                    "URL": null,
                    "authors": [
                        "Nishikawa J",
                        "Kitaura M",
                        "Imagawa M",
                        "Nishihara T."
                    ],
                    "issue": "4",
                    "medline_journal": "Nucleic Acids Res",
                    "raw_pages": "606-11",
                    "title": "Vitamin D receptor contains multiple dimerization interfaces that are functionally different.",
                    "volume": "23",
                    "year": 1995
                },
                "PUB00006168": {
                    "DOI_URL": "http://dx.doi.org/10.1093/nar/22.7.1161",
                    "ISBN": null,
                    "ISO_journal": "Nucleic Acids Res.",
                    "PMID": 8165128,
                    "URL": null,
                    "authors": [
                        "De Vos P",
                        "Schmitt J",
                        "Verhoeven G",
                        "Stunnenberg HG."
                    ],
                    "issue": "7",
                    "medline_journal": "Nucleic Acids Res",
                    "raw_pages": "1161-6",
                    "title": "Human androgen receptor expressed in HeLa cells activates transcription in vitro.",
                    "volume": "22",
                    "year": 1994
                },
                "PUB00015853": {
                    "DOI_URL": "http://dx.doi.org/10.1126/stke.2172004pe4",
                    "ISBN": null,
                    "ISO_journal": "Sci. STKE",
                    "PMID": 14747695,
                    "URL": null,
                    "authors": [
                        "Schwabe JW",
                        "Teichmann SA."
                    ],
                    "issue": "217",
                    "medline_journal": "Sci STKE",
                    "raw_pages": "pe4",
                    "title": "Nuclear receptors: the evolution of diversity.",
                    "volume": "2004",
                    "year": 2004
                },
                "PUB00047321": {
                    "DOI_URL": "http://dx.doi.org/10.1093/jb/mvm158",
                    "ISBN": null,
                    "ISO_journal": "J. Biochem.",
                    "PMID": 17761695,
                    "URL": null,
                    "authors": [
                        "Matsushima A",
                        "Kakuta Y",
                        "Teramoto T",
                        "Koshiba T",
                        "Liu X",
                        "Okada H",
                        "Tokunaga T",
                        "Kawabata S",
                        "Kimura M",
                        "Shimohigashi Y."
                    ],
                    "issue": "4",
                    "medline_journal": "J Biochem",
                    "raw_pages": "517-24",
                    "title": "Structural evidence for endocrine disruptor bisphenol A binding to human nuclear receptor ERR gamma.",
                    "volume": "142",
                    "year": 2007
                },
                "PUB00048627": {
                    "DOI_URL": "http://dx.doi.org/10.1016/j.jsbmb.2007.06.006",
                    "ISBN": null,
                    "ISO_journal": "J. Steroid Biochem. Mol. Biol.",
                    "PMID": 17964775,
                    "URL": null,
                    "authors": [
                        "Abad MC",
                        "Askari H",
                        "O'Neill J",
                        "Klinger AL",
                        "Milligan C",
                        "Lewandowski F",
                        "Springer B",
                        "Spurlino J",
                        "Rentzeperis D."
                    ],
                    "issue": "1-2",
                    "medline_journal": "J Steroid Biochem Mol Biol",
                    "raw_pages": "44-54",
                    "title": "Structural determination of estrogen-related receptor gamma in the presence of phenol derivative compounds.",
                    "volume": "108",
                    "year": 2008
                },
                "PUB00048874": {
                    "DOI_URL": "http://dx.doi.org/10.1002/prot.22294",
                    "ISBN": null,
                    "ISO_journal": "Proteins",
                    "PMID": 19004016,
                    "URL": null,
                    "authors": [
                        "Borel F",
                        "de Groot A",
                        "Juillan-Binard C",
                        "de Rosny E",
                        "Laudet V",
                        "Pebay-Peyroula E",
                        "Fontecilla-Camps JC",
                        "Ferrer JL."
                    ],
                    "issue": "2",
                    "medline_journal": "Proteins",
                    "raw_pages": "538-42",
                    "title": "Crystal structure of the ligand-binding domain of the retinoid X receptor from the ascidian Polyandrocarpa misakiensis.",
                    "volume": "74",
                    "year": 2009
                },
                "PUB00050267": {
                    "DOI_URL": "http://dx.doi.org/10.1016/j.bbrc.2008.06.050",
                    "ISBN": null,
                    "ISO_journal": "Biochem. Biophys. Res. Commun.",
                    "PMID": 18582436,
                    "URL": null,
                    "authors": [
                        "Matsushima A",
                        "Teramoto T",
                        "Okada H",
                        "Liu X",
                        "Tokunaga T",
                        "Kakuta Y",
                        "Shimohigashi Y."
                    ],
                    "issue": "3",
                    "medline_journal": "Biochem Biophys Res Commun",
                    "raw_pages": "408-13",
                    "title": "ERRgamma tethers strongly bisphenol A and 4-alpha-cumylphenol in an induced-fit manner.",
                    "volume": "373",
                    "year": 2008
                },
                "PUB00051211": {
                    "DOI_URL": "http://dx.doi.org/10.1074/jbc.M801920200",
                    "ISBN": null,
                    "ISO_journal": "J. Biol. Chem.",
                    "PMID": 18441008,
                    "URL": null,
                    "authors": [
                        "Greschik H",
                        "Althage M",
                        "Flaig R",
                        "Sato Y",
                        "Chavant V",
                        "Peluso-Iltis C",
                        "Choulier L",
                        "Cronet P",
                        "Rochel N",
                        "Schule R",
                        "Stromstedt PE",
                        "Moras D."
                    ],
                    "issue": "29",
                    "medline_journal": "J Biol Chem",
                    "raw_pages": "20220-30",
                    "title": "Communication between the ERRalpha homodimer interface and the PGC-1alpha binding surface via the helix 8-9 loop.",
                    "volume": "283",
                    "year": 2008
                },
                "PUB00057400": {
                    "DOI_URL": "http://dx.doi.org/10.1371/journal.pone.0005609",
                    "ISBN": null,
                    "ISO_journal": "PLoS ONE",
                    "PMID": 19440305,
                    "URL": null,
                    "authors": [
                        "Yuan X",
                        "Ta TC",
                        "Lin M",
                        "Evans JR",
                        "Dong Y",
                        "Bolotin E",
                        "Sherman MA",
                        "Forman BM",
                        "Sladek FM."
                    ],
                    "issue": "5",
                    "medline_journal": "PLoS One",
                    "raw_pages": "e5609",
                    "title": "Identification of an endogenous ligand bound to a native orphan nuclear receptor.",
                    "volume": "4",
                    "year": 2009
                }
            },
            "name": {
                "name": "Retinoid X receptor/HNF4",
                "short": "Retinoid-X_rcpt/HNF4"
            },
            "overlaps": [
                {
                    "accession": "IPR013088",
                    "name": "Zinc finger, NHR/GATA-type",
                    "type": "homologous_superfamily"
                },
                {
                    "accession": "IPR035500",
                    "name": "Nuclear hormone receptor-like domain superfamily",
                    "type": "homologous_superfamily"
                }
            ],
            "source_database": "interpro",
            "wikipedia": null
        }
    ]
