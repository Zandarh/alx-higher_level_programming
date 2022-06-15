#!/usr/bin/python3

def safe_function(fct, *args):
    """
    executes a function safely
    Args:
        fct: pointer to a function
    Return:
        The function result
    """
    from sys import stderr
    try:
        result = fct(*args)
        return result
    except Exception as error:
        print("Exception: {}".format(error), file=stderr)
        return None
    else:
        return result
