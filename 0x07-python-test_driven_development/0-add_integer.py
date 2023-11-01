#!usr/bin/python3
"""
This module adds two integers and returns sum of two numbers a & b.
Only accepts integers and floats else TypeError is raised
This module will convert float to integer
"""


def add_integer(a, b=98):
    """
    add_integer: Checks if a, b are int, and
    returns the result casting it in int.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
