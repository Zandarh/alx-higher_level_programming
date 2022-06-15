#!/usr/bin/python3

def safe_print_division(a, b):
    """
    divides 2 integers and prints the result

    Args:
        a: numerator
        b: denominator

    Return:
        The division result
    """
    result = None
    try:
        result = a / b
        return (result)

    except (ValueError, ZeroDivisionError):
        return (result)
    finally:
        print("Inside result: {}".format(result))
