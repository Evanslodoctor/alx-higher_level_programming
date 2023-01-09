#!/usr/bin/python3
"""Reads from a file and prints it to stdout."""


def read_file(filename=""):
    """Reads file and prints its contents."""
    with open(filename, encoding="utf-8") as file:
        read_text = file.read()
        print(read_text, end="")
