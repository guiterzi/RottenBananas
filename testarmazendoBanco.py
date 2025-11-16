from database import get_connection

conn = get_connection()
cur = conn.cursor()
cur.execute('SELECT current_database();')
print(cur.fetchone())  # Deve imprimir: BancoProjetoFilmes
cur.execute('SELECT * FROM "Usuario" ORDER BY usuario_id ASC;')
print(cur.fetchall())
cur.close()
conn.close()
