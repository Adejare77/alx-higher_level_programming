#!/usr/bin/python3
def safe_print_division(a, b):
    """ function that divides 2 integers and prints the result

        Args:
            a: first integer
            b: second integer

        Return:
            the result of the division
    """
    try:
        c = a / b
        print("Inside result: {}".format(c))
        return (c)
    except Exception:
        print("Inside result: {}". format(None))
        return None
