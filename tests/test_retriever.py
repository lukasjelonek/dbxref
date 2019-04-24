import unittest
from dbxref import retriever, resolver

class TestDbxrefResolve(unittest.TestCase):

    def test_different_case_database_prefix(self):
        entries = resolver.convert_to_dbxrefs(['PFAM:PF00002','Pfam:PF00002','pfam:PF00002', 'EC:2.7.7.1'])
        documents = retriever.retrieve(entries)
        for d in documents:
          with self.subTest(d=d):
            self.assertTrue('description' in d)
