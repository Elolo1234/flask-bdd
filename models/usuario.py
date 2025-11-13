from datetime import datetime
from extensions import db, bcrypt


# ==========================================================
# 🧱 Tabela de tokens invalidados (para logout)
# ==========================================================
class TokenBlocklist(db.Model):
    __tablename__ = "token_blocklist"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<TokenBlocklist jti={self.jti}>"


# ==========================================================
# 👩‍🔬 Modelo Pesquisador (CRUD protegido)
# ==========================================================
class Pesquisador(db.Model):
    __tablename__ = "pesquisadores"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    area = db.Column(db.String(200), nullable=True)

    def __init__(self, nome, area=None):
        self.nome = nome
        self.area = area

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "area": self.area
        }

    def __repr__(self):
        return f"<Pesquisador nome={self.nome} area={self.area}>"


# ==========================================================
# 👤 Modelo de Usuário (autenticação)
# ==========================================================
class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    # ---------- Métodos de segurança ----------
    def set_password(self, password):
        """Criptografa e armazena a senha."""
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password):
        """Compara senha digitada com o hash salvo."""
        return bcrypt.check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }

    def __repr__(self):
        return f"<User username={self.username}>"
