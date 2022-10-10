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
        return (c)
    except Exception:
        c = None
        return c
    finally:
        print("Inside result: {}".format(c))
