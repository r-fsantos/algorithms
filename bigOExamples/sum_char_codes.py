#!/usr/bin/env python3


def sum_char_codes(string: str) -> int:
    """Calculates the sum of character codes in a string.

    big(O): O(n)

    Args:
        string: The input string.

    Returns:
        The sum of the Unicode code points of the characters in the string.
    """
    # optimal solution
    total_sum = sum([ord(char) for char in string])

    # improving readability for bigO learning
    total_sum = 0

    # for each char, there's another for-loop execution
    # so we have an O(n) algorithm
    for char in string:
        total_sum += ord(char)

    return total_sum


def sum_char_codes_matching(string: str, needle: int) -> int:
    total_sum = 0

    for char in string:
        code = ord(char)

        if code == needle:
            return total_sum

        total_sum += code

    return total_sum


if __name__ == "__main__":
    assert sum_char_codes(string="0") == 48, "Test 1: '0' == 48"
    assert sum_char_codes(string="renato") == 649, "Test 2: 'renato' == 649"

    assert sum_char_codes_matching(string="0010", needle=49) == 96, "Test 3: '001' == 96"  # noqa
