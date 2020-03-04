import unittest
from dbxref.retrieve import interpro


class TestIPro(unittest.TestCase):

    # Test if ipro retriever gives any output
    def test_output(self):
        documents = interpro.retrieve([{'db': 'InterPro', 'id': 'IPR000003'}], basics=True, hierarchy=True, wikipedia=True,
                                  literature=True, cross_references=True, overlaps=True)
        self.assertTrue(documents)


if __name__ == '__main__':
    unittest.main()
