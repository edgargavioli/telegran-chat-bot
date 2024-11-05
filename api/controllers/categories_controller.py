from flask import Blueprint, jsonify, request, abort
from api.models.categories import Category
from api.models.db import db
from functools import wraps
from app.routes.login import current_user

category_bp = Blueprint('categories', __name__, url_prefix='/api')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return jsonify({'error': 'Unauthorized access'}), 401
        return f(*args, **kwargs)
    return decorated_function

@category_bp.route('/categories', methods=['GET'])
@login_required
def get_categories():
    categories = Category.query.all()
    return jsonify([{'id': category.id, 'name': category.name} for category in categories])

@category_bp.route('/categories/<int:id>', methods=['GET'])
@login_required
def get_category(id):
    category = Category.query.get(id)
    if not category:
        return abort(404, 'Category not found')
    return jsonify({'id': category.id, 'name': category.name})

@category_bp.route('/categories', methods=['POST'])
@login_required
def create_category():
    data = request.get_json()
    new_category = Category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'id': new_category.id, 'name': new_category.name}), 201

@category_bp.route('/categories/<int:id>', methods=['PUT'])
@login_required
def update_category(id):
    category = Category.query.get(id)
    if not category:
        return abort(404, 'Category not found')
    data = request.get_json()
    category.name = data['name']
    db.session.commit()
    return jsonify({'id': category.id, 'name': category.name})

@category_bp.route('/categories/<int:id>', methods=['DELETE'])
@login_required
def delete_category(id):
    category = Category.query.get(id)
    if not category:
        return abort(404, 'Category not found')
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted'})
