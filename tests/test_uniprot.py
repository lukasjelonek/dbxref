import unittest
from dbxref.retrieve import uniprot

class TestPfam(unittest.TestCase):

    def test_no_position(self):
      '''regression test for missing position parameter in uniprot entry'''
      documents = uniprot.retrieve([{'db': 'UniProtKB/Swiss-Prot', 'id': 'P0CM58'}])
      # this test failed due to an error due to missing None handling, 
      # so no assertions here. Once fixed. this should suffice
