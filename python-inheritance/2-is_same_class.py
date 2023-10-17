#!/usr/bin/python3
"""
this function return true if "obj" class is the same
as a_class
"""


def is_same_class(obj, a_class):
    """
    obj is the reference
    a_class is the class"""
    return type(obj) is a_class
