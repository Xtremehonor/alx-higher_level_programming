#!/usr/bin/python3
"""
A module that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    list all the attributes and methods of an object
    """
    return dir(obj)
