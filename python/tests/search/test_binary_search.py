#!/usr/bin/env python3

import unittest

from main import binary_search as bs


class TestBinarySearch(unittest.TestCase):
    def test_it_should_find_occurrences_for_large_input(self):
        self.assertEqual(bs([2, 5, 8, 12, 16, 23, 38], 8), 2)

        self.assertEqual(bs(list(range(0, 11, 1)), 8), 8)
        self.assertEqual(bs(list(range(-10, -4, 1)), -9), 1)
        self.assertEqual(bs(list(range(1, 9, 1)), 8), 7)
        self.assertEqual(bs(list(range(1, 9, 1)), 1), 0)
        self.assertEqual(bs(list(range(0, 11, 1)), 0), 0)

    def test_it_should_find_occurrence_single_element_input(self):
        self.assertEqual(bs([1], 1), 0)

    def test_it_should_return_none_for_single_element_input(self):
        self.assertIsNone(bs([1], 0))

    def test_it_should_return_none_for_empty_array(self):
        self.assertIsNone(bs([], 42))

    def test_it_should_return_none_for_not_found_occurrences(self):
        self.assertIsNone(bs(list(range(0, 11, 1)), 100))


if __name__ == "__main__":
    unittest.main()
