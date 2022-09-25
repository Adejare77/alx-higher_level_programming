#!/usr/bin/python3
""" function that replaces an element of a list at
    specific position (like in C).
"""


def replace_in_list(my_list, idx, element):
    """ replaces an element in a list

    Args:
        my_list: the list
        idx: the position of element to be replaced
        element: the new value of the element
    """
    if (idx < 0 or idx > (len(my_list) - 1)):
        return my_list
    my_list[idx] = element
    return (my_list)
