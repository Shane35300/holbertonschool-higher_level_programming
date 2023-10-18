#!/usr/bin/python3
"""
BaseGeometry is a empty class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
