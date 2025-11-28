from flask import Flask
from controllers.web import web
from controllers.admin import admin

app = Flask(__name__)
app.secret_key = 'chave_super_secreta'
app.register_blueprint(web)
app.register_blueprint(admin)

if __name__=='__main__':
    app.run(debug=True)
