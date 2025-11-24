from bancodedados import get_connection
class FilmeRepo:
    def list_filmes(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT FilmeId, Nome, Ano, Duracao, Sinopse FROM Filme")
        resultados_query = cur.fetchall()
        cur.close()
        conn.close()

        filmes = []
        for i in resultados_query:
            filmes.append({
                'filmeid': i[0],
                'nome': i[1],
                'ano': i[2],
                'duracao': i[3],
                'sinopse': i[4]
            })
        return filmes

    def get_filme(self, filmeid):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT FilmeId, Nome, Ano, Duracao, Sinopse FROM Filme WHERE FilmeId = %s", (filmeid,))
        resultados_query = cur.fetchone()
        cur.close()
        conn.close()
        if resultados_query:
            return {
                'filmeid': resultados_query[0],
                'nome': resultados_query[1],
                'ano': resultados_query[2],
                'duracao': resultados_query[3],
                'sinopse': resultados_query[4]
            }
        return None

    def search_filmes(self, query):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT FilmeId, Nome, Ano, Duracao, Sinopse FROM Filme WHERE LOWER(Nome) LIKE %s", ('%' + query.lower() + '%',))
        resultados_query = cur.fetchall()
        cur.close()
        conn.close()

        filmes = []
        for i in resultados_query:
            filmes.append({
                'filmeid': i[0],
                'nome': i[1],
                'ano': i[2],
                'duracao': i[3],
                'sinopse':i[4]
            })
        return filmes
    
    def melhores_filmes(self, limit=10):
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(f"""
            SELECT Filme.FilmeId, Filme.Nome, AVG(Avaliacao.Nota)
            FROM Filme
            JOIN Avaliacao ON Avaliacao.FilmeId = Filme.FilmeId
            GROUP BY Filme.FilmeId, Filme.Nome
            ORDER BY AVG(Avaliacao.Nota) DESC
            LIMIT {limit}
            """)
            resultados_query = cur.fetchall()
            cur.close()

            filmes = []
            for i in resultados_query:
                filmes.append({
                    'filmeid': i[0],
                    'nome': i[1],
                    'media': i[2]
                })

            return filmes
