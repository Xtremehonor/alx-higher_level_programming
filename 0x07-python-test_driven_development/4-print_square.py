#!/usr/bin/python3
"""
Module prints square depending on size

"""

def print_square(size):
    """
    print_square: prints square

    """
   
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0 :
        raise ValueError("size must be >= 0")
    else:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end='')
            print('')
