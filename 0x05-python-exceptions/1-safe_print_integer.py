#!/usr/bin/python3
def safe_print_integer(value):
    """ function that prints an integer with formatted string

        Agrs:
            value: any type(integer, string, etc)

        Return:
            if integer return True else False
    """

    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
