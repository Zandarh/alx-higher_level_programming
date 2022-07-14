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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

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
                        self.__init__(self.__width, self.__height, self.__x, self.__y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.__width = arg
                elif a == 2:
                    self.__height = arg
                elif a == 3:
                    self.__x = arg
                elif a == 4:
                    self.__y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.__width, self.__height, self.__x, self.__y)
                    else:
                        self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        my_dict = {"x": self.__x, "y": self.__y, "id": self.id,
                   "height": self.__height, "width": self.__width}
        return my_dict
