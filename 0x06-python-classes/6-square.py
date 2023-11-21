#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        if self.position[1] > 0:
            for i in range(0, self.position[1]):
                print()
        for i in range(0, self.size):
            if self.position[0] > 0:
                for i in range(0, self.position[0]):
                    print(' ', end="")
            for j in range(0, self.size):
                print('#', end="")
                if (j == self.size - 1):
                    print()
