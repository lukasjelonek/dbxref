import tests.env
import unittest
from dbxref import resolver

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
        self.assertNotEqual(resolver.resolve(["EC:1.1.1.1"]), [])
