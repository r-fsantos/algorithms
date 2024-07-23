#!/usr/bin/env python3


def bubble_sort(array: list[int]) -> list[int]:
    """Implements de bubble sort sorting algorithm.
    It has a O(N^2) running time.

    Args:
        array: Unordered array of integers

    Returns:
        array: Ordered array of integers
    """
    for i in range(0, len(array)):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j + 1]:
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp

    return array
