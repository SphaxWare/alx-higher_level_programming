#!/usr/bin/python3
"""
Rectangle module.
"""


class Rectangle:
    """
    Rectangle class
    """

    number_of_instances = 0
    """int: number of rectangle instances.i"""

    print_symbol = "#"
    """type: Print symbol, any type."""

    def __init__(self, width=0, height=0):
        """
        Constructor for the Rectangle class.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """return new string representing the Rectangle"""
        rec = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rec += str(self.print_symbol)
            if i != self.__height - 1:
                rec += "\n"
        return rec

    def __repr__(self):
        """return a representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """delete the rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls.__height = cls.__width = size
