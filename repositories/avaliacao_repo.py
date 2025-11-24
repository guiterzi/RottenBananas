from bancodedados import get_connection

class AvaliacaoRepo:
    def listar_avaliacoes_por_filme(self, filmeid):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT Avaliacao.UsuarioId, Usuario.Nome, Avaliacao.Nota, Avaliacao.Comentario
            FROM Avaliacao
            JOIN Usuario ON Avaliacao.UsuarioId = Usuario.UsuarioId
            WHERE Avaliacao.FilmeId = %s
        """, (filmeid,))
        resultados_query  = cur.fetchall()
        cur.close()
        conn.close()

        avaliacoes = []
        for i in resultados_query :
            avaliacoes.append({
                'usuarioid': i[0],
                'usuario_nome': i[1],
                'nota': i[2],
                'comentario': i[3]
            })
        return avaliacoes

    def avaliar(self, usuarioid, filmeid, nota, comentario):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            DELETE FROM Avaliacao
            WHERE UsuarioId = %s AND FilmeId = %s
        """, (usuarioid, filmeid))
        cur.execute("""
            INSERT INTO Avaliacao (UsuarioId, FilmeId, Nota, Comentario)
            VALUES (%s, %s, %s, %s)
        """, (usuarioid, filmeid, nota, comentario))
        conn.commit()
        cur.close()
        conn.close()

    def listar_avaliacoes_por_usuario(self, usuarioid):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT Avaliacao.FilmeId, Filme.Nome, Avaliacao.Nota, Avaliacao.Comentario
            FROM Avaliacao
            JOIN Filme ON Avaliacao.FilmeId = Filme.FilmeId
            WHERE Avaliacao.UsuarioId = %s
        """, (usuarioid,))
        resultados_query = cur.fetchall()
        cur.close()
        conn.close()

        avaliacoes = []
        for i in resultados_query :
            avaliacoes.append({
                'filmeid': i[0],
                'filme_nome': i[1],
                'nota': i[2],
                'comentario': i[3]
            })
        return avaliacoes