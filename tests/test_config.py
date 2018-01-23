import unittest
from dbxref import config

class TestConfig(unittest.TestCase):

    def test_load_providers_works(self):
        self.assertNotEqual(config.load_providers(), [])

    def test_index_providers(self):
        data = [{'name': 'test', 'prefixes':['a', 'b']}]
        self.assertEqual(config.index_providers(data), {'a': data[0], 'b': data[0]})

    def test_normalize_index(self):
        index = {'A': 'some value', 'b': 'some other value'}
        self.assertEqual(config.normalize_index(index), {'a' : 'some value', 'b':'some other value'})

    def test_has_provider(self):
        index = config.normalize_index({'A': 'some value', 'b': 'some other value'})
        self.assertTrue(config._has_provider(index, 'B'))
        self.assertTrue(config._has_provider(index, 'a'))
