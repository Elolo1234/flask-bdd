from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from extensions import db
from models.pesquisador import Pesquisador

pesquisador_bp = Blueprint('pesquisador', __name__)

@pesquisador_bp.route('/', methods=['GET'])
@jwt_required()
def listar_pesquisadores():
    pesquisadores = Pesquisador.query.all()
    return jsonify([{"id": p.id, "nome": p.nome, "area": p.area} for p in pesquisadores]), 200

@pesquisador_bp.route('/', methods=['POST'])
@jwt_required()
def criar_pesquisador():
    data = request.get_json()
    novo_pesquisador = Pesquisador(nome=data.get('nome'), area=data.get('area'))
    db.session.add(novo_pesquisador)
    db.session.commit()
    return jsonify({"msg": "Pesquisador criado com sucesso"}), 201

@pesquisador_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def obter_pesquisador(id):
    pesquisador = Pesquisador.query.get(id)
    if not pesquisador:
        return jsonify({"msg": "Pesquisador não encontrado"}), 404
    return jsonify({"id": pesquisador.id, "nome": pesquisador.nome, "area": pesquisador.area}), 200

@pesquisador_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def atualizar_pesquisador(id):
    pesquisador = Pesquisador.query.get(id)
    if not pesquisador:
        return jsonify({"msg": "Pesquisador não encontrado"}), 404
    data = request.get_json()
    pesquisador.nome = data.get('nome', pesquisador.nome)
    pesquisador.area = data.get('area', pesquisador.area)
    db.session.commit()
    return jsonify({"msg": "Pesquisador atualizado com sucesso"}), 200

@pesquisador_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def deletar_pesquisador(id):
    pesquisador = Pesquisador.query.get(id)
    if not pesquisador:
        return jsonify({"msg": "Pesquisador não encontrado"}), 404
    db.session.delete(pesquisador)
    db.session.commit()
    return jsonify({"msg": "Pesquisador excluído com sucesso"}), 200
