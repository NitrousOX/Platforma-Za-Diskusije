# Simulirana baza korisnika za prijavu
USERS = {
    "admin": {"password": "admin", "admin": True},  # admin has admin role
    "korisnik1": {"password": "korisnik1", "admin": False}  # korisnik1 does not have admin role
}

def login(username, password):
    """
    Simulates the login logic.
    Checks if the username and password match a user in the simulated database.
    Also checks the user's role.
    """
    if username in USERS:
        if USERS[username]["password"] == password:
            is_admin = USERS[username]["admin"]
            return {
                "status": "success",
                "message": f"Welcome, {username}!",
                "role": "admin" if is_admin else "user"
            }
        else:
            return {"status": "error", "message": "Invalid password"}  # Correct message for wrong password
    else:
        return {"status": "error", "message": "No account found"}  # Correct message for non-existent user
