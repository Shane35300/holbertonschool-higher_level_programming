#!/usr/bin/python3
"""
This is a simple Python script that defines a class called MyList.
MyList is a subclass of the built-in list class and has an additional method
to print a sorted version of the list.
"""


class MyList(list):
    """
    MyList is a subclass of the list class,
    inheriting its properties and methods.
    """

    def __init__(self, *args):
        """
        Initializes a MyList instance with the provided values.
        """
        super().__init__(args)

    def print_sorted(self):
        """
        This method sorts the elements in the list
        and prints the sorted list.
        """
        print(sorted(self))
