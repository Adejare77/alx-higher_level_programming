#!/usr/bin/python3
""" function that removes all characters c and C
    from a string
"""
def no_c(my_string):
    """ removes character c and C

    Args:
        my_string: the string to remove from
    """
    new_str = ""
    for b in my_string:
        if (b != 'c' and b != 'C'):
            new_str += b
    return (new_str)
