import cloudinary
import cloudinary.uploader
from flask import Blueprint, jsonify, request
from models import db
from models.product import Product
from models.image import Image
from utils.validations import allowed_file
from werkzeug.utils import secure_filename

api = Blueprint('api_products', __name__)

# ---------------------- /PRODUCTS [GET] ----------------------
@api.route('/products', methods=['GET'])
def all_products():

    products = Product.query.all()
    products = list(map(lambda product: product.serialize_with_images(), products))

    return jsonify(products), 200

# ---------------------- /PRODUCTS/<int:id> [GET] ----------------------
@api.route('/products/<int:id>', methods=['GET'])
def single_product(id):

    product = Product.query.get(id)
    
    if not product: return jsonify({"warning": "Product not found"}), 400

    return jsonify({"success": "Founded product", "product": product.serialize_with_images()}), 200

# ---------------------- /PRODUCTS/DELETE/<int:id> [DELETE] ----------------------
@api.route('/products/delete/<int:id>', methods=['DELETE'])
def delete_product(id):

    product = Product.query.get(id)

    if not product: return jsonify({"warning": "Product not found"}), 400

    return jsonify({"success": "Deleted Product"}), 200

# ---------------------- /PRODUCTS/CATEGORIES [GET] ----------------------
@api.route('/products/categories', methods=['GET'])
def get_find_categories():

    # En este caso, de todos los productos, extraigo cada uno de ellos sin repetir y los guardo en categories.
    categories = Product.query.distinct(Product.category)
    categories = list(map(lambda product: product.category, categories))

    return jsonify(categories), 200

# ---------------------- /PRODUCTS/ADD [POST] ----------------------
@api.route('/products/add', methods=['POST'])
def add_product():

    title = request.form.get('title')
    price = request.form.get('price')
    description = request.form.get('description')
    category = request.form.get('category')
    dataCloudinary = []
    images_data = []
    images = None

    # Valido que los campos no vengan vacios
    if not title: return jsonify({"warning": "El titulo es requerido"}), 400
    if not price: return jsonify({"warning": "Precio requerido"}), 400
    if not description: return jsonify({"warning": "Descripcion requerida"}), 400
    if not category: return jsonify({"warning": "Categoria requerida"}), 400

    if not 'images' in request.files: 
        return jsonify({"warning": "The image is required"}), 400
    else: 
        images = request.files.getlist('images')
    
    # Valido si realmente vienen imagenes validas
    for image in images:
        if (image.filename == ''):
            return jsonify({"warning": "All images must have a name."}), 400
        elif (not allowed_file(image.filename)):
            return jsonify({"warning": "Files must be format .jpg, .jpeg, .png"}), 400
    
    # Creo el producto, para posteriormente, guardar las imagenes con el id del producto creado
    new_product = Product()
    new_product.title = title
    new_product.price = price
    new_product.description = description
    new_product.category = category
    new_product.save()
        
    
    # Recorro la lista de imagenes
    # Por cada iteracion, si fue subida correctamente a cloudinary, se guardara la informacion en la db con el producto asociado.
    for index, image in enumerate(images):
        dataCloudinary.append(cloudinary.uploader.upload(image, folder="fakeStore"))
        if dataCloudinary:
            new_image = Image()
            new_image.src_imagen = dataCloudinary[index]['url']
            new_image.id_publico = dataCloudinary[index]['public_id']
            new_image.activo = True
            new_image.product_id = new_product.product_id
            new_image.save()

            images_data.append({"id_image": new_image.image_id, "url" : dataCloudinary[index]['url']})

    return jsonify({"success": "Has añadido un producto", "images_info": images_data, "new_product": new_product.serialize()}), 200



# Metodo para eliminar varias imagenes de cloudinary
# public_ids = ["cld-sample-5", "cld-sample-4", "cld-sample-3", "cld-sample-2", "cld-sample", "sample"]
# image_delete_result = cloudinary.api.delete_resources(public_ids, resource_type="image", type="upload")
# print(image_delete_result)