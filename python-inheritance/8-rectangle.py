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
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if name is None:
            raise TypeError("{} must be an integer".format(name))
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("{} must be an integer".format(name))
        if isinstance(value, float):
            value = int(value)
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
