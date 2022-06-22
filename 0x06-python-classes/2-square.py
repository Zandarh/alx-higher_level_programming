#!/usr/bin/python3

"""define a class square."""


class Square:
    """Declares a square class"""

    def __init__(self, size=0):
        """initialize  class attribute.

        Args:
            size (int): The size of a new square.
        """

        if typee(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
