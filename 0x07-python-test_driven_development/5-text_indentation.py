#!/usr/bin/python3
""" This module provides a function for indenting text. """


def text_indentation(text):
    """ Print a text with 2 new lines after each of these chars: ., ? and : """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    print(*(ln.strip() for ln in (text + "\n").splitlines()), sep="\n", end="")
