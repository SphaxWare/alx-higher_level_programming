#!/usr/bin/python3
"""
This module is addition.

>>>add_integer(1, 2)
3
"""
def add_integer(a, b=98):
    """Return result of the addition of a and b
    >>>add_integer(1, 2)
    3
    >>>add_integer(1, s)
    b must be an integer
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
