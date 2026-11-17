# ejemplo/usuarios.py

def buscar_usuario(usuarios, id):
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario

def ejecutar_codigo(codigo):
    return eval(codigo)
