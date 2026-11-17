"""Gestor de tareas por consola.

Este archivo contiene solo el menú y la interacción con el usuario.
La lógica de las tareas está en tareas.py.
"""

import tareas as logica


def mostrar_menu():
    print("\n=== Gestor de tareas ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Salir")


def pedir_prioridad():
    while True:
        entrada = input("Prioridad (baja, media, alta): ")
        try:
            return logica.normalizar_prioridad(entrada)
        except ValueError as error:
            print(error)


def opcion_agregar(lista_tareas):
    titulo = input("Título de la tarea: ").strip()
    if not titulo:
        print("El título no puede estar vacío.")
        return
    prioridad = pedir_prioridad()
    tarea = logica.agregar_tarea(lista_tareas, titulo, prioridad)
    print(f"Tarea agregada: {tarea['titulo']} (prioridad {tarea['prioridad']})")


def opcion_listar(lista_tareas):
    if not lista_tareas:
        print("No hay tareas registradas.")
        return
    print("\nTareas:")
    for numero, tarea in enumerate(lista_tareas, start=1):
        estado = " (completada)" if tarea["completada"] else ""
        print(f"{numero}. {tarea['titulo']} [prioridad: {tarea['prioridad']}]{estado}")


def main():
    lista_tareas = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            opcion_agregar(lista_tareas)
        elif opcion == "2":
            opcion_listar(lista_tareas)
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
