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

    def to_json(self, attrs=None):
        dico = {}
        for attr, value in self.__dict__.items():
            if isinstance(value, (int, str, dict, bool, list)):
                if attrs is None:
                    dico[attr] = value
                else:
                    if attr in attrs:
                        dico[attr] = value
                    else:
                        continue
        return dico

    def reload_from_json(self, json):
        for attr, value in json.items():
            if attr in self.__dict__:
                self.__dict__[attr] = value
