#!/usr/bin/python3
"""
Module that contains a function that returns the number of lines of a text file
"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    with open(filename, 'r', encoding='utf8') as f:
        i = 0
        for i in f:
            i += 1
        return i
