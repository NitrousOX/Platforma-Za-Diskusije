from flask import Blueprint, jsonify

# Create a blueprint for your API
api = Blueprint('api', __name__)

# Define a route for the root URL ("/")
@api.route('/')
def hello_world():
    return "Hello, World!"

@api.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello, world!', 'status': 'success'})