# app/app.py

from flask import Flask
from flask_sockets import Sockets  # Import Flask-Sockets
from app.websocket_routes import ws_blueprint  # Import the WebSocket blueprint

app = Flask(__name__)

# Initialize Flask-Sockets
sockets = Sockets(app)

# Register the WebSocket blueprint
app.register_blueprint(ws_blueprint)

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=5000, debug=True)
