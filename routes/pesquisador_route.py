from flask import Blueprint, request, jsonify
from services.pesquisador_service import *

pesquisador_bp = Blueprint("pesquisadores", __name__)

@pesquisador_bp.route("/pesquisadores", methods=["GET"])
def listar():
    return jsonify(listar_pesquisadores_json()), 200

@pesquisador_bp.route("/pesquisadores", methods=["POST"])
def criar():
    dados = request.json
    novo = adicionar_pesquisador_json(dados)
    return jsonify(novo), 201

@pesquisador_bp.route("/pesquisadores/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.json
    atualizado = atualizar_pesquisador_json(id, dados)
    if atualizado:
        return jsonify(atualizado), 200
    return jsonify({"erro": "Pesquisador não encontrado"}), 404

@pesquisador_bp.route("/pesquisadores/<int:id>", methods=["DELETE"])
def deletar(id):
    if deletar_pesquisador_por_id_json(id):
        return jsonify({"mensagem": "Pesquisador deletado com sucesso!"}), 200
    return jsonify({"erro": "Pesquisador não encontrado"}), 404