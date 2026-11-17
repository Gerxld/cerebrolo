def email_valido(email):
    return "@" in email and "." in email.split("@")[-1]

def crear_usuario(nombre, email):
    if not nombre.strip():
        raise ValueError("Nombre obligatorio")
    if not email_valido(email):
        raise ValueError("Email inválido")
    return {"nombre": nombre.strip(), "email": email.lower()}
