import unittest
from dbxref.retrieve import pubmed


class TestPubmed(unittest.TestCase):

    def test_output(self):
        documents = pubmed.retrieve([{"db": "Pubmed", "id": "19393038"}], basics=True)
        self.assertTrue(documents)


if __name__ == "__main__":
    unittest.main()
