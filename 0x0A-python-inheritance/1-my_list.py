#!/usr/bin/python3
"""
cointains the Mylist class
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__int__()

    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))
