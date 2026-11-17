PRIORIDADES = ("alta", "media", "baja")

def agregar_tarea(tareas, titulo, prioridad):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("El título es obligatorio")
    if prioridad not in PRIORIDADES:
        raise ValueError("Prioridad inválida: use alta, media o baja")
    tarea = {
        "id": len(tareas) + 1,
        "titulo": titulo,
        "prioridad": prioridad,
        "completada": False,
    }
    tareas.append(tarea)
    return tarea

def completar_tarea(tareas, tarea_id):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            return tarea
    raise ValueError("Tarea no encontrada")

def pendientes(tareas):
    return [t for t in tareas if not t["completada"]]

def ordenar_por_prioridad(tareas):
    # sorted() es estable: misma prioridad conserva el orden de creación
    return sorted(tareas, key=lambda t: PRIORIDADES.index(t["prioridad"]))

def buscar_tareas(tareas, texto):
    if not texto:
        return []
    texto = texto.casefold()
    return [t for t in tareas if texto in t["titulo"].casefold()]
