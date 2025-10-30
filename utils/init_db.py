import sqlite3
from models.usuario import criar_tabela_usuario

def get_db_connection():
    conn = sqlite3.connect("coralsense.db")
    return conn

def init_db():
    criar_tabela_usuario()
    print("Banco inicializado com sucesso!")

if __name__ == "__main__":
    init_db()
