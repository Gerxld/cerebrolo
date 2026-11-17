## Objetivo

Agregar una función que elimine una tarea de la lista a partir de su ID.

## Alcance

- `tasks.py`
- `tests/test_tasks.py`

No se debe modificar ningún otro archivo (`app.py` queda igual).

## Restricciones

- No agregar dependencias externas (solo biblioteca estándar de Python 3).
- No eliminar ni cambiar la firma de las funciones existentes.
- Mantener compatibilidad con todas las pruebas actuales, sin cambiarlas ni debilitarlas.
- No renumerar los IDs de las tareas que permanecen en la lista.

## Criterios de aceptación

- Existe la función `eliminar_tarea(tareas, tarea_id)` en `tasks.py`.
- Elimina de la lista la tarea cuyo `id` coincide con `tarea_id`, modificando la lista recibida, y devuelve la tarea eliminada.
- Si no existe una tarea con ese ID, lanza `ValueError("Tarea no encontrada")`, el mismo mensaje que usa `completar_tarea`.
- Las demás tareas conservan su `id` y su orden.
- Existen pruebas para: eliminar una tarea existente (la lista queda sin ella y la función devuelve la tarea eliminada), eliminar un ID inexistente (lanza `ValueError`) y eliminar sobre una lista vacía.

## Validación

Ejecutar desde la raíz del repositorio:

```
python -m unittest discover -s tests
python app.py
```

La tarea está terminada cuando todas las pruebas pasan y el Pull Request solo toca los dos archivos del alcance.
