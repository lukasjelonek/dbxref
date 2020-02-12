import unittest
from dbxref.retrieve import gi


class TestGI(unittest.TestCase):

    def test_output(self):
        documents = gi.retrieve({"db": "IG", "id": "P0ABT0", }, basics=True, dbsource=True, references=True)
        self.assertTrue(documents)


if __name__ == "__main__":
    unittest.main()
