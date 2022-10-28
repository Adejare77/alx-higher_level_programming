#!/usr/bin/python3
""" Square Geometry """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Calculate a square geometry """
    def __init__(self, size):
        """ Initialize a square

        Args:
            size: The size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
