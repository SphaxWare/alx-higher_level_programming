#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: square size.

        Raises:
            TypeError: not int.
            ValueError: size less than 0.
        """
        self.size = size

    @size.setter
    def size(self, size):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (0 > size):
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    def area(self):
        return self.__size ** 2
