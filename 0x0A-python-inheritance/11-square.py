#!/usr/bin/python3
"""
    11-square module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        A square subclass
    """

    def __init__(self, size):
        """
            initiliazation

            Args:
                size: The square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
            returns a specific string
        """
        return (f"[Square] {self.__size}/{self.__size}")
