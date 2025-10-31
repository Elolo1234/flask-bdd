from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from extensions import db
from models.pesquisa import Pesquisa

pesquisa_bp = Blueprint('pesquisa', __name__)

@pesquisa_bp.route('/', methods=['GET'])
@jwt_required()
def listar_pesquisas():
    pesquisas = Pesquisa.query.all()
    return jsonify([{"id": p.id, "titulo": p.titulo, "descricao": p.descricao} for p in pesquisas]), 200

@pesquisa_bp.route('/', methods=['POST'])
@jwt_required()
def criar_pesquisa():
    data = request.get_json()
    nova_pesquisa = Pesquisa(titulo=data.get('titulo'), descricao=data.get('descricao'))
    db.session.add(nova_pesquisa)
    db.session.commit()
    return jsonify({"msg": "Pesquisa criada com sucesso"}), 201

@pesquisa_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def obter_pesquisa(id):
    pesquisa = Pesquisa.query.get(id)
    if not pesquisa:
        return jsonify({"msg": "Pesquisa não encontrada"}), 404
    return jsonify({"id": pesquisa.id, "titulo": pesquisa.titulo, "descricao": pesquisa.descricao}), 200

@pesquisa_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def atualizar_pesquisa(id):
    pesquisa = Pesquisa.query.get(id)
    if not pesquisa:
        return jsonify({"msg": "Pesquisa não encontrada"}), 404
    data = request.get_json()
    pesquisa.titulo = data.get('titulo', pesquisa.titulo)
    pesquisa.descricao = data.get('descricao', pesquisa.descricao)
    db.session.commit()
    return jsonify({"msg": "Pesquisa atualizada com sucesso"}), 200

@pesquisa_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def deletar_pesquisa(id):
    pesquisa = Pesquisa.query.get(id)
    if not pesquisa:
        return jsonify({"msg": "Pesquisa não encontrada"}), 404
    db.session.delete(pesquisa)
    db.session.commit()
    return jsonify({"msg": "Pesquisa excluída com sucesso"}), 200
