from flask import Blueprint, request, jsonify
from services.pesquisa_service import (
    listar_pesquisas_json,
    adicionar_pesquisa_json,
    atualizar_pesquisa_json,
    deletar_pesquisa_por_id_json
)

pesquisa_bp = Blueprint("pesquisas", __name__)

@pesquisa_bp.route("/pesquisas", methods=["GET"])
def listar():
    pesquisas = listar_pesquisas_json()
    return jsonify(pesquisas), 200

@pesquisa_bp.route("/pesquisas", methods=["POST"])
def criar():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "JSON inválido"}), 400

    novo = adicionar_pesquisa_json(dados)
    return jsonify(novo), 201

@pesquisa_bp.route("/pesquisas/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "JSON inválido"}), 400

    resultado = atualizar_pesquisa_json(id, dados)
    if resultado:
        return jsonify(resultado), 200
    return jsonify({"erro": "Pesquisa não encontrada"}), 404

@pesquisa_bp.route("/pesquisas/<int:id>", methods=["DELETE"])
def deletar(id):
    if deletar_pesquisa_por_id_json(id):
        return jsonify({"mensagem": "Pesquisa deletada com sucesso!"}), 200
    return jsonify({"erro": "Pesquisa não encontrada"}), 404
