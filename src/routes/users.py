from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db
from models.user import User

api = Blueprint('api_users', __name__)

# <----------------------------------------------------------------->
# LISTAR USUARIOS
@api.route('/users', methods=['GET'])
def all_users():

    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))

    return jsonify({'success': users}), 200

# <----------------------------------------------------------------->
# LISTAR UN USUARIO
@api.route('/users/<int:id>', methods=['GET'])
def single_user(id):

    user = User.query.get(id)

    if not user : return jsonify({'warning':'User not found'}), 400

    return jsonify({'success': user.serialize()}), 200

# <----------------------------------------------------------------->
# BORRAR USUARIO
@api.route('/users/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    
    user = User.query.get(id)

    if not user: return jsonify({'warning: ': 'User not found'})

    user.delete()

    return jsonify({'success: ': 'User deleted'}), 201

# <----------------------------------------------------------------->
# REGISTRAR USUARIO
@api.route('/users/register', methods=['POST'])
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
        return jsonify({"status": 400, "warning": "Rut number is required"}), 400
    elif existRutUser:
        return jsonify({"status": 400, "warning": "Rut number is already taken!"}), 400
    
    #phone_number, unique
    if not phone_number:
        return jsonify({"status": 400, "warning": "Phone number is required"}), 400
    elif existPhoneNumber:
        return jsonify({"status": 400, "warning": "Phone number is already taken!"}), 400

    #email, unique
    if not email: 
        return jsonify({"status": 400, "warning": "Email is required"}), 400
    elif existEmail:
        return jsonify({"status": 400, "warning": "Email is already taken!"}), 400
    

    if not first_name: return jsonify({"status": 400, "warning": "First name is required"}), 400
    if not last_name: return jsonify({"status": 400, "warning": "Last name is required"}), 400
    if not password: return jsonify({"status": 400, "warning": "Password required"}), 400
    if not terms_conditions: return jsonify({"status": 400, "warning": "Terms and Conditions must be accepted"}), 400

    newUser = User()
    newUser.rut_numbers = rut_number
    newUser.first_name = first_name
    newUser.last_name = last_name
    newUser.phone_number = phone_number
    newUser.email = email
    newUser.password = generate_password_hash(password)
    newUser.terms_conditions = terms_conditions

    newUser.save()

    return jsonify({"status": 200,"user": newUser.serialize()}), 200