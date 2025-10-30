# dao/pesquisador_dao.py
import sqlite3

DB_NAME = "coralsense.db"

def listar_pesquisadores():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, area FROM pesquisadores")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "nome": r[1], "area": r[2]} for r in rows]

def adicionar_pesquisador(dados):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pesquisadores (nome, area) VALUES (?, ?)",
                   (dados.get("nome"), dados.get("area")))
    conn.commit()
    conn.close()
