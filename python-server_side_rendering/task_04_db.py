#!/usr/bin/python3
from flask import Flask, request, render_template
import json
import csv
import sqlite3

app = Flask(__name__)


# ----------- JSON READER -----------
def read_json_file(file_path):
    """Read JSON data (supports list or {"items": []})"""
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

            if isinstance(data, list):
                return data

            if isinstance(data, dict) and "items" in data:
                return data["items"]

            return []
    except Exception as error:
        print(f"Error reading JSON: {error}")
        return []


# ----------- CSV READER -----------
def read_csv_file(file_path):
    """Read CSV product data"""
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


# ----------- SQLITE READER -----------
def read_sqlite_db(db_path):
    """Read products from SQLite database"""
    products = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        conn.close()
    except Exception as error:
        print(f"Database error: {error}")
        return []

    return products


# ----------- FLASK ROUTE -----------
@app.route("/products")
def show_products():
    source_type = request.args.get("source", "json").lower()
    product_id = request.args.get("id")
    error_message = None
    product_list = []

    # Select data source
    if source_type == "json":
        product_list = read_json_file("products.json")
    elif source_type == "csv":
        product_list = read_csv_file("products.csv")
    elif source_type == "sql":
        product_list = read_sqlite_db("products.db")
    else:
        error_message = "Wrong source"

    # Filter by product ID
    if product_id and not error_message:
        try:
            product_id = int(product_id)

            filtered = [
                p for p in product_list if int(p["id"]) == product_id
            ]

            if not filtered:
                error_message = "Product not found"
            else:
                product_list = filtered

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
