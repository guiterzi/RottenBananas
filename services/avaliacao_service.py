from repositories.avaliacao_repo import AvaliacaoRepo

class AvaliacaoService:
    def __init__(self):
        self.repo = AvaliacaoRepo()

    def create_avaliacao(self, usuarioid, filmeid, nota, comentario):
        self.repo.create_avaliacao(usuarioid, filmeid, nota, comentario)

    def list_avaliacoes_por_filme(self, filmeid):
        return self.repo.list_avaliacoes_por_filme(filmeid)
    
    def list_avaliacoes_por_usuario(self, usuarioid):
        return self.repo.list_avaliacoes_por_usuario(usuarioid)

