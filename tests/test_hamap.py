#!/usr/bin/env python3

import unittest
from dbxref.retrieve import hamap


class TestHAMAP(unittest.TestCase):

    def test_output(self):
        """test if HAMAP retriever gives any output, ergo functions in any way"""
        documents = hamap.retrieve([{"db": "HAMAP", "id": "HM:MF_00607"}], matrix=True)

        self.assertTrue(documents)


if __name__ == "__main__":
    unittest.main()
