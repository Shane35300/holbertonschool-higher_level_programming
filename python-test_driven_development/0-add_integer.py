#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    :param a: The first number.
    :param b: The second number (default is 98).
    :return: The sum of a and b as an integer.

    This function takes two arguments, a and b, which can be integers or
    floats. It adds these two numbers together and returns the result as
    an integer. If a or b is not a number (i.e., not an int or a float),
    a TypeError is raised.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    var_a = int(a)
    var_b = int(b)
    return var_a + var_b
