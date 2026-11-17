## Objetivo

Agregar una categoría a cada tarea y permitir filtrar las tareas pendientes por categoría.

## Alcance

- `tasks.py`
- `app.py`
- `tests/test_tasks.py`

No se debe modificar ningún otro archivo.

## Restricciones

- No agregar dependencias externas (solo biblioteca estándar de Python 3).
- No eliminar funciones existentes (`agregar_tarea`, `completar_tarea`, `pendientes`).
- Mantener compatibilidad con las pruebas actuales: las dos pruebas que existen hoy deben seguir pasando sin cambiarlas.
- No renombrar archivos, funciones ni claves existentes del diccionario de la tarea (`id`, `titulo`, `completada`), y no hacer cambios de estilo ajenos a esta tarea.

## Criterios de aceptación

- `agregar_tarea` recibe una categoría no vacía como parámetro y la guarda en la tarea con la clave `categoria`. La categoría se limpia de espacios al inicio y al final.
- Si la categoría está vacía o solo tiene espacios, `agregar_tarea` lanza `ValueError("La categoría es obligatoria")`. La validación del título sigue funcionando como hasta ahora.
- `pendientes` acepta opcionalmente una categoría. Sin categoría devuelve todas las pendientes, igual que hoy; con categoría devuelve solo las pendientes de esa categoría.
- El filtrado no distingue mayúsculas de minúsculas ("Estudio" y "estudio" coinciden).
- Filtrar por una categoría que ninguna tarea tiene no falla: devuelve una lista vacía.
- `app.py` crea sus tareas de ejemplo con categoría y muestra la categoría en la salida; además imprime un ejemplo de filtrado por categoría.
- Existen pruebas en `tests/test_tasks.py` para: categoría válida, categoría vacía y filtrado (incluyendo el caso sin distinción de mayúsculas).

## Validación

Ejecutar desde la raíz del repositorio:

```
python -m unittest discover -s tests
python app.py
```

La tarea está terminada cuando todas las pruebas pasan, `app.py` se ejecuta sin errores y el Pull Request solo toca los tres archivos del alcance.
