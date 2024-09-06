#!/usr/bin/env python3


def insertion_sort(arr: list[int]) -> list[int]:
    """
    Insertion sort:
        - Divide to conquer approach.
        - PROBLEM = problem + problem + ... + problem
        - [first, ]
        - [first, , ]
        - [first, , ..., last]

    Complexity:
        - Time:
            - Best Case: 0(n)
            - Worst Case: O(n^2)
                - Diagonal of a square, minus the first row
        - Space:
            - O(n), In-place solution
    """
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j + 1] < arr[j]:
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1
    return arr


if __name__ == "__main__":
    arr0 = [1, 2, 3, 4]
    exp0 = arr0

    arr1 = [4, 3, 2, 1]
    exp1 = [1, 2, 3, 4]

    assert insertion_sort(arr0) == exp0, "Test 1 failed"
    assert insertion_sort(arr1) == exp1, "Test 2 failed"
