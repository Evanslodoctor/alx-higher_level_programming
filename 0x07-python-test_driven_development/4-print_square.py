#!/usr/bin/python3
""" This module provides a function that prints a square. """


def print_square(size):
    " Print the square with the character #. "
    if type(size) is not int:       # != vs is not?... 'Readability counts'
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(*(["#" * size] * size), sep="\n")
