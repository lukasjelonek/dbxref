import unittest
from dbxref.retrieve import kegg

class TestKegg(unittest.TestCase):

    def test_parser_output(self):
        documents = kegg.retrieve([{"db": "KEGG", "id": "K00121"}])
