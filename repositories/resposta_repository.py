import psycopg2

class RespostaRepository:
    def __init__(self, conn_params):
        # conn_params deve ser um dict: host, database, user, password
        self.conn_params = conn_params

    def get_respostas_por_questao(self, filmeid):
        conn = psycopg2.connect(**self.conn_params)
        cur = conn.cursor()
        cur.execute("""
            SELECT q.QuestaoId, q.Texto, r.Valor, COUNT(*) as total
            FROM Resposta r
            JOIN Questao q ON r.QuestaoId = q.QuestaoId
            WHERE r.FilmeId = %s
            GROUP BY q.QuestaoId, q.Texto, r.Valor
            ORDER BY q.QuestaoId
        """, (filmeid,))
        resultados = cur.fetchall()
        cur.close()
        conn.close()

        # Organizar por questão
        questoes = {}
        for qid, texto, valor, total in resultados:
            if qid not in questoes:
                questoes[qid] = {
                    'texto': texto,
                    'respostas': {}
                }
            questoes[qid]['respostas'][valor] = total
        return questoes
