#!/usr/bin/python3
"""
Contains the inherits_from function
"""


def inherits_from(obj, a_class):
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
