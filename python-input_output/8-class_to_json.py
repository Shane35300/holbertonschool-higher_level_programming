#!/usr/bin/python3
"""
This function write in a text file
in the standard output
and remove the last '\n' caractere
"""


def class_to_json(obj):
    """
    it  returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for
    JSON serialization of an object
    """
    dico = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (int, str, list, dict, bool)):
            dico[attr] = value
    return dico
