#!/usr/bin/python3
"""
BaseGeometry is a empty class
"""


Rectangle = __import__('9-rectangle').Rectangle


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

    def __str__(self):
        string = f"[Rectangle] {self.__width}/{self.__height}"
        return string
