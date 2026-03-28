import sqlite3

DB_NAME = "data.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        amount REAL,
        category TEXT
    )
    """)

    conn.commit()

    # Insert sample data if empty
    cursor.execute("SELECT COUNT(*) FROM transactions")
    count = cursor.fetchone()[0]

    if count == 0:
        sample_data = [
            ("income", 60000, "Salary"),
            ("expense", 4500, "Food"),
            ("expense", 2200, "Transport"),
            ("expense", 3500, "Shopping"),
            ("income", 15000, "Freelance"),
            ("expense", 1800, "Movies"),
            ("expense", 3000, "Bills"),
        ]

        cursor.executemany(
            "INSERT INTO transactions (type, amount, category) VALUES (?, ?, ?)",
            sample_data
        )

        conn.commit()

    conn.close()