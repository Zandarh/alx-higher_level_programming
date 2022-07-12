#!/usr/bin/python3
"""
    base module
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string rep. of list_dictionarie """
        if (list_dictionaries is None):
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string to a file """
        filename = cls.__name__ + '.json'
        with open(filename, 'w+') as my_file:
            if list_objs is None:
                my_file.write("[}")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                my_file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
