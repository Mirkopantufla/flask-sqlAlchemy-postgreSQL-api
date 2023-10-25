from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db
from models.user import User

api = Blueprint('api_users', __name__)

@api.route('/register', methods=['POST'])
def user_register():

    rut_number = request.json.get('rut_number')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    phone_number = request.json.get('phone_number')
    email = request.json.get('email')
    password = request.json.get('password')
    terms_conditions = request.json.get('terms_conditions')

    existRutUser = User.query.filter_by(rut_numbers = rut_number).first()
    existPhoneNumber = User.query.filter_by(phone_number = phone_number).first()
    existEmail = User.query.filter_by(email = email).first()

    #rut_number, unique
    if not rut_number:
        return jsonify({"warning": "Rut number is required"}), 400
    elif existRutUser:
        return jsonify({"warning": "Rut number is already taken!"}), 400
    
    #phone_number, unique
    if not phone_number:
        return jsonify({"warning": "Phone number is required"}), 400
    elif existPhoneNumber:
        return jsonify({"warning": "Phone number is already taken!"}), 400

    #email, unique
    if not email: 
        return jsonify({"warning": "Email is required"}), 400
    elif existEmail:
        return jsonify({"warning": "Email is already taken!"}), 400
    

    if not first_name: return jsonify({"warning": "First name is required"}), 400
    if not last_name: return jsonify({"warning": "Last name is required"}), 400
    if not password: return jsonify({"warning": "Password required"}), 400
    if not terms_conditions: return jsonify({"warning": "Terms and Conditions must be accepted"}), 400

    newUser = User()
    newUser.rut_numbers = rut_number
    newUser.first_name = first_name
    newUser.last_name = last_name
    newUser.phone_number = phone_number
    newUser.email = email
    newUser.password = generate_password_hash(password)
    newUser.terms_conditions = terms_conditions

    newUser.save()

    return jsonify("Nuevo usuario: ", newUser.serialize()), 200

@api.route('/users', methods=["GET"])
def list_users():

    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))

    return jsonify(users), 200

@api.route('/users/<int:id>', methods=['GET'])
def specific_user(id):

    user = User.query.get(id)

    if not user : return jsonify({'message':'Usuario inexistente'}), 400

    return jsonify(user.serialize()), 200

@api.route('/users/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    
    user = User.query.get(id)

    if not user: return jsonify({'Advertencia: ': 'Usuario inexistente'})

    user.delete()

    return jsonify({'Aceptado: ': 'Usuario Eliminado'}), 201