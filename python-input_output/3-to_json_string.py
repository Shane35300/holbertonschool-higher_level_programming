#!/usr/bin/python3
"""
Write a function that returns the JSON
representation of an object
(string):
"""


import json


def to_json_string(my_obj):
    """
    my_obj is a string to serialize
    """

    return json.dumps(my_obj)
