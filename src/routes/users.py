from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db
from models.user import User

api = Blueprint('api_users', __name__)

@api.route('/register', methods=['POST'])
def user_register():
    
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))

    return jsonify(users), 200
