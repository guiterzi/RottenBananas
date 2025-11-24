import bancodedados
from models.avaliacao import Avaliacao

# class AvaliacaoRepo:
#     def list_avaliacoes_by_usuario(self, usuarioid):
#         conn = bancodedados.get_connection()
#         cur = conn.cursor()
#         cur.execute("SELECT UsuarioId, FilmeId, Nota, Comentario FROM Avaliacao WHERE UsuarioId=%s", (usuarioid,))
#         rows = cur.fetchall()
#         cur.close()
#         conn.close()
#         avaliacoes = []
#         for r in rows:
#             avaliacoes.append(Avaliacao(r[0], r[1], r[2], r[3]))
#         return avaliacoes


class AvaliacaoRepo:
    def list_avaliacoes_por_usuario(self, usuarioid):
        conn = bancodedados.get_connection()
        cur = conn.cursor()

        # SQL explícito sem alias
        cur.execute("""
            SELECT Avaliacao.FilmeId, Filme.Nome, Avaliacao.Nota, Avaliacao.Comentario
            FROM Avaliacao
            JOIN Filme ON Avaliacao.FilmeId = Filme.FilmeId
            WHERE Avaliacao.UsuarioId = %s
        """, (usuarioid,))

        rows = cur.fetchall()

        cur.close()
        conn.close()

        avaliacoes = []
        for r in rows:
            avaliacoes.append({
                'filmeid': r[0],
                'filme_nome': r[1],
                'nota': r[2],
                'comentario': r[3]
            })

        return avaliacoes


    def list_avaliacoes_by_filme(self, filmeid):
        conn = bancodedados.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT UsuarioId, FilmeId, Nota, Comentario FROM Avaliacao WHERE FilmeId=%s", (filmeid,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        avaliacoes = []
        for r in rows:
            avaliacoes.append(Avaliacao(r[0], r[1], r[2], r[3]))
        return avaliacoes

    def create_avaliacao(self, usuarioid, filmeid, nota, comentario):
        conn = bancodedados.get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO Avaliacao (UsuarioId, FilmeId, Nota, Comentario) VALUES (%s, %s, %s, %s)",
                    (usuarioid, filmeid, nota, comentario))
        conn.commit()
        cur.close()
        conn.close()