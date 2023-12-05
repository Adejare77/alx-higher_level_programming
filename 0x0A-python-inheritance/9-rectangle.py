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
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ returns the area of the rectangle """
        return (self.__height * self.__width)

    def __str__(self):
        """ prints the ratio of the width to height """
        return f"[Rectangle] {self.__width}/{self.__height}"
