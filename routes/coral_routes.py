from flask import Blueprint, jsonify, request
from extensions import db
from flask_jwt_extended import jwt_required
from models.coral import Coral 

coral_bp = Blueprint('coral_bp', __name__)

@coral_bp.route('/', methods=['GET'])
@jwt_required()
def listar_corais():
    corais = Coral.query.all()
    return jsonify([c.to_dict() for c in corais]), 200

@coral_bp.route('/', methods=['POST'])
@jwt_required()
def criar_coral():
    data = request.get_json()
    novo_coral = Coral(
        nome=data['nome'],
        localizacao=data['localizacao'],
        especie=data['especie']
    )
    db.session.add(novo_coral)
    db.session.commit()
    return jsonify({"msg": "Coral cadastrado com sucesso"}), 201
