from database import get_connection

conn = get_connection()
cur = conn.cursor()
cur.execute("SELECT current_database();")
print("Banco atual:", cur.fetchone())

cur.execute("SELECT table_schema, table_name FROM information_schema.tables WHERE table_name='Usuario';")
print("Schemas da tabela Usuario:", cur.fetchall())

cur.execute("SELECT * FROM public.\"Usuario\" ORDER BY usuario_id ASC;")
print("Registros atuais:", cur.fetchall())
