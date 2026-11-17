# Registro de solicitudes al chat web

Chat: claude.ai (Sonnet 5.5), una sola conversación: https://claude.ai/chat/b0c0dbdd-c0c1-4efd-9adb-6b834df109bd. Capturas en `capturas/` (chat_01 a chat_11, JPG). Los prompts completos están en el informe PDF.

| N.° | Paso | Prompt (resumen en una línea) | Cambio que produjo | Captura |
|---|---|---|---|---|
| 1 | 4 | Contexto del laboratorio (literal de la guía) | Ninguno; el chat esperó el requisito | chat_01 |
| 2 | 5 | Primera versión: agregar, listar, salir, lista en memoria | `app.py` v1 | chat_02 |
| 3 | 6 | Explicar cada función y el flujo, sin cambiar código | Ninguno | chat_03 |
| 4 | 9 | Prioridad baja/media/alta con reintento si es inválida | `app.py` v2: dict por tarea + `pedir_prioridad()` | chat_04 |
| 5 | 12 | Depurar `EOFError` al pulsar Ctrl+Z en la prioridad | `try/except EOFError` en `__main__` | chat_05, chat_06 |
| 6 | 14 | Separar lógica en `tareas.py`, menú en `app.py`, pruebas con unittest | Tres archivos; 5 pruebas | chat_07 |
| 7 | 16 | Completar tarea desde el menú, `[ ]` / `[X]` al listar | `app.py`: opción 3, `opcion_completar`, marcas | chat_08 |
| 8 | 17 | Revisión final: errores, validaciones, duplicación, legibilidad | 14 hallazgos; ningún cambio directo | chat_09, chat_10 |
| 9 | 17 | Aplicar solo hallazgos 6, 11 y 3 (parcial) | `KeyboardInterrupt`, `try/except` en `opcion_agregar`, 2 pruebas nuevas | chat_11 |

## Decisiones sobre la revisión (solicitud 8)
- Aceptados: 6 (Ctrl+C), 11 (pruebas con 0 y negativo).
- Modificado: 3. Se conservó el filtro de título vacío en `app.py` y se adoptó solo el `try/except ValueError`.
- Rechazados: 1 y 2 (validación de tipos, inalcanzable desde el menú); 4, 5, 7, 8, 9, 10, 12, 13, 14 (mejoras para un programa más grande, ver informe, sección 4).
- Alcance extra de la solicitud 6 (`completar_tarea`, campo `completada`, 2 pruebas): conservado y justificado en el informe.
