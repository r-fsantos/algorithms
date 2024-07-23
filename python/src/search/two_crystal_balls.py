#!/usr/bin/env python3


def two_crystal_balls(breaks: list[bool]) -> int:
    """Given the following problem:

    Given two crystal balls that will break if dropped from high enough
    distance, determine the exact spot in which it will break in the most
    optimized way.

    Solution: Iterates over the array with a well-established jump amount,
    given by the square root of the size of the array. Once a true value is
    found, then the index go back of a jump amount and go forward until a new
    counter hits the jump amount or the array size.

    It's a middle term solution between linear search and binary search
    algorithms. It's running time is O(qrt(n)).

    Args:
        breaks: An array of booleans

    Returns:
        The first occurrence of true or -1 if not found.
    """
    jmp_amount = int(len(breaks) ** 0.5)

    for i in range(breaks[jmp_amount], len(breaks), jmp_amount):
        if breaks[i]:
            break

    i -= jmp_amount
    j = 0
    while j < jmp_amount and i < len(breaks):
        if breaks[i]:
            return i
        i += 1
        j += 1

    return -1
