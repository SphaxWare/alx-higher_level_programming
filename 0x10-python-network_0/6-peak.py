#!/usr/bin/python3
"""Peak from a list of unsorted ints"""


def find_peak(list_of_integers):
    """
    Find the peak element of a list.
    """
    nums = list_of_integers
    left, right = 0, len(list_of_integers) - 1

    while left <= right:
        mid = left + ((right - left) // 2)

        # Check if the peak is on the left
        if mid > 0 and nums[mid] < nums[mid - 1]:
            right = mid - 1
        # Check if the peak is on the right
        elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
            left = mid + 1
        # Found the peak
        else:
            return nums[mid]

    # No peak found
    return None
