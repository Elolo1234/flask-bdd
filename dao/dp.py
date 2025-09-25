import sqlite3, os

DB_PATH = "dados/coralsense.db"
os.makedirs("dados", exist_ok=True)

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
