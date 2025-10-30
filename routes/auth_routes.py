from flask import Blueprint, jsonify, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    unset_jwt_cookies
)
from dao.usuario_dao import salvar_usuario, buscar_usuario_por_email

auth_bp = Blueprint("auth", __name__)
bcrypt = Bcrypt()

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    senha_hash = bcrypt.generate_password_hash(data["senha"]).decode("utf-8")

    novo_usuario = {
        "nome": data["nome"],
        "email": data["email"],
        "senha": senha_hash
    }
    salvar_usuario(novo_usuario)
    return jsonify({"message": "Usuário criado com sucesso!"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    usuario = buscar_usuario_por_email(data["email"])

    if usuario and bcrypt.check_password_hash(usuario["senha"], data["senha"]):
        token = create_access_token(identity=usuario["email"])
        return jsonify({
            "message": "Login realizado com sucesso!",
            "access_token": token
        }), 200
    else:
        return jsonify({"message": "Usuário ou senha incorretos!"}), 401


@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    resp = jsonify({"message": "Logout realizado!"})
    unset_jwt_cookies(resp)
    return resp, 200
