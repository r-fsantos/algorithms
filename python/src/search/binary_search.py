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
    high = len(haystask)

    while low < high:
        mid = int(low + (high - low) / 2)
        guess = haystask[mid]

        if needle == guess:
            return mid
        elif needle > guess:
            low = mid + 1
        else:
            high = mid

    return None
