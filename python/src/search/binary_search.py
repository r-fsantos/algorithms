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


if __name__ == "__main__":
    assert (
        binary_search(haystask=list(range(0, 11, 1)), needle=8) == 8
        ), "Test 1: 8"
    assert (
        binary_search(haystask=list(range(0, 11, 1)), needle=100) == None  # noqa
        ), "Test: 2: None"
    assert (
        binary_search(haystask=list(range(-10, -4, 1)), needle=-9) == 1
        ), "Test 3: 1"
    assert (
        binary_search(haystask=list(range(1, 9, 1)), needle=8) == 7
        ), "Test 4: 7"
    assert (
        binary_search(haystask=list(range(1, 9, 1)), needle=1) == 0
        ), "Test 5: 0"
    assert (
        binary_search(haystask=list(range(0, 11, 1)), needle=0) == 0
        ), "Test 6: 0"
