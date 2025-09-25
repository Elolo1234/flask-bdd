import sqlite3
from models.pesquisa import Pesquisa

DB_NAME = "coralsense.db"

class PesquisaDAO:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pesquisa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            objetivo TEXT,
            ano INTEGER,
            local TEXT,
            coral_id INTEGER,
            FOREIGN KEY(coral_id) REFERENCES coral(id) ON DELETE SET NULL
        )
        """)
        self.conn.commit()

    def add(self, pesquisa: Pesquisa):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO pesquisa (titulo, objetivo, ano, local, coral_id)
        VALUES (?, ?, ?, ?, ?)
        """, (pesquisa.titulo, pesquisa.objetivo, pesquisa.ano, pesquisa.local, pesquisa.coral_id))
        self.conn.commit()
        return cursor.lastrowid

    def get(self, pesquisa_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM pesquisa WHERE id=?", (pesquisa_id,))
        row = cursor.fetchone()
        if row:
            return Pesquisa(*row)
        return None

    def update(self, pesquisa: Pesquisa):
        cursor = self.conn.cursor()
        cursor.execute("""
        UPDATE pesquisa SET titulo=?, objetivo=?, ano=?, local=?, coral_id=?
        WHERE id=?
        """, (pesquisa.titulo, pesquisa.objetivo, pesquisa.ano, pesquisa.local, pesquisa.coral_id, pesquisa.id))
        self.conn.commit()

    def delete(self, pesquisa_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM pesquisa WHERE id=?", (pesquisa_id,))
        self.conn.commit()

    def list_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM pesquisa")
        return [Pesquisa(*row) for row in cursor.fetchall()]

    def close(self):
        self.conn.close()
