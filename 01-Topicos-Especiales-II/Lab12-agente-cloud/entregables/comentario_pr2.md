@copilot Revisé el diff y las pruebas pasan, pero falta cubrir un caso que el issue pide de forma explícita: filtrar por una categoría que ninguna tarea tiene. Hoy la prueba de filtrado solo comprueba una categoría existente en minúsculas.

Antes de integrar este PR, agrega pruebas en `tests/test_tasks.py` que comprueben que:

1. Filtrar por una categoría inexistente devuelve una lista vacía.
2. Filtrar con la categoría en mayúsculas ("TRABAJO") devuelve la misma tarea que "trabajo" (el caso inverso al que ya existe).

No cambies la API pública ni agregues dependencias, y no toques `tasks.py` ni `app.py` salvo que una de las pruebas nuevas revele un fallo real. Actualiza el mismo Pull Request.
