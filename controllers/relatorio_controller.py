from flask import Blueprint, render_template, request
from services.relatorio_service import RelatorioService
from repositories.resposta_repository import RespostaRepository
from services.filme_service import FilmeService

relatorio_bp = Blueprint("relatorio", __name__)

resposta_repo = RespostaRepository({
    'host': 'localhost',
    'database': 'BANCOFILMES',
    'user': 'postgres',
    'password': '123456'
})
relatorio_service = RelatorioService(resposta_repo)
filme_service = FilmeService()

@relatorio_bp.route("/relatorio", methods=['GET','POST'])
def relatorio():
    filmeid = request.form.get('filmeid')  # vem do select
    filmes = filme_service.listar_filmes()
    graficos = []
    if filmeid:
        graficos = relatorio_service.gerar_graficos_por_questao(filmeid=int(filmeid))
    return render_template("relatorio.html", filmes=filmes, graficos=graficos, filmeid=filmeid)
