from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from datetime import timedelta


from routes.auth_routes import auth_bp
from routes.coral_route import coral_bp
from routes.pesquisa_route import pesquisa_bp
from routes.pesquisador_route import pesquisador_bp

app = Flask(__name__)


app.config["JWT_SECRET_KEY"] = "minha_chave_super_secreta"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)


bcrypt = Bcrypt(app)
jwt = JWTManager(app)


app.register_blueprint(auth_bp)
app.register_blueprint(coral_bp)
app.register_blueprint(pesquisa_bp)
app.register_blueprint(pesquisador_bp)

if __name__ == "__main__":
    app.run(debug=True)
