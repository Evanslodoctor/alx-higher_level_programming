#!/usr/bin/python3
""" Provides a function to write to files """


def write_file(filename="", text=""):
    """ Write to a file passed as an argument"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
