from tasks import agregar_tarea, completar_tarea, pendientes

tareas = []

agregar_tarea(tareas, "Estudiar pruebas unitarias", "alta")
agregar_tarea(tareas, "Preparar exposición", "media")
completar_tarea(tareas, 1)

print("Tareas pendientes:")
for tarea in pendientes(tareas):
    print(f'- {tarea["id"]}: {tarea["titulo"]} (prioridad: {tarea["prioridad"]})')
