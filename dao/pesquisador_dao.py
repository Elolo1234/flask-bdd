import sqlite3
from models.pesquisador import Pesquisador

DB_NAME = "coralsense.db"

class PesquisadorDAO:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pesquisador (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            instituicao TEXT,
            especialidade TEXT,
            email TEXT
        )
        """)
        self.conn.commit()

    def add(self, pesquisador: Pesquisador):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO pesquisador (nome, instituicao, especialidade, email)
        VALUES (?, ?, ?, ?)
        """, (pesquisador.nome, pesquisador.instituicao, pesquisador.especialidade, pesquisador.email))
        self.conn.commit()
        return cursor.lastrowid

    def get(self, pesquisador_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM pesquisador WHERE id=?", (pesquisador_id,))
        row = cursor.fetchone()
        if row:
            return Pesquisador(*row)
        return None

    def update(self, pesquisador: Pesquisador):
        cursor = self.conn.cursor()
        cursor.execute("""
        UPDATE pesquisador SET nome=?, instituicao=?, especialidade=?, email=?
        WHERE id=?
        """, (pesquisador.nome, pesquisador.instituicao, pesquisador.especialidade, pesquisador.email, pesquisador.id))
        self.conn.commit()

    def delete(self, pesquisador_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM pesquisador WHERE id=?", (pesquisador_id,))
        self.conn.commit()

    def list_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM pesquisador")
        return [Pesquisador(*row) for row in cursor.fetchall()]

    def close(self):
        self.conn.close()
