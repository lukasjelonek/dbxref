import unittest
from dbxref.retrieve import rfam


class TestRfam(unittest.TestCase):

    def test_output(self):
        documents = rfam.retrieve({"db": "Rfam", "id": "RF03094"}, basics=True, references=True)
        self.assertTrue(documents)


if __name__ == "__main__":
    unittest.main()
