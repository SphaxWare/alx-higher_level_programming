"""Square module."""


class Square:
    """Defines an empty square."""
    def __init__(self, size=0):
        self.__size = size
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (0 > size):
            raise ValueError("size must be >= 0")
