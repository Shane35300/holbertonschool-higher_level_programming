#!/usr/bin/python3
"""
Write a function that returns the JSON
representation of an object
(string):
"""


import json


def from_json_string(my_str):
    """
    my_str is a string to serialize
    """

    return json.loads(my_str)
