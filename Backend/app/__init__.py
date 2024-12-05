from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config.from_pyfile('config.py', silent=True)

    # Register routes
    from .routes import api
    app.register_blueprint(api)

    return app

