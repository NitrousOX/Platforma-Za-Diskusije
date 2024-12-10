from flask import Blueprint, jsonify, request, current_app, Response
from bson.json_util import dumps

# Import servisa iz Services foldera
from app.Services.loginService import login, logout
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
    if current_app.mongo_service is not None:
        admins_json = current_app.mongo_service.get_all("admins")
        return Response(dumps(admins_json), mimetype='application/json'), 200
    return jsonify({"error": "No database connection or user not found"}), 500