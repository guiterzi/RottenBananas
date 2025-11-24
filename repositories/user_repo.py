import bancodedados
from models.usuario import Usuario

class UserRepo:
    def create_user(self, nome, login, senha):
        conn = bancodedados.get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Usuario (Nome, Login, Senha) VALUES (%s, %s, %s) RETURNING UsuarioId, Nome, Login",
            (nome, login, senha)
        )
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if row:
            return Usuario(row[0], row[1], row[2])
        return None

    def get_user_by_login_senha(self, login, senha):
        conn = bancodedados.get_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT UsuarioId, Nome, Login FROM Usuario WHERE Login=%s AND Senha=%s",
            (login, senha)
        )
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return Usuario(row[0], row[1], row[2])
        return None