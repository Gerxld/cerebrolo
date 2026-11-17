# Paso 28. Cambio limitado a R05 (v1.1)

Fecha y hora: 29/10/2026 11:01
Comando (desde laboratorio_sdd, prompt por entrada estándar): `claude -p --model sonnet --allowedTools "Read,Edit" --permission-mode acceptEdits`

## Prompt

```text
Cambio aprobado: spec v1.1, R05/AC05 reduce el límite de
3 a 2. La prueba actualizada falla. Modifica exclusivamente
la regla de límite en prestamos.py. No cambies otras funciones
ni tests. Ejecutaré las pruebas independientemente.
```

## Respuesta de la IA

Cambié la regla de límite en `prestamos.py:45-46` de 3 a 2. El umbral ahora es `>= 2`. También actualicé el texto del error a "el usuario ya tiene 2 préstamos activos", para que el mensaje coincida con el límite. No toqué otras funciones ni tests, y no ejecuté las pruebas, como indicaste.

Si la prueba actualizada compara el texto exacto del mensaje y espera el texto anterior ("3 préstamos"), fallará por eso. En ese caso dime y lo ajusto.
