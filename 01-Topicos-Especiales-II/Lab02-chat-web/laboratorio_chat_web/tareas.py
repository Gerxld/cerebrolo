"""Lógica de tareas (sin entrada/salida por consola)."""

PRIORIDADES_VALIDAS = ("baja", "media", "alta")


def normalizar_prioridad(prioridad):
    """Devuelve la prioridad en minúsculas y sin espacios.

    Lanza ValueError si no es baja, media o alta.
    """
    valor = str(prioridad).strip().lower()
    if valor not in PRIORIDADES_VALIDAS:
        raise ValueError("Prioridad no válida. Debe ser: baja, media o alta.")
    return valor


def agregar_tarea(lista_tareas, titulo, prioridad):
    """Crea una tarea, la agrega a la lista y la devuelve.

    Lanza ValueError si el título está vacío o la prioridad no es válida.
    """
    titulo = str(titulo).strip()
    if not titulo:
        raise ValueError("El título no puede estar vacío.")
    prioridad = normalizar_prioridad(prioridad)

    tarea = {"titulo": titulo, "prioridad": prioridad, "completada": False}
    lista_tareas.append(tarea)
    return tarea


def completar_tarea(lista_tareas, numero):
    """Marca como completada la tarea con ese número (empezando en 1).

    Lanza ValueError si el número no corresponde a ninguna tarea.
    """
    if not 1 <= numero <= len(lista_tareas):
        raise ValueError(f"No existe la tarea número {numero}.")
    tarea = lista_tareas[numero - 1]
    tarea["completada"] = True
    return tarea
