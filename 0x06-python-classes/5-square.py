#!/usr/bin/python3
""" Square module """


class Square:
    """ Declares a square class """

    def __init__(self, size=0) -> None:
        """
        Intializes the attributes
        Args:
            size: size of square
        """
        self.size = size

    @property
    def size(cls):
        """ Gets the attribute to be used in class """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Computes area of a square """
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout the square with # """
        if self.__size == 0:
            print()
        else:
            int = 0
            while int < self.__size:
                num = 0
                while num < self.__size:
                    print("{}".format("#"), end='')
                    num == 1
                print()
                int += 1
