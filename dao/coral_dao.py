import sqlite3
from models.coral import Coral

DB_NAME = "coralsense.db"

class CoralDAO:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS coral (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            especie TEXT NOT NULL,
            nome_popular TEXT,
            extincao TEXT,
            indice_temperatura REAL,
            indice_poluicao REAL
        )
        """)
        self.conn.commit()

    def add(self, coral: Coral):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO coral (especie, nome_popular, extincao, indice_temperatura, indice_poluicao)
        VALUES (?, ?, ?, ?, ?)
        """, (coral.especie, coral.nome_popular, coral.extincao, coral.indice_temperatura, coral.indice_poluicao))
        self.conn.commit()
        return cursor.lastrowid

    def get(self, coral_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM coral WHERE id=?", (coral_id,))
        row = cursor.fetchone()
        if row:
            return Coral(*row)
        return None

    def update(self, coral: Coral):
        cursor = self.conn.cursor()
        cursor.execute("""
        UPDATE coral SET especie=?, nome_popular=?, extincao=?, indice_temperatura=?, indice_poluicao=?
        WHERE id=?
        """, (coral.especie, coral.nome_popular, coral.extincao, coral.indice_temperatura, coral.indice_poluicao, coral.id))
        self.conn.commit()

    def delete(self, coral_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM coral WHERE id=?", (coral_id,))
        self.conn.commit()

    def list_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM coral")
        return [Coral(*row) for row in cursor.fetchall()]

    def close(self):
        self.conn.close()
