#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square and its position in a 2D plane."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with a given size and position."""
        self.size = size
        self.position = position

    def area(self):
        """Returns the area of the square."""
        return self.__size**2

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Prints the square with respect to its position."""
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()

    @property
    def position(self):
        """Getter method for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for the position attribute."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(not isinstance(i, int) or i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """Returns a string representation of the square (same as my_print)."""
        show = ""
        if not self.__size:
            return s
        for y in range(self.__position[1]):
            show += '\n'
        for i in range(self.__size):
            for x in range(self.__position[0]):
                show += ' '
            for j in range(self.__size):
                show += '#'
            show += '\n'
        return show[: - 1]
