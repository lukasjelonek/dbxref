import tests.env
import unittest
from dbxref import config

class TestConfig(unittest.TestCase):

    def test_load_providers_works(self):
        self.assertNotEqual(config.load_providers(), [])

    def test_index_providers(self):
        data = [{'name': 'test', 'prefixes':['a', 'b']}]
        self.assertEqual(config.index_providers(data), {'a': data[0], 'b': data[0]})
