#!/usr/bin/env python3


def binary_search(haystask: list[int], needle: int) -> int | None:
    """Finds the index fot thre first occurrence of a needle on a haystack.

    Implements the Binary Search Algorithm. BigO: O(log n)

    Args:
        haystack: An ordered array of integers
        needle: The integer to be found in the haystack

    Returns:
        The first occurrence of the needle in the harstack
        or None if not found.
    """
    low = 0
    high = len(haystask) - 1

    while high >= low:
        mid = (high + low) // 2

        if needle == haystask[mid]:
            return mid
        elif needle > haystask[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return None
