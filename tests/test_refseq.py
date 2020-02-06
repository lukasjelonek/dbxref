import unittest
from dbxref.retrieve import refseq


class TestRefSeq(unittest.TestCase):

    def test_output(self):
        """Test if refseq.py gives any output"""
        documents = refseq.retrieve([{"db": "RefSeq", "id": "3269"}])
        self.assertTrue(documents)


if __name__ == '__main__':
    unittest.main()
