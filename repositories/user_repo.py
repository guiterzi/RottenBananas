import bancodedados
from models.usuario import Usuario

class UserRepo:
    def criar_usuario(self, nome, login, senha):
        conn = bancodedados.get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Usuario (Nome, Login, Senha) VALUES (%s, %s, %s) RETURNING UsuarioId, Nome, Login",
            (nome, login, senha)
        )
        resultados_query = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if resultados_query:
            return Usuario(resultados_query[0], resultados_query[1], resultados_query[2])
        return None

    def logar(self, login, senha):
        conn = bancodedados.get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT UsuarioId, Nome, Login FROM Usuario WHERE Login=%s AND Senha=%s",
            (login, senha)
        )
        resultados_query = cur.fetchone()
        cur.close()
        conn.close()
        if resultados_query:
            return Usuario(resultados_query[0], resultados_query[1], resultados_query[2])
        return None