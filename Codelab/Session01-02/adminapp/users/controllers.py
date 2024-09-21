from flask import Blueprint, request, jsonify
from users.services import UserService
from users.dtos import UserDTO

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
def get_users():
    """
    Get all users
    ---
    responses:
      200:
        description: A list of users
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              email:
                type: string
    """
    users = UserService.get_all_users()
    user_dtos = [UserDTO(user.id, user.name, user.email).to_dict() for user in users]
    return jsonify(user_dtos)

@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get a user by ID
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user
    responses:
      200:
        description: A user
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            email:
              type: string
      404:
        description: User not found
    """
    user = UserService.get_user_by_id(user_id)
    if user:
        user_dto = UserDTO(user.id, user.name, user.email)
        return jsonify(user_dto.to_dict())
    return jsonify({'message': 'User not found'}), 404



@users_bp.route('/', methods=['POST'])
def create_user():
    """
    Create a new user
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
            email:
              type: string
    responses:
      201:
        description: User created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            email:
              type: string
      400:
        description: Invalid input
    """
    data = request.get_json()

    # Check if the request has the required fields
    if 'name' not in data or 'email' not in data:
        return jsonify({'message': 'Name and email are required'}), 400

    # Check if the email is already in use
    if UserService.get_user_by_email(data['email']):
        return jsonify({'message': 'Email already in use'}), 400

    # Check if email format is valid
    if not UserService.is_valid_email(data['email']):
        return jsonify({'message': 'Invalid email format'}), 400

    # Check if username length should be between 3 and 50
    if len(data['name']) < 3 or len(data['name']) > 50:
        return jsonify({'message': 'Name should be between 3 and 50 characters'}), 400

    user = UserService.create_user(data['name'], data['email'])
    user_dto = UserDTO(user.id, user.name, user.email)
    return jsonify(user_dto.to_dict()), 201

@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update a user
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
    responses:
      200:
        description: User updated successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            email:
              type: string
      404:
        description: User not found
    """
    data = request.get_json()
    user = UserService.update_user(user_id, data['name'], data['email'])
    if user:
        user_dto = UserDTO(user.id, user.name, user.email)
        return jsonify(user_dto.to_dict())
    return jsonify({'message': 'User not found'}), 404

@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user
    responses:
      200:
        description: User deleted successfully
      404:
        description: User not found
    """
    if UserService.delete_user(user_id):
        return jsonify({'message': 'User deleted'})
    return jsonify({'message': 'User not found'}), 404