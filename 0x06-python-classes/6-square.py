#!/usr/bin/python3
""" Defining a Square"""


class Square:

    """ Defining a class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """ Initializing
        args:
            size(int): size of the square
        """

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @property
    def position(self):
        """Setting a tuple of 2 positive integers"""
        return self.__position

    @size.setter
    def size(self, value):
        if isinstance(value, int) and value >= 0:
            self.__size = value
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @position.setter
    def position(self, value):

        if not isinstance(value, tuple) or (value[0] <= 0 or value[1] <= 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""

        if self.__size > 0:
            for _ in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print('_' * self.__position[0], end='')
                print('#' * self.__size, end='')
                print()
        else:
            print()
