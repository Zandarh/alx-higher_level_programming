#!/usr/bin/python3

def safe_print_integer_err(value):
    """
    prints an integer
    Args:
        Value: The parameter checked
    Return:
        True if integer else False
    """
    from sys import stderr
    try:
        print("{:d}".format(value))
        return True
    except ValueError as error:
        print("Exception: {}".format(error), file=stderr)
        return False
    except TypeError as an_other:
        print("Exception: {}".format(an_other), file=stderr)
        return False

