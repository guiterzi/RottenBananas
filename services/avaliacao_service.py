from repositories.avaliacao_repo import AvaliacaoRepo

class AvaliacaoService:
    def __init__(self):
        self.repo = AvaliacaoRepo()

    def avaliar(self, usuarioid, filmeid, nota, comentario):
        self.repo.avaliar(usuarioid, filmeid, nota, comentario)

    def listar_avaliacoes_por_filme(self, filmeid):
        return self.repo.listar_avaliacoes_por_filme(filmeid)
    
    def listar_avaliacoes_por_usuario(self, usuarioid):
        return self.repo.listar_avaliacoes_por_usuario(usuarioid)

