USERS = {
    "admin": "admin", # username: passowrd
    "korisnik1": "korisnik1"
}

def register(username, password):
    """
    Simulacija registracije korisnika.
    Proverava da li korisnicko ime vec postoji
    """
    if username in USERS:
        return {"status": "error", "message": "Username already exists"}
    else:
        USERS[username] = password
        return {"status": "success", "message": f"User {username} successfully registered"}

def unregister():
    """
    Simulacija brisaja korisnickog naloga.
    (Ova funkcija je ostavljena prazna za buduci razvoj)
    """
    return {"status": "success", "message": "Unregister successful"}
