#!/usr/bin/python3
"""Creating a Rectangle"""

from .base import Base


class Rectangle(Base):
    """Inherits from the Base class (Circle)"""

    @staticmethod
    def validator(parameter: str, value: int):
        if type(value) is not int:
            raise TypeError(f"{parameter} must be an integer")
        elif (parameter == "width" or parameter == "height") and (value <= 0):
            raise ValueError(f"{parameter} must be > 0")
        elif (parameter == "x" or parameter == "y") and (value < 0):
            raise ValueError(f"{parameter} must be >= 0")

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """call the super class with id - this super call with use the the
            logic of the __init__ of the Base class

        Args:
            width (int): width/breadth of the rectangle
            height (int): height/length of the rectangle
            x (int, optional): position of the rectangle in x-direction.
                Defaults to 0.
            y (int, optional): position of the rectangle in y-direction.
                Defaults to 0.
            id (int, optional): unique identification for each given instances.
                Defaults to None.
        """
        super().__init__(id)
        Rectangle.validator("width", width)
        Rectangle.validator("height", height)
        Rectangle.validator("x", x)
        Rectangle.validator("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """Access the private instance attribute"""
    @property
    def width(self):
        """Returns the modified width value"""
        return (self.__width)

    @property
    def height(self):
        """Returns the modified height value"""
        return (self.__height)

    @property
    def x(self):
        """Returns the modified x value"""
        return (self.__x)

    @property
    def y(self):
        """Returns the modified y value"""
        return (self.__y)

    """modify private instance attributes"""
    @width.setter
    def width(self, value):
        """modify the private instance attribute width"""
        self.validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """modify the private instance attribute height"""
        self.validator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """modify the private instance attribute x"""
        self.validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """modify the private instance attribute y"""
        self.validator("y", value)
        self.__y = value

    def area(self) -> int:
        """Returns the Area of the Rectangle"""
        return self.width * self.height

    def display(self) -> None:
        """prints in stdout the Rectangle instance with the
            character #
        """
        print("\n" * self.__y if self.__y > 0 else "", end="")
        [print(" " * self.__x, "#" * self.__width, sep="")
         for h in range(self.__height)]

    def __str__(self) -> str:
        """returns a __str__ representation"""
        return f"[{self.__class__.__name__}] \
({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:

        Args:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        Kwargs:
            must be skipped if *args exists and is not empty.
            Each key in this dictionary represents an attribute to the instance
        """
        try:
            if args:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            elif kwargs:
                for k, v in kwargs.items():
                    setattr(self, k, v)
        except IndexError as e:
            pass

    def to_dictionary(self) -> dict:
        """returns dictionary representation of instance"""
        return {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width
        }
