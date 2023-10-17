#!/usr/bin/python3
"""
this function return true if "obj" class is the same
as a_class
"""


def inherits_from(obj, a_class):
    """
    obj is the reference
    a_class is the class"""
    if not type(obj) is a_class and issubclass(type(obj), a_class):
            return True
    else:
        return False
