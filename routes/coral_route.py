from flask import Blueprint, request, jsonify
from services.coral_service import (
    listar_corais_json,
    adicionar_coral_json,
    buscar_coral_por_id_json,
    salvar_corais_json,
    deletar_coral_por_id_json
)

coral_bp = Blueprint("corais", __name__)

@coral_bp.route("/corais", methods=["GET"])
def listar():
    corais = listar_corais_json()
    return jsonify(corais), 200

@coral_bp.route("/corais", methods=["POST"])
def criar():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "JSON inválido"}), 400

    novo = adicionar_coral_json(dados)
    corais = listar_corais_json()
    salvar_corais_json(corais)
    return jsonify(novo), 201

@coral_bp.route("/corais/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "JSON inválido"}), 400

    coral = buscar_coral_por_id_json(id)
    if not coral:
        return jsonify({"erro": "Coral não encontrado"}), 404

    coral.update(dados)
    corais = listar_corais_json()
    for i in range(len(corais)):
        if corais[i]["id"] == id:
            corais[i] = coral
    salvar_corais_json(corais)
    return jsonify(coral), 200

@coral_bp.route("/corais/<int:id>", methods=["DELETE"])
def deletar(id):
    if deletar_coral_por_id_json(id):
        corais = listar_corais_json()
        salvar_corais_json(corais)
        return jsonify({"mensagem": "Coral deletado com sucesso!"}), 200
    return jsonify({"erro": "Coral não encontrado"}), 404
