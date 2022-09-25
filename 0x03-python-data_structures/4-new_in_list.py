#!/usr/bin/python3
""" function that replaces an element in a list at
    a specific position without modifying the original
    list (like in C).
"""


def new_in_list(my_list, idx, element):
    """ replaces element in the list without
        replacing the original list

    Args:
        my_list: the original list
        idx: index/position of the elment to replace
        element: the new value of the element
    """
    if (idx < 0 or idx > (len(my_list) - 1)):
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
