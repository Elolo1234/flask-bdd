from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models.coral import Coral

coral_bp = Blueprint('coral', __name__)

@coral_bp.route('/', methods=['GET'])
@jwt_required()
def listar_corais():
    corais = Coral.query.all()
    return jsonify([{"id": c.id, "nome": c.nome} for c in corais]), 200

@coral_bp.route('/', methods=['POST'])
@jwt_required()
def criar_coral():
    data = request.get_json()
    novo_coral = Coral(nome=data['nome'])
    db.session.add(novo_coral)
    db.session.commit()
    return jsonify({"msg": "Coral criado com sucesso"}), 201
