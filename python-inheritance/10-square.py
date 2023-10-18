#!/usr/bin/python3
"""
BaseGeometry is a empty class
"""


class BaseGeometry():
    """
    Cette classe représente une figure géométrique.

    Il n'a pas encore d'attributs ou de méthodes spécifiques.
    """

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def integer_validator(self, name, value):
        if type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if name is None:
            raise TypeError("{} must be an integer".format(name))
        if not type(value) is int and not type(value) is float:
            raise TypeError("{} must be an integer".format(name))
        if type(value) is float:
            value = int(value)
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Cette classe représente un rectangle.

    Il n'a pas encore d'attributs ou de méthodes spécifiques.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        string = f"[Rectangle] {self._Square__width}/{self._Square__height}"
        return string


class Square(Rectangle):
    """
    Cette classe représente un carré.

    Il n'a pas encore d'attributs ou de méthodes spécifiques.
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__width = size
        self.__height = size

    def area(self):
        return self.__width * self.__height
