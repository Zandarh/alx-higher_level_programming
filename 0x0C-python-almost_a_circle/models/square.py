#!/usr/bin/python3
"""
    square module
"""
from models.base import Base
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
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def width(self):
        """ Getter for size """
        return super().width

    @width.setter
    def width(self, value):
        """ Setter for size """
        super(Square, self.__class__).width.fset(self, value)
        # incomplete, a slight issue here

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        # incomplete

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        my_dict = {"id": self.id, "x": self.x, 'size': self.size, "y": self.y}
        return my_dict
