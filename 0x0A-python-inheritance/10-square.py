#!?usr/bin/python3
"""
    10-square module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        A square subclass of Rectangle
    """

    def __init__(self, size):
        """
            insitialization

            Args:
                size: the square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
