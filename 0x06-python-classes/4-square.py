#!/usr/bin/python3
""" Defines a class "Square" and its attributes """

class Square:
    """ defines a square that must be of integer data type

        Args:
            size: size of the square

        Return:
            Nothing
    """
    def __init__(self, size=0):
        """ Instantiate the square with size equals zero """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

