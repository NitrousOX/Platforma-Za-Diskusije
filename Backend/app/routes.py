from flask import Blueprint, jsonify
from pymongo import MongoClient
# Import servisa iz Services foldera
from app.Services.loginService import login
from app.Services.registerService import register


# Create a blueprint for your API
api = Blueprint('api', __name__)

# Define a route for the root URL ("/")
@api.route('/')
def hello_world():
    # Define the MongoDB URI
    mongodb_uri = "mongodb://root:password@mongodb:27017"

    # Establish a connection to MongoDB
    client = MongoClient(mongodb_uri)

    # Access the database
    db = client.get_database('mydb')  # Replace 'mydb' with your database name
    return "Hello, World!"



@api.route('/login', methods=['GET'])
def get_data():
    return login()

@api.route('/api/register', methods=['GET'])
def get_data():
    return register()