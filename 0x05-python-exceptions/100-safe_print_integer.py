#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    """ function that prints an integer

        Args:
            value: any type (integer, string, etc)
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write("Exception:", e)
