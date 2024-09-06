#!/usr/bin/env python3

def heapsort(nums: list[int]) -> list[int]:
    build_heap(nums)

    for i in range(len(nums) - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, 0, i)
    return nums


def build_heap(nums: list[int]):
    n = len(nums)
    for i in range(n // 2, -1, -1):
        heapify(nums, i, n)
    print(nums)


def heapify(v: list[int], i: int, hs: int):
    """
    v: heap
    i: current index
    hs: heap_size
    largest_i: largest value between a parent and its childs
    lc: left child
    rc: right child
    """
    largest_i = i
    lc = 2 * i + 1
    rc = 2 * i + 2

    if lc < hs and v[lc] > v[i]:
        largest_i = lc

    if rc < hs and v[rc] > v[largest_i]:
        largest_i = rc

    if largest_i != i:
        v[i], v[largest_i] = v[largest_i], v[i]
        heapify(v, largest_i, hs)


if __name__ == "__main__":
    input1 = [100, 19, 36, 17, 3, 25, 1, 2, 7]
    assert heapsort(input1) == [1, 2, 3, 7, 17, 19, 25, 36, 100]

    input2 = [100, 19, 36, 17, 3, 25, 1, 2, 2]
    assert heapsort(input2) == [1, 2, 2, 3, 17, 19, 25, 36, 100]

    input3 = [25, 19, 36, 17, 3, 100, 1, 2, 2]
    assert heapsort(input3) == [1, 2, 2, 3, 17, 19, 25, 36, 100]

    input4 = [10, 2, 3, 20, 4]
    build_heap(input4)
