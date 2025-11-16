from flask import Blueprint, request, render_template
from services.usuario_service import criar_usuario_service

usuario_bp = Blueprint("usuario", __name__)

# Rota para mostrar o formulário
@usuario_bp.route("/", methods=["GET"])
def form_usuario_controller():
    return render_template("form_usuario.html")  # procura em templates/

# Rota para processar o POST
@usuario_bp.route("/usuarios", methods=["POST"])
def criar_usuario_controller():
    nome = request.form.get("nome")
    login = request.form.get("login")
    senha = request.form.get("senha")

    usuario_id = criar_usuario_service(nome, login, senha)
    return f"Usuário criado com ID: {usuario_id}"
