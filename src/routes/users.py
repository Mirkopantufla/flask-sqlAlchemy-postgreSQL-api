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
    register_date = request.json.get('register_date')
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))

    return jsonify(users), 200
