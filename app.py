from flask import Flask
from extensions import db, bcrypt, jwt

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coralsense.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'chave_super_secreta_mude_esta'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 1h

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Blueprints
    from routes.auth_routes import auth_bp
    from routes.coral_routes import coral_bp
    from routes.pesquisa_routes import pesquisa_bp
    from routes.pesquisador_routes import pesquisador_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(coral_bp, url_prefix="/coral")
    app.register_blueprint(pesquisa_bp, url_prefix="/pesquisa")
    app.register_blueprint(pesquisador_bp, url_prefix="/pesquisador")

    # Criar tabelas
    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        return {"msg": "API CoralSense com autenticação JWT ativa"}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
