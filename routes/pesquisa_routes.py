from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from dao.pesquisa_dao import listar_pesquisas, adicionar_pesquisa

pesquisa_bp = Blueprint("pesquisas", __name__)

@pesquisa_bp.route("/pesquisas", methods=["GET"])
@jwt_required()
def listar_pesquisas_route():
    usuario = get_jwt_identity()
    pesquisas = listar_pesquisas()
    return jsonify({
        "user": usuario,
        "pesquisas": pesquisas
    }), 200


@pesquisa_bp.route("/pesquisas", methods=["POST"])
@jwt_required()
def criar_pesquisa():
    usuario = get_jwt_identity()
    dados = request.get_json()
    adicionar_pesquisa(dados)
    return jsonify({
        "message": "Pesquisa cadastrada com sucesso!",
        "user": usuario
    }), 201
