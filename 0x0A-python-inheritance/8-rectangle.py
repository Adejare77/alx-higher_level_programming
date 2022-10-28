#!/usr/bin/python3
""" Inheriting from BaseGemetry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ calculates Rectangular geometry """
    def __init__(self, width, height):
        """ Instantiation of width and height of the rectangle

            Args:
                width: breath of the rectangle
                height: height of the rectangle

            Return:
                Nothing yet
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
