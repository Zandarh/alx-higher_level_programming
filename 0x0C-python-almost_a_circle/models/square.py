#!/usr/bin/python3
"""
    square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        a subclass of class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            initializing instances of this class

            Args:
                size: length of the square
                x:
                y:
                id:
        """
        super(Square, self).__init__(size, size, x, y, id)
        self.x = x
        self.y = y
        self.size = size

    def __str__(self):
        """ String representation of instances """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
