
# Simulirana baza korisnika za prijavu
USERS = {
    "admin": "admin", # username: password
    "korisnik1": "korisnik1"
}


def login(username, password):
    """
    Simulacija login logike.
    Proverava da li korisnicko ime i lozinka odgovaraju nekom korisniku.
    """
    if username in USERS and USERS[username] == password:
        return {"status": "success", "message": f"Welcome, {username}!"}
    else:
        return {"status": "error", "message": "Invalid username or password"}

    return {"message": "Login successful"}

def logout():
    """
    Simulacija odjavljivanja
    """
    return {"status": "success", "message": "Logout successful"}
