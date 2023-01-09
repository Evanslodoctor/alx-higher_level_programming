#!/usr/bin/python3
""" Serialize the writable attributes of an object"""


def class_to_json(obj):
    """ Serialize the writable attrs of an obj"""
    return obj.__dict__
