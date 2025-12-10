#!/usr/bin/python3
from flask import Flask, request, render_template
import json
import csv

app = Flask(__name__)


def read_json_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data.get("items", [])
    except Exception as error:
        print(f"Error reading JSON: {error}")
        return []


def read_csv_file(file_path):
    products_list = []

    try:
        with open(file_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                products_list.append(row)
    except Exception as error:
        print(f"Error reading CSV: {error}")

    return products_list


@app.route("/products")
def show_products():
    source_type = request.args.get("source", "json").lower()
    product_id = request.args.get("id")
    error_message = None
    product_list = []

    if source_type == "json":
        product_list = read_json_file("products.json")
    elif source_type == "csv":
        product_list = read_csv_file("products.csv")
    else:
        error_message = "Wrong source"

    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [
                product for product in product_list
                if product["id"] == product_id
            ]

            if not filtered_products:
                error_message = "Product not found"
            else:
                product_list = filtered_products

        except ValueError:
            error_message = "Invalid id"

    return render_template(
        "product_display.html",
        products=product_list,
        error=error_message,
        source=source_type
    )


if __name__ == "__main__":
    app.run()
