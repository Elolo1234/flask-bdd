import sqlite3

def criar_tabela_usuario():
    conn = sqlite3.connect("coralsense.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT UNIQUE,
            senha TEXT
        )
    """)
    conn.commit()
    conn.close()
