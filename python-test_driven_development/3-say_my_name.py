#!/usr/bin/python3
"""
That function have to print a string that contains
a "first name" and a "last name"
And raise a type error message in case of non-string
"""


def say_my_name(first_name, last_name=""):
    """
    :parameter first_name: is the first name
    :parameter last_name: is the last name
    """
    if not (isinstance(first_name, str) and len(first_name) != 0):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
