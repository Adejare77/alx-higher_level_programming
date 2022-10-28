#!/usr/bin/python3
""" checks if an object is an instance of a class """


def is_kind_of_class(obj, a_class):
    """ The function compares the obj to the a_class

        Agrs:
            obj: The object of the class to find
            a_class: The class to compare the object to

        Return:
            True if it is of instance else False
    """
    if issubclass(type(obj), a_class):
        return True
    return False
