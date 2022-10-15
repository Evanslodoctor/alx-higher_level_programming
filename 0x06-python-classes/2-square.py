#!/usr/bin/python3
""" This module defines a class named 'Square' """


class Square:
    """ Definition of a Square class with private instance attribute, size. """

    def __init__(self, size=0):
        """ Initializing the instance attribute size with validation."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
