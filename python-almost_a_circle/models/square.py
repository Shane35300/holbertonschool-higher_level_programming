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
        self.width = value
        self.height = value
        self.__size = value

    def __str__(self):
        """
        This method returns a string based on this model:
        [Square] (<id>) <x>/<y> - <width>/<height>
        """

        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y,
                        self.size))

    def update(self, *args, **kwargs):
        """
        This method is is used to modify instance attributes according
        to a list of arguments
        """
        if args:
            count = 0
            for arg in args:
                count += 1
            if count > 0:
                self.id = args[0]
            if count > 1:
                self.size = args[1]
            if count > 2:
                self.x = args[2]
            if count > 3:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
