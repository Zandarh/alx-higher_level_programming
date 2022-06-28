#!/usr/bin/python3

""" Rectangle class module """


class Rectangle:
    """ This is a rectangle class """

    def __int__(self, width=0, height=0):
        """
            Initialization of the Rectangle class

            Args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.__width = width

    @property
    def width(self):
        """
            Gets the private instance width used by the class
        """
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

    def area(self):
        """
            Calculates the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
            Calculates the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """
            return string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        lenght = list()
        for row in range(self.__height):
            for column in range(self.__width):
                lenght.aappend("#")
        return lenght
