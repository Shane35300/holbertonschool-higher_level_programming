#!/usr/bin/python3
"""
This file contains the definition of the Square class,
which inherits from the Base class.
It allows for the representation of a square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This fonction define a square
    with size, and its position with x and y
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = self.width

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__size = value

    def __str__(self):
        """
        This method returns a string based on this model:
        [Square] (<id>) <x>/<y> - <width>/<height>
        """

        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y,
                        self.size))
