#!/usr/bin/python3
""" BaseGeometry """


class BaseGeometry:
    """ defines BaseGeometry class """
    def area(self):
        """ calculate BaseGeometry Area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ checks if the value is an integer number greater than
            zero

            Agrs:
                name: string type. name of
                value: an integer > 0

            Return:
                Error if value is not an integer or less than zero
        """
        if not (type(value) == int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
