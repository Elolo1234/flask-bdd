from flask import Flask, jsonify
from extensions import db, bcrypt, jwt

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coralsense.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'troque_essa_chave_para_uma_segura'

    # Inicializa extensões
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Mensagens de erro JWT
    @jwt.unauthorized_loader
    def unauthorized_callback(msg):
        return jsonify({"msg": "Authorization header ausente ou inválido", "detail": msg}), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(msg):
        return jsonify({"msg": "Token inválido", "detail": msg}), 422

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({"msg": "Token expirado"}), 401

    # Registrar blueprints com URLs padronizadas (plural)
    from routes.auth_routes import auth_bp
    from routes.coral_routes import coral_bp
    from routes.pesquisa_routes import pesquisa_bp
    from routes.pesquisador_routes import pesquisador_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')              # /auth/register, /auth/login
    app.register_blueprint(coral_bp, url_prefix='/corais')           # /corais GET/POST
    app.register_blueprint(pesquisa_bp, url_prefix='/pesquisas')     # /pesquisas CRUD
    app.register_blueprint(pesquisador_bp, url_prefix='/pesquisadores') # /pesquisadores CRUD

    # Rota de teste
    @app.route('/')
    def home():
        return jsonify({"msg": "API CoralSense funcionando!"}), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
