#!/usr/bin/python3
from flask import Flask, render_template
import json
import os

app = Flask(__name__)


@app.route("/items")
def items():
    items_list = []
    json_file = "items.json"

    if os.path.exists(json_file):
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                items_list = data.get("items", [])
        except Exception as e:
            print(f"Error reading JSON file: {e}")

    return render_template("items.html", items=items_list)


if __name__ == "__main__":
    app.run()
