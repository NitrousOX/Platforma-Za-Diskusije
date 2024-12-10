# app/websocket_routes.py

from flask import Blueprint
from flask_sockets import Sockets  # Import Flask-Sockets instead of Flask-SocketIO
import json
from app.Services.loginService import login  # Import the login function

ws_blueprint = Blueprint("ws", __name__)
sockets = Sockets()

# app/websocket_routes.py
@sockets.route('/ws')
def handle_websocket(ws):
    while not ws.closed:
        try:
            message = ws.receive()
            if message:
                data = json.loads(message)
                action = data.get("action")

                if action == "login":
                    username = data.get("username")
                    password = data.get("password")
                    response = login(username, password)  # Call the login service
                else:
                    response = {"status": "error", "message": "Invalid action"}

                # Send response back via WebSocket
                ws.send(json.dumps(response))

        except Exception as e:
            print(f"Error in WebSocket handling: {str(e)}")  # Log error details for debugging
            ws.send(json.dumps({"status": "error", "message": str(e)}))

