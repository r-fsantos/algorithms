#!/usr/bin/env python3


def linear_search(haystack: list[int], needle: int) -> int:
    """Finds the index for the first occurrence of a needle inside
    of a haystack

    Implements de Linear Search Algorithm. Big O: O(n)

    Args:
        haystack: An ordered array of integers
        needle: The integer to be found in the haystack

    Returns:
        The first occurrence of the needle in the harstack
        or None if not found.
    """
    for i in range(0, len(haystack), 1):
        if needle == haystack[i]:
            return i
    return None
