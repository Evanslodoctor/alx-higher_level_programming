#!/usr/bin/python3
""" Insert text in a file after specific lines """


def append_after(filename="", search_string="", new_string=""):
    """ Insert text to file after lines with a specific string """
    with open(filename, 'r+') as file:
        lines = [
            line + new_string * (search_string in line)
            for line in file.readlines()
        ]
        file.seek(0)
        file.writelines(lines)
