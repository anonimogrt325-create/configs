from flask import Blueprint, request, jsonify

# Create a blueprint for the app
app_routes = Blueprint('app_routes', __name__)

# Authentication route
@app_routes.route('/auth/login', methods=['POST'])
def login():
    return jsonify({'message': 'Login successful'}), 200

@app_routes.route('/auth/register', methods=['POST'])
def register():
    return jsonify({'message': 'Registration successful'}), 201

# Product listing route
@app_routes.route('/products', methods=['GET'])
def list_products():
    return jsonify([{'id': 1, 'name': 'Product 1'}, {'id': 2, 'name': 'Product 2'}]), 200

# Cart route
@app_routes.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        return jsonify({'message': 'Item added to cart'}), 201
    return jsonify({'message': 'Cart retrieved'}), 200

# Payment route
@app_routes.route('/payment', methods=['POST'])
def payment():
    return jsonify({'message': 'Payment processed'}), 200

