#!/usr/bin/env python3
import unittest
from reversenames import reverse_names

class TestReverseNames(unittest.TestCase):

    def test_multi_reverse(self):
        exepted = ["Ada Lovelace", "Luke Skywalker", "Ford Prefect", "D0rth Vadder"]
        input = ["Lovelace, Ada", "Skywalker, Luke", "Prefect, Ford", "Vadder, D0rth"]
        for i, name in enumerate(input):
            result = reverse_names(name)
            self.assertEqual(result,exepted[i])
    
    def test_reverse(self):
        expected = "Darth Vadder"
        input = "Vadder, Darth"
        result = reverse_names(input)
        self.assertEqual(result,expected)

unittest.main()
