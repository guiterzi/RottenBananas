from database import get_connection

try:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    result = cur.fetchone()
    print("Conexão OK!", result)
    cur.close()
    conn.close()
except Exception as e:
    print("Erro na conexão:", e)
