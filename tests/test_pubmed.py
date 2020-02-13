import unittest
from dbxref.retrieve import pubmed


class TestPubmed(unittest.TestCase):

    def test_output(self):
        documents = pubmed.retrieve({"db": "PM", "id": "PM:19393038"}, basics=True, references=True, article_ids=True)
        self.assertTrue(documents)


if __name__ == "__main__":
    unittest.main()
