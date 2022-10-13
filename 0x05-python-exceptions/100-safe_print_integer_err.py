#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        ans = isinstance(value, int)
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write(f"Exception: {e}\n")
        return False
