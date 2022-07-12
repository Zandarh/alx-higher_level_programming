#!/usr/bin/python3
"""
    rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
        a subclass of base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializing the class instance

            Args:
                width: The width of the rectangle
                height: The eight of the rectangle
                x:
                y:
                id:
        """
        super(Rectangle, self).__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """ Gets the width """
            return self.__width

        @width.setter
        def width(self, value):
            """ Sets the value argument to width """
            if type(value) != int:
                raise TypeError("width must be an integer")
            elif value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            """ Sets the value argument to height """
            if type(value) != int:
                raise TypeError("height must be an integer")
            elif value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            """ Sets the value of x """
            if type(value) != int:
                raise TypeError("x must be an integer")
            if x < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            """ Sets the value of y """
            if type(value) != int:
                raise TypeError("y must be an integer")
            if y < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value

    def area(self):
        """ Function that returns the area of the rectangle """
        return (self.width * self.height)

    def display(self):
        """ prints in stdout the rectangle with character # """
        for i in range(self.__y):
            print()
        for row in range(self.__height):
            for j in range(self.__x):
                print(' ', end='')
            for column in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """ Gives a string representation """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}" \
            f" - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        my_dict = {"x": self.x, "y": self.y, "id": self.id,
                   "height": self.height, "width": self.width}
        return my_dict
