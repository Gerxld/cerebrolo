def crear_curso(codigo, nombre):
    if not codigo.strip():
        raise ValueError("Código obligatorio")
    return {"codigo": codigo.upper(), "nombre": nombre.strip()}

def buscar_curso(cursos, codigo):
    for curso in cursos:
        if curso["codigo"] == codigo.upper():
            return curso
    return None
