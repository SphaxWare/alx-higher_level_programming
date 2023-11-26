#!/usr/bin/python3
"""
    my integer addition module.
    >>> add_integer(1, 5)
    3
"""


def add_integer(a, b=98):
    """the addition of a and b.

    Args:
        a: integer.
        b: another integer, default 98.

    Raises:
        TypeError: if a, b are not int, float.

    Returns:
        The sum of the two integers.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
