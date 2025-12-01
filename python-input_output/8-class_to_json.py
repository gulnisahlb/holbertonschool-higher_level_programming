#!/usr/bin/python3
"""Function that returns the dictionary description of a class instance"""


def class_to_json(obj):
    """Return the dictionary description of obj for JSON serialization"""
    return obj.__dict__.copy()
