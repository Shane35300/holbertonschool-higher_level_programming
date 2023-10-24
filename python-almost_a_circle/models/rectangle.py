#!/usr/bin/python3
"""
This file contains the definition of the Rectangle class,
which inherits from the Base class.
It allows for the representation of a rectangle with attributes
for width, height, X position, and Y position.
"""


from models.base import Base


class Rectangle(Base):
    """
    This class defines a rectangle by inheriting from the Base class.
    It represents a rectangle with attributes for width,
    height, X position, and Y position.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
         Constructor for the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The X position of the rectangle. Default is 0.
            y (int, optional): The Y position of the rectangle. Default is 0.
            id (int, optional): The rectangle's identifier. Default is None.

        Raises:
            TypeError: If any of the inputs is not an integer.
            ValueError: If any of the inputs is less than 0.
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        This method returns the area value of
        a Rectangle instance
        """

        return self.__width * self.__height

    def display(self):
        """
        This method print in the standard output the representation
        of a Rectangle instance with the caracter '#'
        """
        string = ""
        for k in range(self.__y):
            string += "\n"
        for i in range(self.__height):
            for l in range(self.__x):
                string += " "
            for j in range(self.__width):
                string += "#"
            string += "\n"
        print(string, end="")

    def __str__(self):
        """
        This method returns a string based on this model:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """

        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

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
                self.width = args[1]
            if count > 2:
                self.height = args[2]
            if count > 3:
                self.x = args[3]
            if count > 4:
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "_Square__size" in kwargs:
                self.size = kwargs["_Square__size"]
                self.width = kwargs["_Square__size"]
                self.height = kwargs["_Square__size"]

    def to_dictionary(self):
        """
        This method returns the dictionary
        representation of a Rectangle instance
        """

        dico = {}
        for key, value in self.__dict__.items():
            if key.startswith("_Rectangle"):
                key = key[12:]
            dico[key] = value
        return dico
