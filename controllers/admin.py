from flask import Blueprint, render_template, request, redirect, url_for, session
from services.filme_service import FilmeService
from services.avaliacao_service import AvaliacaoService

admin = Blueprint('admin', __name__, url_prefix='/admin')

filme_service = FilmeService()
avaliacao_service = AvaliacaoService()

def admin_required(f):
    def wrapper(*args, **kwargs):
        if session.get('usuarioid') != 1:
            return redirect(url_for('web.index'))
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper


@admin.route('/favoritos-oscar')
@admin_required
def admin_favoritos_oscar():
    filmes_oscar = filme_service.listar_filmes_oscar()
    todos_filmes = filme_service.listar_filmes()
    # remover filmes já adicionados da lista de seleção
    filmes_disponiveis = [f for f in todos_filmes if f not in filmes_oscar]
    return render_template('admin_favoritos_oscar.html', filmes_oscar=filmes_oscar, todos_filmes=filmes_disponiveis)

@admin.route('/favoritos-oscar/adicionar', methods=['POST'])
@admin_required
def admin_adicionar_favorito():
    filmeid = request.form.get('filmeid')
    filme_service.adicionar_favorito_oscar(filmeid)
    return redirect(url_for('admin.admin_favoritos_oscar'))

@admin.route('/favoritos-oscar/remover/<int:filmeid>')
@admin_required
def admin_remover_favorito(filmeid):
    filme_service.remover_favorito_oscar(filmeid)
    return redirect(url_for('admin.admin_favoritos_oscar'))

@admin.route('/favoritos-oscar/<int:filmeid>/editar-questoes')
@admin_required
def admin_editar_questoes(filmeid):
    filme = filme_service.get_filme_detalhes(filmeid)
    questoes_filme = avaliacao_service.listar_questoes_por_filme(filmeid)
    questoes_disponiveis = avaliacao_service.listar_questoes_disponiveis(filmeid)
    return render_template('admin_editar_questoes.html', filme=filme, questoes_filme=questoes_filme, questoes_disponiveis=questoes_disponiveis)

@admin.route('/favoritos-oscar/<int:filmeid>/adicionar-questao-existente', methods=['POST'])
@admin_required
def admin_adicionar_questao_existente(filmeid):
    questaoid = request.form.get('questaoid')
    avaliacao_service.associar_questao_filme(filmeid, questaoid)
    return redirect(url_for('admin.admin_editar_questoes', filmeid=filmeid))

@admin.route('/favoritos-oscar/<int:filmeid>/criar-questao', methods=['POST'])
@admin_required
def admin_criar_questao(filmeid):
    texto = request.form.get('texto')
    questaoid = avaliacao_service.criar_questao(texto)
    avaliacao_service.associar_questao_filme(filmeid, questaoid)
    return redirect(url_for('admin.admin_editar_questoes', filmeid=filmeid))

@admin.route('/favoritos-oscar/<int:filmeid>/remover-questao/<int:questaoid>')
@admin_required
def admin_remover_questao(filmeid, questaoid):
    avaliacao_service.remover_questao_filme(filmeid, questaoid)
    return redirect(url_for('admin.admin_editar_questoes', filmeid=filmeid))


@admin.route('/favoritos-oscar/<int:filmeid>/salvar-questoes', methods=['POST'])
@admin_required
def admin_salvar_questoes(filmeid):
    questoes_escolhidas = request.form.getlist('questoes')


    questoes_atuais = avaliacao_service.listar_questoes_por_filme(filmeid)
    for q in questoes_atuais:
        avaliacao_service.remover_questao_filme(filmeid, q['questaoid'])

 
    for qid in questoes_escolhidas:
        avaliacao_service.associar_questao_filme(filmeid, qid)

    return redirect(url_for('admin.admin_editar_questoes', filmeid=filmeid))

@admin.route('/questoes/deletar/<int:questaoid>')
@admin_required
def admin_deletar_questao(questaoid):
    avaliacao_service.deletar_questao(questaoid)
    return redirect(request.referrer)
