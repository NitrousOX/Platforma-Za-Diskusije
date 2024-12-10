from flask import Blueprint, jsonify, request, current_app
from pymongo import MongoClient
# Import servisa iz Services foldera
from app.Services.loginService import login
from app.Services.registerService import register, unregister


# Create a blueprint for your API
api = Blueprint('api', __name__)

# Define a route for the root URL ("/")
@api.route('/')
def hello_world():
    return "Hello, World!"


# Route for login
@api.route('/api/login', methods=['POST'])
def login_user():
    # Dobijanje podataka iz POST zahteva
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Poziv servisa za prijavu
    response = login(username, password)
    return jsonify(response)

# Route for logout
@api.route('/api/logout', methods=['GET'])
def test_logout():
    # Poziv metode iz loginService
    response = logout()
    return jsonify(response)

# Route for register
@api.route('/api/register', methods=['POST'])
def register_user():
    # Dobijanje podataka iz POST zahteva
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Poziv servisa za registraciju
    response = register(username, password)
    return jsonify(response)

# Route for unregister
@api.route('/api/unregister', methods=['GET'])
def test_unregister():
    # Poziv metode iz registerService
    response = unregister()
    return jsonify(response)

@api.route('/api/getAdmin',methods = ['GET'])
def getUser():
    if current_app.db is not None:
        # Example: Query the database
        user_data = current_app.db.Administrators.find_one({"username": "adminUser"})
        user_data['_id'] = str(user_data['_id'])
        print(user_data)
        if user_data:
            return jsonify(user_data), 200
    return jsonify({"error": "No database connection or user not found"}), 500