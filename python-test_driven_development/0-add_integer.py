#!/usr/bin/python3
"""
>>> add_integer(100, -2)
98
>>> add_integer(2)
100"""


def add_integer(a, b=98):
    """:param a: The first number.
    :param b: The second number (default is 98).
    :return: The sum of a and b as an integer."""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
