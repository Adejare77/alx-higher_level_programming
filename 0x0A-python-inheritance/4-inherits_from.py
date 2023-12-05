#!/usr/bin/python3
"""
Checks if an objects is an instance of a class
that inherits directly or indirectly
"""


def inherits_from(obj, a_class):
    """ Returns True if the obj is a subclass else
        false

        Args:
            obj: object to check for
            a_class: what to compare the object to

        Return:
            True if it is a subclass else False
    """
    if issubclass(type(obj), a_class):
        return True
    return False
