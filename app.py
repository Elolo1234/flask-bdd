from flask import Flask, jsonify
from utils.init_db import init_db
from routes.coral_route import coral_bp
from routes.pesquisa_route import pesquisa_bp
from routes.pesquisador_route import pesquisador_bp

app = Flask(__name__)


init_db()

app.register_blueprint(coral_bp, url_prefix="/corais")
app.register_blueprint(pesquisa_bp, url_prefix="/pesquisas")
app.register_blueprint(pesquisador_bp, url_prefix="/pesquisadores")

@app.before_first_request
def start():
    init_db() 

@app.route('/')
def home():
    return jsonify({"mensagem": "API CoralSense com Flask e SQLite3"})

if __name__ == "__main__":
    app.run(debug=True)
