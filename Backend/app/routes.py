from flask import Blueprint, jsonify
from pymongo import MongoClient

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

@api.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello, world!', 'status': 'success'})