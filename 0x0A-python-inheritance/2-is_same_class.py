#!/usr/bin/python3
""" Checks for an object class"""


def is_same_class(obj, a_class):
    """ returns True if object is exactly an instance
        else False

        Agrs:
            obj: The object to check for
            a_class: The class to compare the object to

        Return:
            True if they are of equal class else false
        """
    if type(obj) == a_class:
        return True
    return False
