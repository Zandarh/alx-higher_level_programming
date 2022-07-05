#!/usr/bin/python3
"""
    1-list module
"""


class MyList (list):
    """
        subclass of list
    """

    def print_sorted(self):
        """
            Sorts the list before printing
        """
        print(sorted(self))
