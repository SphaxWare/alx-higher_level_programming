#!/usr/bin/python3
"""Define a MagicClass bytecode."""


import math


class MagicClass:
    """A circle"""

    def __init__(self, radius=0):
        """Initialize MagicClass.
        Arg:
            radius (float or int): radius
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Return area of circle"""
        return self.__radius**2 * math.pi

    def circumference(self):
        """Return The circumference of the circle"""
        return 2 * math.pi * self.__radius
