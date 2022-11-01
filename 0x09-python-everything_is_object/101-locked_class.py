#!/usr/bin/python3
"""This is a module that containts a clas that avoids dynmaically created attributes.
"""

class LockedClass:
    """A locked class that only lets the user dynamically create the instance attribute 'first_name'
    """
    
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
