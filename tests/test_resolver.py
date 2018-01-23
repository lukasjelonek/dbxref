import unittest
from dbxref import resolver

valid_ids = [
                'GO:0097281',
                'EC:1.1.1.1',
                'UniProtKB/Swiss-Prot:P12345',
                'UniProtKB/TrEMBL:A2VB99',
                'taxon:452271',
                'pubmed:19037750',
                'PDB:4AJY',
                'http://www.google.de',
                'https://www.google.de',
                'GeneID:956582',
                'GI:731497',
                'PFAM:PF00002',
                'RFAM:RF00360',
                'InterPro:IPR002928',
                'SO:0000704',
]

invalid_ids = [
                'GO:123',
                'EC:hoho',
                'UniProtKB/Swiss-Prot:45',
                'UniProtKB/TrEMBL:99',
                'taxon:hoho',
                'pubmed:hoho',
                'PDB:hoho',
                'http://wurst',
                'https://wurst',
                #'InterPro:hoho',
                #'GI:hoho',
                #'GeneID:hoho',
                #'PFAM:hoho',
                #'RFAM:hoho',
                #'SO:123',
]

class TestDbxrefResolve(unittest.TestCase):

    def test_conversion_of_string_to_dbxref(self):

        data = [
                ('GO:1234', {'db': 'GO', 'id': '1234'}),
                ('https://www.google.de', {'db': 'https', 'id': '//www.google.de'}),
                ('db:sub:id', {'db': 'db', 'id': 'sub:id'}),
                
                ]
        for d in data:
            with self.subTest(d=d):
                self.assertEqual(resolver.convert_string_to_dbxref(d[0]), d[1])


    def test_resolve_enzyme(self):
        self.assertNotEqual(resolver.resolve(resolver.convert_to_dbxrefs(["EC:1.1.1.1"])), [])

    def test_check_dbxref_exists(self):
        import logging
        from dbxref.resolver import STATUS_EXISTS, STATUS_NOT_EXISTS, STATUS_UNSUPPORTED_DB, STATUS_UNKNOWN
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger().setLevel(logging.WARNING)
        resolver.logger.setLevel(logging.DEBUG)
        data = [
                # existent ids
                ('GO:0097281', STATUS_EXISTS),
                ('EC:1.1.1.1', STATUS_EXISTS),
                ('UniProtKB/Swiss-Prot:P12345', STATUS_EXISTS),
                ('UniProtKB/TrEMBL:A2VB99', STATUS_EXISTS),
                ('taxon:452271', STATUS_EXISTS),
                ('pubmed:19037750', STATUS_EXISTS),
                ('PDB:4AJY', STATUS_EXISTS),
                ('http://www.google.de', STATUS_EXISTS),
                ('https://www.google.de', STATUS_EXISTS),

                # non existent ids
                ('GO:123', STATUS_NOT_EXISTS),
                ('EC:hoho', STATUS_NOT_EXISTS),
                ('UniProtKB/Swiss-Prot:45', STATUS_NOT_EXISTS),
                ('UniProtKB/TrEMBL:99', STATUS_NOT_EXISTS),
                ('taxon:hoho', STATUS_NOT_EXISTS),
                ('pubmed:hoho', STATUS_NOT_EXISTS),
                ('PDB:hoho', STATUS_NOT_EXISTS),
                ('http://wurst', STATUS_NOT_EXISTS),
                ('https://wurst', STATUS_NOT_EXISTS),

                # currently unsupported
                #('GeneID:956582', FOUND),
                #('GI:731497', FOUND),
                #('PFAM:PF00002', FOUND),
                #('RFAM:RF00360', FOUND),
                #('InterPro:IPR002928', FOUND),
                #('SO:0000704', FOUND),

                #('InterPro:hoho', NOT_FOUND),
                #('GI:hoho', NOT_FOUND),
                #('GeneID:hoho', NOT_FOUND),
                #('PFAM:hoho', NOT_FOUND),
                #('RFAM:hoho', NOT_FOUND),
                #('SO:123', NOT_FOUND),
                ]

        for d in data:
            with self.subTest(d=d):
                self.assertEqual(resolver.check_dbxref_exists(resolver.convert_string_to_dbxref(d[0])), d[1] )

    def test_check_urls(self):
        import requests
        dbxrefs = resolver.convert_to_dbxrefs(valid_ids)
        resolved = resolver.resolve(dbxrefs, check_existence=False)
        for r in resolved:
          for k in r['locations']:
            for url in r['locations'][k]:
              with self.subTest(url=url):
                try:
                  with requests.get(url, allow_redirects=True, timeout=3) as req:
                    self.assertLess(req.status_code, 400)
                except:
                    self.assertTrue(False)


