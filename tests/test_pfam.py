import unittest
from dbxref.retrieve import pfam

class TestPfam(unittest.TestCase):

    def test_no_position(self):
      '''regression test for missing comment in pfam entry'''
      documents = pfam.retrieve([{'db': 'PFAM', 'id': 'PF00083.23'}])
      # this test failed due to an error due to missing None handling, 
      # so no assertions here. Once fixed. this should suffice

    def test_renamed_family(self):
      '''regression test for missing comment in pfam entry'''
      documents = pfam.retrieve([{'db': 'PFAM', 'id': 'Tiny_TM_bacill'}])
      # this test failed due to a redirect when a family was renamed
      # unfortunately the redirect was not encoded in http headers, but in 
      # html markup (<meta http-equiv="Refresh" content="5; URL=/family/PF09680" />)
      # so no assertions here. Once fixed. this should suffice
