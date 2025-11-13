from flask import Flask, jsonify
from datetime import timedelta
from extensions import db, bcrypt, jwt

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coralsense.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'troque_essa_chave_para_uma_segura'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=2)  # Token dura 2h

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    @jwt.unauthorized_loader
    def unauthorized_callback(msg):
        return jsonify({"msg": "Authorization header ausente ou inválido", "detail": msg}), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(msg):
        return jsonify({"msg": "Token inválido", "detail": msg}), 422

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({"msg": "Token expirado"}), 401

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return jsonify({"msg": "Token inválido ou já foi utilizado"}), 401

    from routes.auth_routes import auth_bp
    from routes.coral_routes import coral_bp
    from routes.pesquisa_routes import pesquisa_bp
    from routes.pesquisador_routes import pesquisador_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(coral_bp, url_prefix='/corais')
    app.register_blueprint(pesquisa_bp, url_prefix='/pesquisas')
    app.register_blueprint(pesquisador_bp, url_prefix='/pesquisadores')

    @app.route('/')
    def home():
        return jsonify({"msg": "API CoralSense funcionando!!"}), 200

    return app


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        from models.usuario import User, TokenBlocklist, Pesquisador
        from models.coral import Coral
        from models.pesquisa import Pesquisa
        db.create_all()
        print("✅ Banco de dados e tabelas criadas (se ainda não existiam).")

    print("Rotas registradas:")
    print(app.url_map)

    app.run(debug=True)
