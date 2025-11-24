from repositories.user_repo import UserRepo

class AuthService:
    def __init__(self):
        self.repo = UserRepo()

    def register(self, nome, login, senha):
        return self.repo.create_user(nome, login, senha)

    def login(self, login, senha):
        return self.repo.get_user_by_login_senha(login, senha)