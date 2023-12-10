#!/usr/bin/pyython3
"""Creating a Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from both the Base and Rectangle Class"""

    def __init__(self, size, x=0, y=0, id=None) -> None:
        """Instantiation of parameters

        Args:
            size (int): size of the square
            x (int, optional): the height of the square. Defaults to 0.
            y (int, optional): the width of the square. Defaults to 0.
            id (_type_, optional): unique identification for each given
            instances. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self) -> int:
        """returns the modified size attribute"""
        return (self.width)

    @size.setter
    def size(self, value: int):
        """modify the private instance attribute"""
        super().validator("width", value)
        self.width = value
        self.height = value

    def __str__(self) -> str:
        """returns a __str__ representation"""
        return f"[{self.__class__.__name__}] ({self.id}) \
{self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:

        Args:
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        Kwargs:
            must be skipped if *args exists and is not empty.
            Each key in this dictionary represents an attribute to the instance
        """
        try:
            if args:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            elif kwargs:
                for k, v in kwargs.items():
                    setattr(self, k, v)
        except IndexError:
            pass

    def to_dictionary(self) -> dict:
        """returns dictionary representation of instance"""
        _dict = super().to_dictionary()
        del _dict['height']
        del _dict['width']
        _dict['size'] = self.size
        return (_dict)
