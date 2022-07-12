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
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        my_dict = {"id": self.id, "x": self.x, 'size': self.size, "y": self.y}
        return my_dict
