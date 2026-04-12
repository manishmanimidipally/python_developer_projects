import sqlite3

def connect():
    return sqlite3.connect("jobs.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        company TEXT,
        source TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def insert_job(title, company):
    conn = connect()
    cursor = conn.cursor()

    # Prevent duplicates
    cursor.execute(
        "SELECT * FROM jobs WHERE title=? AND company=?",
        (title, company)
    )
    exists = cursor.fetchone()

    if not exists:
        cursor.execute(
            "INSERT INTO jobs (title, company, source) VALUES (?, ?, ?)",
            (title, company, "RemoteOK")
        )

    conn.commit()
    conn.close()


def get_jobs():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jobs ORDER BY id DESC")
    data = cursor.fetchall()

    conn.close()
    return data