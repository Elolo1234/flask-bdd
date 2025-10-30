import sqlite3

DB_NAME = "coralsense.db"

def listar_corais():
    """Retorna todos os corais cadastrados."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM corais")
    corais = cursor.fetchall()
    conn.close()
    return [{"id": c[0], "nome": c[1], "local": c[2]} for c in corais]


def adicionar_coral(dados):
    """Adiciona um novo coral ao banco."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO corais (nome, local) VALUES (?, ?)",
        (dados["nome"], dados["local"])
    )
    conn.commit()
    conn.close()
