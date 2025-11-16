from database import get_connection

def inserir_genero(nome):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute = ("""INSERT INTO "Genero" nome
                   VALUES %s
                   RETURNING genero_id""",(nome,))
    genero_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return genero_id