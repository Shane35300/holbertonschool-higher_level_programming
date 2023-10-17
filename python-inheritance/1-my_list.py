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

    def print_sorted(self):
        """
        This method sorts the elements in the list
        and prints the sorted list.
        """
        for item in self:
            if not isinstance(item, int):
                raise TypeError('Not all elements in the list are integers')
        print(sorted(self))
