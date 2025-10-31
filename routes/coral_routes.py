from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from extensions import db
from models.coral import Coral

coral_bp = Blueprint('coral_bp', __name__)

@coral_bp.route('/', methods=['GET'])
@jwt_required()
def listar_corais():
    corais = Coral.query.all()
    return jsonify([{"id": c.id, "nome": c.nome} for c in corais]), 200

@coral_bp.route('/', methods=['POST'])
@jwt_required()
def criar_coral():
    if not request.is_json:
        return jsonify({"msg": "Content-Type deve ser application/json"}), 400
    data = request.get_json()
    if 'nome' not in data:
        return jsonify({"msg": "Campo 'nome' obrigatório"}), 400
    novo_coral = Coral(nome=data['nome'])
    db.session.add(novo_coral)
    db.session.commit()
    return jsonify({"msg": "Coral criado com sucesso"}), 201
