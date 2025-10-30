from flask import Blueprint, request, jsonify
from extensions import db, bcrypt, jwt
from models.usuario import User, TokenBlocklist
from flask_jwt_extended import create_access_token, jwt_required, get_jwt

auth_bp = Blueprint('auth_bp', __name__)

# Registro de usuário (exemplo)
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(username=data['username'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "Usuário registrado com sucesso"}), 201

# Login (exemplo)
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Usuário ou senha incorretos"}), 401

# Validação de tokens revogados
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload.get("jti")
    return TokenBlocklist.query.filter_by(jti=jti).first() is not None
