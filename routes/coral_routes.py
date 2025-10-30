from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from dao.coral_dao import listar_corais, adicionar_coral

coral_bp = Blueprint("corais", __name__)

@coral_bp.route("/corais", methods=["GET"])
@jwt_required()
def listar_corais_route():
    usuario = get_jwt_identity()
    corais = listar_corais()
    return jsonify({
        "user": usuario,
        "corais": corais
    }), 200


@coral_bp.route("/corais", methods=["POST"])
@jwt_required()
def criar_coral():
    usuario = get_jwt_identity()
    dados = request.get_json()
    adicionar_coral(dados)
    return jsonify({
        "message": "Coral adicionado com sucesso!",
        "user": usuario
    }), 201
