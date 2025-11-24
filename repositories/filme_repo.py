import bancodedados
from models.filme import Filme

class FilmeRepo:
    def list_filmes(self):
        conn = bancodedados.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT FilmeId, Nome, Ano, Duracao, Sinopse FROM Filme ORDER BY Nome")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        filmes = []
        for r in rows:
            filmes.append(Filme(r[0], r[1], r[2], r[3], r[4]))
        return filmes

    def get_filme(self, filmeid):
        conn = bancodedados.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT FilmeId, Nome, Ano, Duracao, Sinopse FROM Filme WHERE FilmeId=%s", (filmeid,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return Filme(row[0], row[1], row[2], row[3], row[4])
        return None

    def search_filmes(self, query):
        conn = bancodedados.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT FilmeId, Nome, Ano, Duracao, Sinopse FROM Filme WHERE LOWER(Nome) LIKE %s ORDER BY Nome",
                    ('%' + query.lower() + '%',))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        filmes = []
        for r in rows:
            filmes.append(Filme(r[0], r[1], r[2], r[3], r[4]))
        return filmes