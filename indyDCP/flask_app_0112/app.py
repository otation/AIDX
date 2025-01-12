from flask import Flask, request, render_template, redirect, url_for
import pymysql
from datetime import datetime

app = Flask(__name__)

# Database configuration
DB_CONFIG = {
    "host": "192.168.3.111",
    "user": "inteldx",
    "password": "intel2024!",
    "database": "test_bm",
    "port": 3306
}

def get_db_connection():
    return pymysql.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"],
        port=DB_CONFIG["port"]
    )

def generate_order_no():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        today_date = datetime.now().strftime("%Y%m%d")
        query = f"SELECT COUNT(*) FROM orders WHERE OrderNo LIKE '{today_date}_%'"
        cursor.execute(query)
        result = cursor.fetchone()
        next_number = result[0] + 1
        new_order_no = f"{today_date}_{next_number:04d}"
    connection.close()
    return new_order_no

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit_order", methods=["POST"])
def submit_order():
    try:
        product_quantities = {
            "product1": int(request.form.get("product1", 0)),
            "product2": int(request.form.get("product2", 0)),
            "product3": int(request.form.get("product3", 0)),
            "product4": int(request.form.get("product4", 0)),
            "product5": int(request.form.get("product5", 0)),
            "product6": int(request.form.get("product6", 0)),
            "product7": int(request.form.get("product7", 0)),
            "product8": int(request.form.get("product8", 0)),
            "product9": int(request.form.get("product9", 0)),
        }

        order_no = generate_order_no()

        connection = get_db_connection()
        with connection.cursor() as cursor:
            insert_query = (
                "INSERT INTO orders (OrderNo, Product1Qty, Product2Qty, Product3Qty, Product4Qty, Product5Qty, Product6Qty, Product7Qty, Product8Qty, Product9Qty) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            )
            cursor.execute(insert_query, (order_no, *product_quantities.values()))
            connection.commit()

        return redirect(url_for("list_orders"))

    except Exception as e:
        return f"An error occurred: {e}", 500

@app.route("/list_orders")
def list_orders():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            select_query = "SELECT No, OrderNo, OrderDate, Product1Qty, Product2Qty, Product3Qty, Product4Qty, Product5Qty, Product6Qty, Product7Qty, Product8Qty, Product9Qty FROM orders"
            cursor.execute(select_query)
            orders = cursor.fetchall()

        return render_template("list_orders.html", orders=orders)

    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
