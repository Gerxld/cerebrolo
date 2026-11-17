"""Gestor de tareas por consola - Versión 2.

Funciones:
    1) Agregar una tarea con título y prioridad (baja, media o alta).
    2) Listar las tareas existentes.
    3) Salir.

Las tareas se guardan solo en memoria (se pierden al cerrar el programa).
"""

PRIORIDADES_VALIDAS = ("baja", "media", "alta")


def mostrar_menu():
    print("\n=== Gestor de tareas ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Salir")


def pedir_prioridad():
    while True:
        prioridad = input("Prioridad (baja, media, alta): ").strip().lower()
        if prioridad in PRIORIDADES_VALIDAS:
            return prioridad
        print("Prioridad no válida. Debe ser: baja, media o alta.")


def agregar_tarea(tareas):
    titulo = input("Título de la tarea: ").strip()
    if not titulo:
        print("El título no puede estar vacío.")
        return
    prioridad = pedir_prioridad()
    tareas.append({"titulo": titulo, "prioridad": prioridad})
    print(f"Tarea agregada: {titulo} (prioridad {prioridad})")


def listar_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
        return
    print("\nTareas:")
    for numero, tarea in enumerate(tareas, start=1):
        print(f"{numero}. {tarea['titulo']} [prioridad: {tarea['prioridad']}]")


def main():
    tareas = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            listar_tareas(tareas)
        elif opcion == "3":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print("\nEntrada finalizada. Hasta luego.")
