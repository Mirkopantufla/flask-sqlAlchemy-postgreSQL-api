import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import db

from models.cart import Cart
from models.commune import Comunne
from models.image import Image
from models.product import Product
from models.region import Region
from models.role import Role
from models.shipDetail import ShipDetail
from models.user import User

from dotenv import load_dotenv

from routes.auth import api as api_auth
from routes.users import api as api_users
from routes.products import api as api_products

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

db.init_app(app)
Migrate(app, db)
jwt = JWTManager(app)
CORS(app)

app.register_blueprint(api_auth, url_prefix="/api")
app.register_blueprint(api_users, url_prefix="/api")
app.register_blueprint(api_products, url_prefix="/api")

if __name__ == '__main__':
    app.run()