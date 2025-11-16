# def inserir_usuario(nome, login, senha):
#     # Regras de negócio podem ser aplicadas aqui
#     # Ex: validar duplicidade, tamanho da senha, etc.

#     usuario_id = inserir_usuario(nome, login, senha)
#     return usuario_id

from repositories.usuario_repository import inserir_usuario

def criar_usuario_service(nome, login, senha):
    return inserir_usuario(nome, login, senha)
