from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.user_service import UserService
from app.utils.validators import validate_input

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    is_valid, msg = validate_input(data, ["username", "password", "email", "nama"])
    if not is_valid:
        return jsonify({"message": msg}), 400
    
    response, status_code = UserService.register(data)
    return jsonify(response), status_code

@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    is_valid, msg = validate_input(data, ["username", "password"])
    if not is_valid:
        return jsonify({"message": msg}), 400
    
    response, status_code = UserService.login(data)
    return jsonify(response), status_code

@users_bp.route('', methods=['GET'])
@jwt_required()
def get_users():
    response, status_code = UserService.get_all()
    return jsonify(response), status_code

@users_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    data = request.get_json()
    response, status_code = UserService.update(id, data)
    return jsonify(response), status_code

@users_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    response, status_code = UserService.delete(id)
    return jsonify(response), status_code