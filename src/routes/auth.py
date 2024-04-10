from flask import Blueprint, request, jsonify
from models.user import User
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from werkzeug.security import check_password_hash

api = Blueprint('api_auth', __name__)

@api.route('/login', methods=['POST'])
def login():
    
    email = request.json.get('email')
    password = request.json.get('password')
    
    if not email: return jsonify({ "warning": "Email is required!", "status": 400})
    if not password: return jsonify({ "warning": "Password is required!" , "status": 400})
    
    userFound = User.query.filter_by(email=email).first()
    
    if not userFound: return jsonify({ "error": "Incorrect email or password", "status": 401})
    
    if not check_password_hash(userFound.password, password):
        return jsonify({ "error": "Incorrect email or password", "status": 401})
    
    access_token = create_access_token(identity=userFound.user_id)
    
    data = {
        "access_token": access_token,
        "user": userFound.serialize()
    }
    
    return jsonify({"data": data, "status": 200})