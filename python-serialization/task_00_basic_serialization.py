#!/usr/bin/python3
"""serialization"""


import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to JSON and save it to a file """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize JSON data from a file into a Python dictionary."""
    with open(filename, 'r') as file:
        return json.load(file)
