#!/usr/bin/python3
"""
Ce script définit une classe appelée "Base"
qui sert de base pour d'autres classes.
La classe "Base" gère un compteur d'instances et attribue
un identifiant unique à chaque instance créée.
"""


import json


class Base():
    """
    Initialisation de la variable de classe
    pour compter le nombre d'instances de "Base"
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        this function returns a json string representation of
        list dictionnaries
        """

        if list_dictionaries is None:
            return "[]"
        else:
            string = ""
            string += json.dumps(list_dictionaries)
        return string

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.
        The filename will be based on the class name.
        """

        filename = cls.__name__ + ".json"
        list = []
        if list_objs is not None:
            for obj in list_objs:
                list.append(obj.__dict__)

        with open(filename, 'w') as txt:
            txt.write(cls.to_json_string(list))
