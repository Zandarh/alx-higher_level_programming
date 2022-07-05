#!/usr/bin/python3
"""
    6-base_geometry module
"""


class BaseGeometry:
    """
        An unempty class
    """
    def area(self):
        """
        To raise an exception at the moment
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Function validtaes the value argument

            Args:
                name: The name
                Value: The value to be validated

            Return: True or False
        """
        if not (isinstance(value, int)):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return True
