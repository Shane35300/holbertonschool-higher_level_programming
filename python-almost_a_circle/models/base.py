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

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of dictionaries represented by json_string.
        """

        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """

        rect = cls(3, 4)
        rect.update(**dictionary)
        return rect

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding="utf-8") as txt:
                json_str = txt.read()
                list_dicts = cls.from_json_string(json_str)
            instances = []
            for data in list_dicts:
                dico = {}
                for key, value in data.items():
                    if key.startswith("_Rectangle"):
                        key = key[12:]
                    if key.startswith("_Square"):
                        key = key[9:]
                    dico[key] = value
                instance = cls.create(**dico)
                instances.append(instance)
            return instances
        except FileNotFoundError:
            return []
