import unittest
from dbxref import retriever, resolver

class TestPfam(unittest.TestCase):

    def test_no_go_terms(self):
      '''regression test for missing go terms in pfam entry'''
      documents = retriever.retrieve([{'db': 'pfam', 'id': 'PF10423.8'}])
      # this test failed due to an error due to missing None handling, 
      # so no assertions here. Once fixed. this should suffice
