#!/usr/bin/env python3

import unittest

from main import binary_search as bs


class TestBinarySearch(unittest.TestCase):
    def test_it_should_find_occurrence(self):
        self.assertEqual(bs([2, 5, 8, 12, 16, 23, 38], 8), 2)


# if __name__ == "__main__":
#     unittest.main()
