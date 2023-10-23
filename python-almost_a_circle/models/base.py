#!/usr/bin/python3
"""
Ce script définit une classe appelée "Base"
qui sert de base pour d'autres classes.
La classe "Base" gère un compteur d'instances et attribue
un identifiant unique à chaque instance créée.
"""


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
