#!/usr/bin/python3
"""
    print square module.
"""
def print_square(size):
    """
    this function print a square with
    size (int)
    """
    if type(size) != int or type(size) == float and 0 > size:
        raise TypeError("size must be an integer")
    if 0 > size:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
