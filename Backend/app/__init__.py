from flask import Flask
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)

    #Connecting to the database
    load_dotenv()
    mongodb_uri = os.getenv("DATABASE_URL")
    try:
        # Establish MongoDB connection
        client = MongoClient(mongodb_uri, server_api=ServerApi('1'))  # Timeout set to 5 seconds
        # Perform a quick connection check
        client.admin.command('ping')  # This pings the MongoDB server
        db = client["DRS"]  # Get default database
        app.db = db
        print("Successfully connected to MongoDB!")
        print(db)
        
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        app.db = None  # Handle failure by setting db to None

    # Register routes
    from .routes import api
    app.register_blueprint(api)

    return app

