#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square in 2D space.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a new instance of the Square class.
        size(self): Getter for the size attribute.
        size(self, value): Setter for the size attribute.
        position(self): Getter for the position attribute.
        position(self, value): Setter for the position attribute.
        area(self): Calculates the area of the square.
        my_print(self): Prints the square using '#' characters, respecting the position.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new instance of the Square class.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square in 2D space.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size of the square."""
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
        """Get or set the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position of the square in 2D space.
        """
        self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters, respecting the position."""
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
                if j == self.size - 1:
                    print()

