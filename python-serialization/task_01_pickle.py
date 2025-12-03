#!/usr/bin/python3
"""serialization"""


import pickle


class CustomObject:
    """serialization"""

    def __init__(self, name, age, is_student):
        """serialization"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """serialization"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialization"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """serialization"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
