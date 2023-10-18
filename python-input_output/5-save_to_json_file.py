#!/usr/bin/python3
"""
This function write in a text file
in the standard output
and remove the last '\n' caractere
"""


import json


def save_to_json_file(my_obj, filename):
    """
    filename is a file containing a text
    that this function has to print
    """

    with open(filename, 'w', encoding="utf-8") as txt:
        txt.write(json.dumps(my_obj))
