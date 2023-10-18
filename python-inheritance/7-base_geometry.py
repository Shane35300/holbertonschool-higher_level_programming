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
        if not type(value) is int and not type(value) is float:
            raise TypeError("{} must be an integer".format(name))
        if type(value) is float:
            value = int(value)
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
