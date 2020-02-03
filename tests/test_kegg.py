import unittest
from dbxref.retrieve import kegg


class TestKegg(unittest.TestCase):

    def test_output(self):
        documents = kegg.retrieve([{"db": "KEGG", "id": "K00121"}], basics=True, brite=True, pathway=True,
                                  dbxrefs_links=True, formula=True, reaction=True, genes=True, motif=True,
                                  orthology=True, reference=True)

    def test_brite_output_1(self):
        # test
        brite_example_1 = [["BRITE       Root1"],
                           ["             branch1"],
                           ["              branch2"],
                           ["               Branch3"],
                           ["                BRANCH4"],
                           ["                 branch5"]
                           ]
        brite_example_output_1 = {"vertices": ["Root1", "branch1", "branch2", "Branch3", "BRANCH4", "branch5"],
                                  "edges": {"0": ["1"],
                                            "1": ["2"],
                                            "2": ["3"],
                                            "3": ["4"],
                                            "4": ["5"],
                                            "5": []
                                            }
                                  }
        self.assertEqual(kegg.read_brite(brite_example_1), brite_example_output_1)

        # test
        brite_example_2 = [["BRITE       Root1"],
                           ["             branch1"],
                           ["              branch2"],
                           ["             Branch3"],
                           ["              BRANCH4"],
                           ["               branch5"]
                           ]
        brite_example_output_2 = {"vertices": ["Root1", "branch1", "branch2", "Branch3", "BRANCH4", "branch5"],
                                "edges": {"0": ["1", "3"],
                                          "1": ["2"],
                                          "2": [],
                                          "3": ["4"],
                                          "4": ["5"],
                                          "5": []
                                          }
                                  }
        self.assertEqual(kegg.read_brite(brite_example_2), brite_example_output_2)

        # test
        brite_example_3 = [["BRITE       Root1"],
                           ["             branch1"],
                           ["              branch2"],
                           ["            Branch3"],
                           ["             BRANCH4"],
                           ["              branch5"]
                           ]
        brite_example_output_3 = {"vertices": ["Root1", "branch1", "branch2", "Branch3", "BRANCH4", "branch5"],
                                  "edges": {"0": ["1"],
                                            "1": ["2"],
                                            "2": [],
                                            "3": ["4"],
                                            "4": ["5"],
                                            "5": []
                                            }
                                  }
        self.assertEqual(kegg.read_brite(brite_example_3), brite_example_output_3)

        # test
        brite_example_4 = [["BRITE       Root1"],
                           ["             branch1"],
                           ["              branch2"],
                           ["              Branch3"],
                           ["              BRANCH4"],
                           ["              branch5"]
                           ]
        brite_example_output_4 = {"vertices": ["Root1", "branch1", "branch2", "Branch3", "BRANCH4", "branch5"],
                                  "edges": {"0": ["1"],
                                            "1": ["2", "3", "4", "5"],
                                            "2": [],
                                            "3": [],
                                            "4": [],
                                            "5": []
                                            }
                                  }
        self.assertEqual(kegg.read_brite(brite_example_4), brite_example_output_4)

        # test
        brite_example_5 = [["BRITE       Root1"],
                           ["             branch1"],
                           ["              branch2"],
                           ["               Branch3"],
                           ["                BRANCH4"],
                           ["                 branch5"],
                           ["                Branch6"],
                           ["                Branch7"],
                           ["              Branch8"],
                           ["               Branch9"]
                           ]
        brite_example_output_5 = {"vertices": ["Root1", "branch1", "branch2", "Branch3", "BRANCH4", "branch5",
                                               "Branch6", "Branch7", "Branch8", "Branch9"],
                                  "edges": {"0": ["1"],
                                            "1": ["2", "8"],
                                            "2": ["3"],
                                            "3": ["4", "6", "7"],
                                            "4": ["5"],
                                            "5": [],
                                            "6": [],
                                            "7": [],
                                            "8": ["9"],
                                            "9": []
                                            }
                                  }
        self.assertEqual(kegg.read_brite(brite_example_5), brite_example_output_5)


if __name__ == '__main__':
    unittest.main()