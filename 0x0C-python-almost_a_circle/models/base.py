#!/usr/bin/python3
"""
    base module
"""


class Base:
    """
        This is the base class
    """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """
            Initializing instances of the base class

            Args:
                id: The id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
