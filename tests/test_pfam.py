import unittest
from dbxref.retrieve import pfam

class TestPfam(unittest.TestCase):

    def test_no_position(self):
      '''regression test for missing comment in pfam entry'''
      documents = pfam.retrieve([{'db': 'PFAM', 'id': 'PF00083.23'}])
      # this test failed due to an error due to missing None handling, 
      # so no assertions here. Once fixed. this should suffice
