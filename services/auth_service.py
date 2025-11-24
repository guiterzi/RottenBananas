from repositories.user_repo import UserRepo

class AuthService:
    def __init__(self):
        self.repo = UserRepo()

    def registrar(self, nome, login, senha):
        return self.repo.criar_usuario(nome, login, senha)

    def login(self, login, senha):
        return self.repo.logar(login, senha)