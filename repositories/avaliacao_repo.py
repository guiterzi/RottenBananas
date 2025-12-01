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
    
    def listar_questoes_por_filme(self, filmeid):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT Questao.QuestaoId, Questao.Texto
            FROM FilmeQuestao
            JOIN Questao ON FilmeQuestao.QuestaoId = Questao.QuestaoId
            WHERE FilmeQuestao.FilmeId = %s
        """, (filmeid,))
        resultados_query = cur.fetchall()
        cur.close()
        conn.close()

        questoes = []
        for i in resultados_query:
            questoes.append({
                'questaoid': i[0],
                'texto': i[1]
            })
        return questoes
    
    def responder_questao(self, usuarioid, filmeid, questaoid, valor):
        conn = get_connection()
        cur = conn.cursor()
        
        cur.execute("""
            DELETE FROM Resposta
            WHERE UsuarioId = %s AND FilmeId = %s AND QuestaoId = %s
        """, (usuarioid, filmeid, questaoid))
        
        cur.execute("""
            INSERT INTO Resposta (UsuarioId, FilmeId, QuestaoId, Valor)
            VALUES (%s, %s, %s, %s)
        """, (usuarioid, filmeid, questaoid, valor))
        conn.commit()
        cur.close()
        conn.close()

    def listar_questoes_disponiveis(self, filmeid):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT QuestaoId, Texto FROM Questao
            WHERE QuestaoId NOT IN (
                SELECT QuestaoId FROM FilmeQuestao WHERE FilmeId = %s
            )
        """, (filmeid,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [{'questaoid': r[0], 'texto': r[1]} for r in rows]

    def associar_questao_filme(self, filmeid, questaoid):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO FilmeQuestao (FilmeId, QuestaoId) VALUES (%s,%s)", (filmeid, questaoid))
        conn.commit()
        cur.close()
        conn.close()

    def criar_questao(self, texto):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO Questao (Texto) VALUES (%s) RETURNING QuestaoId", (texto,))
        questaoid = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return questaoid

    def remover_questao_filme(self, filmeid, questaoid):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM FilmeQuestao WHERE FilmeId=%s AND QuestaoId=%s", (filmeid, questaoid))
        conn.commit()
        cur.close()
        conn.close()

    def deletar_questao(self, questao_id):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            DELETE FROM FilmeQuestao
            WHERE QuestaoId = %s
        """, (questao_id,))

        cur.execute("""
            DELETE FROM Resposta
            WHERE QuestaoId = %s
        """, (questao_id,))

        cur.execute("""
            DELETE FROM Questao
            WHERE QuestaoId = %s
        """, (questao_id,))

        conn.commit()
        cur.close()
        conn.close()
