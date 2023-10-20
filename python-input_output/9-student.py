#!/usr/bin/python3
"""
This is a class of student
Public instance attributes:
first_name, last_name, age
"""


class Student():
    """
    it returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for
    JSON serialization of an object
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        dico = {}
        for attr, value in self.__dict__.items():
            if isinstance(value, (int, str, dict, bool, list)):
                dico[attr] = value
        return dico
