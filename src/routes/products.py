from flask import Blueprint, jsonify, request
from models import db
from models.product import Product

api = Blueprint('api_products', __name__)

@api.route('/products', methods=['GET'])
def all_products():

    products = Product.query.all()
    products = list(map(lambda product: product.serialize(), products))

    return jsonify({"Productos": products}), 200

@api.route('/products/<int:id>', methods=['GET'])
def single_product(id):

    product = Product.query.get(id)
    
    if not product: return jsonify({"warning": "Producto inexistente"}), 400

    return jsonify({"Product" : product.serialize()}), 200

@api.route('/products/delete/<int:id>', methods=['DELETE'])
def delete_product(id):

    product = Product.query.get(id)

    if not product: return jsonify({"warning": "Producto buscado inexistente"}), 400

    return jsonify({"Single product": "Producto Eliminado"}), 200

# @api.route('/products/add', methods='[POST]')
# def add_product():

#     newProduct = Product()
#     newProduct.title
#     newProduct.price
#     newProduct.description
#     newProduct.category
#     newProduct.image_id
#     newProduct.rating

    