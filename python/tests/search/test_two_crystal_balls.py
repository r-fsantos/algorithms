#!/usr/bin/env python3

import random
import unittest

from src.search.two_crystal_balls import two_crystal_balls


class TestTwoCrystalBalls(unittest.TestCase):
    def test_two_crystal_balls(self):
        # Generate a random index within the range [0, 9999]
        idx = random.randint(0, 9999)

        # Create an array of 10000 elements, initially filled with False
        data = [False] * 10000

        # Set elements from the randomly chosen index to True
        for i in range(idx, 10000):
            data[i] = True

        # Check if the function correctly identifies the starting index of the True sequence  # noqa
        self.assertEqual(two_crystal_balls(data), idx)

        # Test the function with an array filled with False, expecting -1 as the result  # noqa
        self.assertEqual(two_crystal_balls([False] * 821), -1)


if __name__ == "__main__":
    unittest.main()
