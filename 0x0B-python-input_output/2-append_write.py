#!/usr/bin/python3
""" Provides a function to append to files """


def append_write(filename="", text=""):
    """ Appends text to a file passed as an argument"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
