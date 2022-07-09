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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """ Gets the width """
            return self.__width

        @width.setter
        def width(self, value):
            """ Sets the value argument to width """
            if isinstance(value, int) is False:
                raise TypeError(f"{self.__width} must be an integer")
            elif value <= 0:
                raise ValueError(f"{self.__width} must be > 0")
            else:
                self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            """ Sets the value argument to height """
            if isinstance(value, int) is False:
                raise TypeError(f"{self.__height} must be an integer")
            elif value <= 0:
                raise ValueError(f"{self.__height} must be > 0")
            else:
                self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            """ Sets the value of x """
            if x < 0:
                raise ValueError(f"{self.__x} must be >= 0")
            else:
                self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            """ Sets the value of y """
            if y < 0:
                raise ValueError(f"{self.__y} must be >= 0")
            else:
                self.__y = value

    def area(self):
        """ Function that returns the area of the rectangle """
        return (self.__width * self.__height)

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
        if args is not None and len(args) > 0:
            arg = list(args)
            keylist = []
            i = 1
            while i <= len(arg):
                setattr(self, keylist[i], arg[i])
                i += 1
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        # incomplete, not working as should

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        my_dict = {"x": self.__x, "y": self.__y, "id": self.id,
                   "height": self.__height, "width": self.__width}
        return my_dict