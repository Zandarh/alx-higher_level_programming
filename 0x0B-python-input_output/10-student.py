#!/usr/bin/python3
"""
    10-student module
"""


class Student:
    """
        a class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
            initialization of the iinstance of class Student

            Args:
                first_name: The student's first name
                last_name: The student's last name
                age: The sturent's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Retrieves the dict representation of the Student instance
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
