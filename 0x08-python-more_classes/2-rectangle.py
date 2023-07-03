#!/usr/bin/python3
""" Defines a Rectangle class."""


class Rectangle:
    def __init__(self, width=0, height=0):
        """ initialize a new rectangle.
        Args:
            width(int): the width of the new rectangle.
            height(int): the height of the new rectangle. """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """ return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)
