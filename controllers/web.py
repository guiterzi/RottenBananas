from flask import Blueprint, render_template, request, redirect, url_for, session
from services.auth_service import AuthService
from services.filme_service import FilmeService
from services.avaliacao_service import AvaliacaoService

web = Blueprint('web', __name__)

auth_service = AuthService()
filme_service = FilmeService()
avaliacao_service = AvaliacaoService()

@web.route('/')
def index():
    return render_template('home.html')

@web.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        nome = request.form['nome']
        login = request.form['login']
        senha = request.form['senha']
        user = auth_service.register(nome, login, senha)

        if user:
            session['usuarioid']=user.usuarioid
            session['nome']=user.nome
            return redirect(url_for('web.index'))
        
    return render_template('register.html')

@web.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        login_val = request.form['login']
        senha = request.form['senha']
        user = auth_service.login(login_val, senha)

        if user:
            session['usuarioid']=user.usuarioid
            session['nome']=user.nome
            return redirect(url_for('web.index'))
        
    return render_template('login.html')

@web.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('web.index'))

@web.route('/filmes')
def filmes():
    filmes = filme_service.list_filmes()
    return render_template('movies.html', filmes=filmes)

@web.route('/filme/<int:filmeid>', methods=['GET','POST'])
def filme_detail(filmeid):
    filme = filme_service.get_filme_detail(filmeid)
    if request.method=='POST' and 'usuarioid' in session:
        nota = int(request.form['nota'])
        comentario = request.form['comentario']
        avaliacao_service.create_avaliacao(session['usuarioid'], filmeid, nota, comentario)
        return redirect(url_for('web.filme_detail', filmeid=filmeid))
    return render_template('movie_detail.html', filme=filme)

@web.route('/perfil')
def perfil():
    usuarioid = session.get('usuarioid')
    avaliacoes = avaliacao_service.list_avaliacoes_por_usuario(usuarioid)
    return render_template('user_profile.html', avaliacoes=avaliacoes)


@web.route('/buscar', methods=['GET'])
def buscar():
    query = request.args.get('q')
    if query:
        filmes = filme_service.search_filmes(query)
    else:
        filmes = []
    return render_template('search.html', filmes=filmes, query=query)

@web.route('/melhores')
def melhores():
    melhores_filmes = filme_service.melhores_filmes(10)
    return render_template('melhores_filmes.html', melhores_filmes=melhores_filmes)