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

#################
    def listar_questoes_por_filme(self, filmeid):
        return self.repo.listar_questoes_por_filme(filmeid)

    # Registrar respostas do usuário a questões de um filme
    def responder(self, usuarioid, filmeid, questaoid, valor):
        self.repo.responder_questao(usuarioid, filmeid, questaoid, valor)

    def listar_questoes_disponiveis(self, filmeid):
        return self.repo.listar_questoes_disponiveis(filmeid)

    def associar_questao_filme(self, filmeid, questaoid):
        self.repo.associar_questao_filme(filmeid, questaoid)

    def criar_questao(self, texto):
        return self.repo.criar_questao(texto)

    def remover_questao_filme(self, filmeid, questaoid):
        self.repo.remover_questao_filme(filmeid, questaoid)
