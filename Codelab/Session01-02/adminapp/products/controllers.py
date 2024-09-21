import os
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from products.services import ProductService
from products.dtos import ProductDTO

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
def get_products():
    """
    Get all products
    ---
    responses:
        200:
            description: A list of products
            schema:
                type: array
                items:
                    type: object
                    properties:
                        id:
                            type: integer
                        name:
                            type: string
                        price:
                            type: number
                        description:
                            type: string
    """
    products = ProductService.get_all_products()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price, 'description': p.description} for p in products])

@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Get a product by ID
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: ID of the product
    responses:
      200:
        description: A product
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            price:
              type: number
            description:
              type: string
            picture:
              type: string
      404:
        description: Product not found
    """
    product = ProductService.get_product_by_id(product_id)
    if product:
        product_dto = ProductDTO(product.id, product.name, product.price, product.picture, product.description)
        return jsonify(product_dto.to_dict())
    return jsonify({'message': 'Product not found'}), 404

@products_bp.route('/', methods=['POST'])
def create_product():
    """
    Create a new product
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            price:
              type: number
            description:
              type: string
    responses:
      201:
        description: Product created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            price:
              type: number
            description:
              type: string
    """
    data = request.get_json()
    product = ProductService.create_product(data['name'], data['price'], data.get('description'))
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description}), 201

@products_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """
    Update a product
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: ID of the product
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            price:
              type: number
            description:
              type: string
    responses:
      200:
        description: Product updated successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            price:
              type: number
            description:
              type: string
      404:
        description: Product not found
    """
    data = request.get_json()
    product = ProductService.update_product(product_id, data['name'], data['price'], data.get('description'))
    if product:
        return jsonify({'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description})
    return jsonify({'message': 'Product not found'}), 404

@products_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """
    Delete a product
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: ID of the product
    responses:
      200:
        description: Product deleted successfully
      404:
        description: Product not found
    """
    if ProductService.delete_product(product_id):
        return jsonify({'message': 'Product deleted'})
    return jsonify({'message': 'Product not found'}), 404

@products_bp.route('/<int:product_id>/upload_image', methods=['POST'])
def upload_image(product_id):
    """
    Upload an image for a product
    ---
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
        description: ID of the product
      - name: image
        in: formData
        type: file
        required: true
        description: Image file to upload
    responses:
      201:
        description: Image uploaded successfully
      404:
        description: Product not found
    """
    product = ProductService.get_product_by_id(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404

    if 'image' not in request.files:
        return jsonify({'message': 'No image part'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Save the image file path as the picture of the product
        ProductService.update_product_picture(product_id, file_path)

        return jsonify({'message': 'Image uploaded successfully'}), 201

    return jsonify({'message': 'Invalid file type'}), 400

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS