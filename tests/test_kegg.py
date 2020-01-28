import unittest
from dbxref.retrieve import uniprot

class TestKegg(unittest.TestCase):

    def test_parser_output(self):
        documents = uniprot.retrieve([{"db": "KEGG", "id": "K00121"}])
