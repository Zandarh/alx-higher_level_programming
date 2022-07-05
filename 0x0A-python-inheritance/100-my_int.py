#!/usr/bin/python3
"""
    100-my_int module
"""


class MyInt(int):
    """
        MyInt class
    """
    def __init__(self, inverse):
        """
            initiliazing
        """
    def __eq__(self, value):
        """
            Override == opeartor with != behavior.

            Args
                value: The variable checked
        """
        return (super().__ne__(value))

    def __ne__(self, value):
        """
            Override != operator with == behavior.

            Args:
                value: The variable inspected
        """
        return (super().__eq__(value))
