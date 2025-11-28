class Usuario:
    def __init__(self, usuarioid, nome, login, admin= False):
        self.usuarioid = usuarioid
        self.nome = nome
        self.login = login
        self.admin = admin