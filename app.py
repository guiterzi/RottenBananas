from flask import Flask
from controllers.web import web

app = Flask(__name__)
app.secret_key = 'chave_super_secreta'
app.register_blueprint(web)

if __name__=='__main__':
    app.run(debug=True)
