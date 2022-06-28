#!/usr/bin/python3

""" Rectangle class module """


class Rectangle:
    """ This is a rectangle class """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
            Initialization of the Rectangle class

            Args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        """
            Returns a new rectangle

            Args:
                size: length of width and height
            Returns:
                new instance of class
        """
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            gives the biggest rectangle based on the area
            Args:
                rect_1: First rectangle
                rect_2: Second rectangle
            Returns:
                the biggest rectangle based on the area
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area()) == (rect_2.area()):
            return rect_1
        if (rect_1.area()) > (rect_2.area()):
            return rect_1
        return rect_2

    def __str__(self):
        """
            return string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        length = list()
        for row in range(self.__height):
            for column in range(self.__width):
                length.append(str(self.print_symbol))
            if row + 1 != self.__height:
                length.append('\n')
        return ''.join(length)

    def __repr__(self):
        """
            Returns a string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
            Deletes a rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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
