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
    except TypeError as error:
        print("Exceptions: {}".format(error), file=stderr)
    except IndexError as ind:
        print("Exceptions: {}".format(ind), file=stderr)
    except ZeroDivisionError as zer:
        print("Exceptions: {}".format(zer), file=stderr)
    except ValueError as var:
        print("Exceptions: {}".format(var), file=stderr)
