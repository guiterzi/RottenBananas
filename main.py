from flask import Flask, request, jsonify, render_template_string
from database import get_connection
from controller.usuario_controller import usuario_bp


app = Flask(__name__)

app.register_blueprint(usuario_bp)
if __name__ == "__main__":
    app.run(debug=True)