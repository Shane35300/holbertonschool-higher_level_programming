#!/usr/bin/python3
"""
This function write in a text file
in the standard output
and remove the last '\n' caractere
"""


read_file = __import__('0-read_file').read_file


def write_file(filename="", text=""):
    """
    filename is a file containing a text
    that this function has to print
    """

    with open(filename, 'w', encoding="utf-8") as txt:
        return txt.write(text)
