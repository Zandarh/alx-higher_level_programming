#!/usr/bin/python3
""" Square module """
class Square:
    """ Declares a square class """

    def __init__(self, size=0):
        """ defines class attribute
            Args:
                size: size of the square
        """
        self.size = size

        @property
        def size(self):
            """ Gets the attribute to be used in a class """
            return self.__size

        @size.setter
        def size(self, value):
            if type(value) is not int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >=0")
            else:
                self.__size = size

    def area(self):
        """ Computes the area of a square """
        return self.__size ** 2
