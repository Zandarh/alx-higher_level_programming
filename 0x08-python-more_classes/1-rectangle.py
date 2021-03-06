#!/usr/bin/python3

""" Rectangle module based on 0-rectangle.py"""


class Rectangle:
    """ Represent a square """

    def __init__(self, width=0, height=0):
        """
            Initialization of the Rectangle class

            Args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
            Gets the private instance height used by the class
        """
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
