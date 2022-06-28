#!/usr/bin/python3

"""
    The print square module
"""

def print_square(size):
    """
        prints a squar with the character #
        
        Args:
            size: The lenght of the square
            
        Return: Returns the square
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for row in range(size):
        for column in range(size):
            print("#", end='')
        print("")
