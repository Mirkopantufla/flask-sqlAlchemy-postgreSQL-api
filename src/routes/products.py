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

    return jsonify(product.serialize()), 200

@api.route('/products/delete/<int:id>', methods=['DELETE'])
def delete_product(id):

    product = Product.query.get(id)

    if not product: return jsonify({"warning": "Producto buscado inexistente"}), 400

    return jsonify({"Single product": "Producto Eliminado"}), 200

@api.route('/products/add', methods=['POST'])
def add_product():

    title = request.form['title']
    price = request.form['price']
    description = request.form['description']
    category = request.form['category']
    rating = request.form['rating']

    imagen = None

    if not title: return jsonify({"advertencia": "El titulo es requerido!"}), 400
    if not price: return jsonify({"advertencia": "Precio requerido!"}), 400
    if not description: return jsonify({"advertencia": "Descripcion requerida!"}), 400
    if not category: return jsonify({"advertencia": "Categoria requerida!"}), 400
    
    if not 'imagen' in request.files: 
        return jsonify({"advertencia": "La imagen es requerida!"}), 400
    else:
        imagen = request.files['imagen']

    newProduct = Product()
    newProduct.title = title
    newProduct.price = price
    newProduct.description = description
    newProduct.category = category
    newProduct.rating = rating

    