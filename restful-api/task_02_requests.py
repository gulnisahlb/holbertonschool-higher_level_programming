#!/usr/bin/python3
"""this is docstr"""
import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        data = response.json()
        for i in data:
            print(i.get("title"))
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open("posts.csv", "w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            for i in data:
                row = {
                    "id": i.get("id"),
                    "title": i.get("title"),
                    "body": i.get("body"),
                }
                writer.writerow(row)
