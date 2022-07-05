#!/usr/bin/python3
"""
    7-base_geometry module
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

            Raises:
                TypeError: when value is not an integer
                ValueError: when value is less than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
