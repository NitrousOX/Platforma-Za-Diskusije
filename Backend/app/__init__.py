
from flask import Flask
from flask_sockets import Sockets
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from app.Services.mongoDBService import MongoDBService
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)

    #sockets = Sockets(app)  # Attach Flask-Sockets

    # Connect to the database
    load_dotenv()
    print(f"MongoDB URI from environment: {os.getenv('DATABASE_URL')}")
    mongodb_uri = os.getenv("DATABASE_URL")
    try:
        # Establish MongoDB connection
        client = MongoClient(mongodb_uri, server_api=ServerApi('1'))  # Timeout set to 5 seconds
        # Perform a quick connection check
        client.admin.command('ping')  # This pings the MongoDB server
        db = client["DRS"]  # Get default database
        app.db = db
        print("Successfully connected to MongoDB!")
        app.mongo_service = MongoDBService(db)

    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        app.db = None

    # Register REST routes
    from .routes import api
    app.register_blueprint(api)

    # Register WebSocket routes
    # from .websocket_routes import sockets, ws_blueprint
    # sockets.register_blueprint(ws_blueprint)

    return app

