
from flask_sockets import Sockets
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)

    sockets = Sockets(app)  # Attach Flask-Sockets

    # Connect to the database
    load_dotenv()
    mongodb_uri = os.getenv("DATABASE_URL")
    try:
        client = MongoClient(mongodb_uri, serverSelectionTimeoutMS=5000)
        client.admin.command("ping")
        db = client["DRS_DB"]
        app.db = db
        print("Successfully connected to MongoDB!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        app.db = None

    # Register REST routes
    from .routes import api
    app.register_blueprint(api)

    # Register WebSocket routes
    from .websocket_routes import sockets, ws_blueprint
    sockets.register_blueprint(ws_blueprint)

    return app

