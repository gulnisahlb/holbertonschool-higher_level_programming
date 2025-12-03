#!/usr/bin/python3
"""serialization"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file into a JSON file named data.json"""
    try:
        data_list = []

        with open(csv_filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_list.append(row)

        with open('data.json', 'w') as jsonfile:
            json.dump(data_list, jsonfile, indent=4)

        return True

    except Exception:
        return False
