from flask import Blueprint, request, jsonify
from datetime import datetime
from extensions import db, bcrypt, jwt
from models.usuario import User, TokenBlocklist
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt,
    get_jwt_identity
)

auth_bp = Blueprint('auth_bp', __name__)




@auth_bp.route('/register', methods=['POST'])
def register():
    if not request.is_json:
        return jsonify({"msg": "Content-Type deve ser application/json"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "Campos 'username' e 'password' são obrigatórios"}), 400



    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Usuário já existe"}), 400



    user = User(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "Usuário registrado com sucesso"}), 201



@auth_bp.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Content-Type deve ser application/json"}), 400

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "Campos 'username' e 'password' são obrigatórios"}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"msg": "Usuário ou senha incorretos"}), 401

    access_token = create_access_token(identity=str(user.id))
    return jsonify(access_token=access_token), 200



@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]  
    now = datetime.utcnow()
    db.session.add(TokenBlocklist(jti=jti, created_at=now))
    db.session.commit()
    return jsonify({"msg": "Logout realizado. Token invalidado."}), 200



@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload.get("jti")
    token = TokenBlocklist.query.filter_by(jti=jti).first()
    return token is not None



@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    return jsonify({"msg": f"Acesso permitido ao usuário {current_user_id}"}), 200
