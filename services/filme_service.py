from repositories.filme_repo import FilmeRepo
from repositories.avaliacao_repo import AvaliacaoRepo

class FilmeService:
    def __init__(self):
        self.repo = FilmeRepo()
        self.av_repo = AvaliacaoRepo()

    def listar_filmes(self):
        filmes = self.repo.listar_filmes()
        for f in filmes:
            avals = self.av_repo.listar_avaliacoes_por_filme(f['filmeid'])
            if avals:
                f['rating'] = sum(a['nota'] for a in avals)/len(avals)
                f['rating_count'] = len(avals)
                f['reviews'] = avals
            else:
                f['rating'] = None
                f['rating_count'] = 0
                f['reviews'] = []
        return filmes

    def get_filme_detalhes(self, filmeid):
        f = self.repo.get_filme(filmeid)
        if f:
            avals = self.av_repo.listar_avaliacoes_por_filme(f['filmeid'])
            f['reviews'] = avals
            if avals:
                f['rating'] = sum(a['nota'] for a in avals)/len(avals)
                f['rating_count'] = len(avals)
            else:
                f['rating'] = None
                f['rating_count'] = 0
        return f

    def buscar_filmes(self, query):
        filmes = self.repo.buscar_filmes(query)
        for f in filmes:
            avals = self.av_repo.listar_avaliacoes_por_filme(f['filmeid'])
            if avals:
                f['rating'] = sum(a['nota'] for a in avals)/len(avals)
                f['rating_count'] = len(avals)
                f['reviews'] = avals
            else:
                f['rating'] = None
                f['rating_count'] = 0
                f['reviews'] = []
        return filmes
    

    def melhores_filmes(self,limit=10):
        return self.repo.melhores_filmes(limit)
    
    def listar_filmes_oscar(self):
        filmes = self.repo.listar_filmes_oscar()
        for f in filmes:
            avals = self.av_repo.listar_avaliacoes_por_filme(f['filmeid'])
            if avals:
                f['rating'] = sum(a['nota'] for a in avals)/len(avals)
                f['rating_count'] = len(avals)
                f['reviews'] = avals
            else:
                f['rating'] = None
                f['rating_count'] = 0
                f['reviews'] = []
        return filmes
    def adicionar_favorito_oscar(self, filmeid):
        self.repo.adicionar_favorito_oscar(filmeid)

    def remover_favorito_oscar(self, filmeid):
        self.repo.remover_favorito_oscar(filmeid)

