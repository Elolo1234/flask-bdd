from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from dao.pesquisador_dao import listar_pesquisadores, adicionar_pesquisador

pesquisador_bp = Blueprint("pesquisadores", __name__)

@pesquisador_bp.route("/pesquisadores", methods=["GET"])
@jwt_required()
def listar_pesquisadores_route():
    usuario = get_jwt_identity()
    pesquisadores = listar_pesquisadores()
    return jsonify({
        "user": usuario,
        "pesquisadores": pesquisadores
    }), 200


@pesquisador_bp.route("/pesquisadores", methods=["POST"])
@jwt_required()
def criar_pesquisador():
    usuario = get_jwt_identity()
    dados = request.get_json()
    adicionar_pesquisador(dados)
    return jsonify({
        "message": "Pesquisador cadastrado com sucesso!",
        "user": usuario
    }), 201
