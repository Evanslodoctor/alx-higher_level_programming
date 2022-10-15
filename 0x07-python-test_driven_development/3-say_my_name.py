#!/usr/bin/python3
""" This module provides a function that prints your name. """


def say_my_name(first_name, last_name=""):
    " Print the given name. "
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
