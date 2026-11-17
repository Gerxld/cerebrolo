"""Gestor de tareas por consola - Versión 1.

Funciones:
    1) Agregar una tarea con un título.
    2) Listar las tareas existentes.
    3) Salir.

Las tareas se guardan solo en memoria (se pierden al cerrar el programa).
"""


def mostrar_menu():
    print("\n=== Gestor de tareas ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Salir")


def agregar_tarea(tareas):
    titulo = input("Título de la tarea: ").strip()
    if not titulo:
        print("El título no puede estar vacío.")
        return
    tareas.append(titulo)
    print(f"Tarea agregada: {titulo}")


def listar_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
        return
    print("\nTareas:")
    for numero, titulo in enumerate(tareas, start=1):
        print(f"{numero}. {titulo}")


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
    main()
