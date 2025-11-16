from database import get_connection

def inserir_usuario(nome, login, senha):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO "Usuario" (nome, login, senha)
        VALUES (%s, %s, %s)
        RETURNING usuario_id;
    """, (nome, login, senha))
    usuario_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return usuario_id
