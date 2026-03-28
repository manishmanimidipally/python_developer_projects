from flask import Flask, render_template, request, redirect
import sqlite3
from db import create_table, DB_NAME

app = Flask(__name__)

# Initialize DB
create_table()

def get_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route("/")
def dashboard():
    data = get_data()
    return render_template("dashboard.html", data=data)

# ➕ Add
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        t_type = request.form["type"]
        amount = float(request.form["amount"])
        category = request.form["category"]

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO transactions (type, amount, category) VALUES (?, ?, ?)",
            (t_type, amount, category)
        )
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add_transaction.html")

# 🗑️ Delete
@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

# ✏️ Edit
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    if request.method == "POST":
        t_type = request.form["type"]
        amount = float(request.form["amount"])
        category = request.form["category"]

        cursor.execute("""
            UPDATE transactions
            SET type=?, amount=?, category=?
            WHERE id=?
        """, (t_type, amount, category, id))

        conn.commit()
        conn.close()
        return redirect("/")

    cursor.execute("SELECT * FROM transactions WHERE id=?", (id,))
    data = cursor.fetchone()
    conn.close()

    return render_template("edit_transaction.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)