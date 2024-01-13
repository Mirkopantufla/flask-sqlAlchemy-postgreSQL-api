import cloudinary
import cloudinary.uploader
from flask import Blueprint, jsonify, request
from models import db
from models.product import Product
from models.image import Image
from utils.validations import allowed_file
from werkzeug.utils import secure_filename

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

    return jsonify({"product": product.serialize_with_images()}), 200

@api.route('/products/delete/<int:id>', methods=['DELETE'])
def delete_product(id):

    product = Product.query.get(id)

    if not product: return jsonify({"warning": "Producto buscado inexistente"}), 400

    return jsonify({"Single product": "Producto Eliminado"}), 200

@api.route('/products/find/categories', methods=['GET'])
def get_find_categories():

    # En este caso, de todos los productos, extraigo cada uno de ellos sin repetir y los guardo en categories.
    categories = Product.query.distinct(Product.category)
    categories = list(map(lambda product: product.category, categories))

    print(categories)

    return jsonify(categories), 200


@api.route('/products/add', methods=['POST'])
def add_product():

    title = request.form['title']
    price = request.form['price']
    description = request.form['description']
    category = request.form['category']
    dataCloudinary = []
    images_data = []
    images = None

    # Valido que los campos no vengan vacios
    if not title: return jsonify({"warning": "El titulo es requerido!"}), 400
    if not price: return jsonify({"warning": "Precio requerido!"}), 400
    if not description: return jsonify({"warning": "Descripcion requerida!"}), 400
    if not category: return jsonify({"warning": "Categoria requerida!"}), 400
    if not 'images' in request.files:
        return jsonify({"warning": "Debes subir almenos una imagen!"}), 400
    
    # Creo una lista con todos los archivos que vengan de front
    images = request.files.getlist('images')
    
    # Valido si realmente vienen imagenes validas
    for image in images:

        if (image.filename == ''):
            return jsonify({"warning": "All images must have a name"}), 400
        elif (not allowed_file(image.filename)):
            return jsonify({"warning": "Files must be format .jpg, .jpeg, .png"}), 400
        
    # Creo el producto para poder guardar las imagenes con el id del producto
    new_product = Product()
    new_product.title = title
    new_product.price = price
    new_product.description = description
    new_product.category = category
    new_product.save()
        
    for index, image in enumerate(images):
        if image and allowed_file(image.filename):
            dataCloudinary.append(cloudinary.uploader.upload(image, folder="fakeStore"))
            if dataCloudinary:
                new_image = Image()
                new_image.src_imagen = dataCloudinary[index]['url']
                new_image.id_publico = dataCloudinary[index]['public_id']
                new_image.activo = True
                new_image.product_id = new_product.product_id
                new_image.save()

                images_data.append({"id_image": new_image.image_id, "url" : dataCloudinary[index]['url']})

    return jsonify({"images_info": images_data, "new_product": new_product.serialize()}), 200



# Metodo para eliminar varias imagenes de cloudinary
# public_ids = ["cld-sample-5", "cld-sample-4", "cld-sample-3", "cld-sample-2", "cld-sample", "sample"]
# image_delete_result = cloudinary.api.delete_resources(public_ids, resource_type="image", type="upload")
# print(image_delete_result)