#!/usr/bin/env python3

import unittest

from main import bubble_sort as bbs


class TestBubbleSort(unittest.TestCase):
    def test_it_should_order_a_large_array(self):
        self.assertListEqual(
            bbs([38, 23, 16, 12, 8, 5, 2]), [2, 5, 8, 12, 16, 23, 38]
        )
        self.assertListEqual(
            bbs([42, 38, 23, 16, 12, 8, 5, 2]), [2, 5, 8, 12, 16, 23, 38, 42]
        )

    def test_it_should_return_empty_array_for_empty_input(self):
        self.assertEqual(len(bbs([])), 0)


if __name__ == "__main__":
    unittest.main()
