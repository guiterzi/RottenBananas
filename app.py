from flask import Flask
from controllers.web import web
from controllers.admin import admin
from controllers.relatorio_controller import relatorio_bp
from services.relatorio_service import RelatorioService

app = Flask(__name__)
app.secret_key = 'chave_super_secreta'
app.register_blueprint(web)
app.register_blueprint(admin)
app.register_blueprint(relatorio_bp)
if __name__=='__main__':
    app.run(debug=True)
