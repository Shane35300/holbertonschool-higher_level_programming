#!/usr/bin/python3
"""
This function write in a text file
in the standard output
and remove the last '\n' caractere
"""


import json


def load_from_json_file(filename):
    """
    filename is a file containing a text
    that this function has to print
    """

    with open(filename, 'r', encoding="utf-8") as txt:
        return json.loads(txt.read())
