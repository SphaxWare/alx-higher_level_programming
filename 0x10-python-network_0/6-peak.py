#!/usr/bin/python3
"""Peak from a list of unsorted ints"""


def find_peak(list_of_integers):
    """
    find the peak unt of a list
    """
    nums = list_of_integers
    l, r = 0, len(list_of_integers) - 1


    while l <= r:
        m = l + ((r - l) // 2)
        # left greater
        if m > 0 and nums[m] < nums[m - 1]:
            r = m - 1
        # right is grater
        elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
            l = m + 1
        else:
            return m
