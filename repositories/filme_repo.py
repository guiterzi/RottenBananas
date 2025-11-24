from bancodedados import get_connection
class FilmeRepo:
    def list_filmes(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT FilmeId, Nome, Ano, Duracao, Sinopse FROM Filme")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        filmes = []
        for r in rows:
            filmes.append({
                'filmeid': r[0],
                'nome': r[1],
                'ano': r[2],
                'duracao': r[3],
                'sinopse': r[4]
            })
        return filmes

    def get_filme(self, filmeid):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT FilmeId, Nome, Ano, Duracao, Sinopse FROM Filme WHERE FilmeId = %s", (filmeid,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return {
                'filmeid': row[0],
                'nome': row[1],
                'ano': row[2],
                'duracao': row[3],
                'sinopse': row[4]
            }
        return None

    def search_filmes(self, query):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT FilmeId, Nome, Ano, Duracao, Sinopse FROM Filme WHERE LOWER(Nome) LIKE %s", ('%' + query.lower() + '%',))
        rows = cur.fetchall()
        cur.close()
        conn.close()

        filmes = []
        for r in rows:
            filmes.append({
                'filmeid': r[0],
                'nome': r[1],
                'ano': r[2],
                'duracao': r[3],
                'sinopse': r[4]
            })
        return filmes
    
    def melhores_filmes(self, limit=10):
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(f"""
            SELECT filme.filmeid, filme.nome, AVG(avaliacao.nota) AS media
            FROM filme
            JOIN avaliacao ON avaliacao.filmeid = filme.filmeid
            GROUP BY filme.filmeid, filme.nome
            ORDER BY media DESC
            LIMIT {limit}""")
            rows = cur.fetchall()
            cur.close()

            filmes = []
            for r in rows:
                filmes.append({
                    'filmeid': r[0],
                    'nome': r[1],
                    'media': r[2]
                })

            return filmes
