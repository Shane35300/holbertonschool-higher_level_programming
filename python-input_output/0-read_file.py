#!/usr/bin/python3
"""
This function print a text file
in the standard output
and remove the last '\n' caractere
"""


def read_file(filename=""):
    """
    filename is a file containing a text
    that this function has to print
    """

    with open(filename, 'r', encoding="utf-8") as txt:
        text = txt.read()
    if text.endswith('\n'):
        text = text[:-1]
    print(text, end="")
