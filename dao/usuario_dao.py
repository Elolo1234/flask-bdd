import sqlite3

def salvar_usuario(usuario):
    conn = sqlite3.connect("coralsense.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuarios (nome, email, senha)
        VALUES (?, ?, ?)
    """, (usuario["nome"], usuario["email"], usuario["senha"]))
    conn.commit()
    conn.close()

def buscar_usuario_por_email(email):
    conn = sqlite3.connect("coralsense.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "nome": row[1], "email": row[2], "senha": row[3]}
    return None
