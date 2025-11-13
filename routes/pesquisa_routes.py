from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from extensions import db
from models.pesquisa import Pesquisa

pesquisa_bp = Blueprint('pesquisa_bp', __name__)

@pesquisa_bp.route('/', methods=['GET'])
@jwt_required()
def listar_pesquisas():
    pesquisas = Pesquisa.query.all()
    return jsonify([p.to_dict() for p in pesquisas]), 200


@pesquisa_bp.route('/', methods=['POST'])
@jwt_required()
def criar_pesquisa():
    data = request.get_json()

    if not data or 'titulo' not in data:
        return jsonify({"msg": "Campo 'titulo' é obrigatório"}), 400

    nova_pesquisa = Pesquisa(
        titulo=data.get('titulo'),
        objetivo=data.get('objetivo'),
        ano=data.get('ano'),
        local=data.get('local'),
        coral_relacionado=data.get('coral_relacionado')
    )
    db.session.add(nova_pesquisa)
    db.session.commit()
    return jsonify({"msg": "Pesquisa criada com sucesso"}), 201


@pesquisa_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def obter_pesquisa(id):
    pesquisa = Pesquisa.query.get(id)
    if not pesquisa:
        return jsonify({"msg": "Pesquisa não encontrada"}), 404
    return jsonify(pesquisa.to_dict()), 200


@pesquisa_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def atualizar_pesquisa(id):
    pesquisa = Pesquisa.query.get(id)
    if not pesquisa:
        return jsonify({"msg": "Pesquisa não encontrada"}), 404

    data = request.get_json()
    pesquisa.titulo = data.get('titulo', pesquisa.titulo)
    pesquisa.objetivo = data.get('objetivo', pesquisa.objetivo)
    pesquisa.ano = data.get('ano', pesquisa.ano)
    pesquisa.local = data.get('local', pesquisa.local)
    pesquisa.coral_relacionado = data.get('coral_relacionado', pesquisa.coral_relacionado)

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
