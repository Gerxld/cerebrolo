# Informe de revisión: `ejemplo/calculadora.py`

## Resumen
El archivo tiene sintaxis válida (`check_syntax.py` dio OK), pero ni siquiera se puede importar: la línea 16 ejecuta `dividir(10, 0)` al cargarlo y lanza `ZeroDivisionError`. Además tiene un secreto en el código, dos funciones que fallan con entradas límite y un `except` que oculta errores. No modifiqué el archivo.

## Hallazgos

| Severidad | Archivo / línea | Problema | Evidencia | Corrección |
|---|---|---|---|---|
| ALTO (error) | `calculadora.py:16` | Código ejecutable a nivel de módulo, con una división por cero segura. Al importar o ejecutar el archivo, el programa termina con traceback. | `print(dividir(10, 0))` | Quitar la línea, o ponerla dentro de `if __name__ == "__main__":` con un `try/except ZeroDivisionError`. |
| ALTO (error) | `calculadora.py:4-5` | `dividir` no controla `b == 0`. | `return a / b` | Validar `b` y lanzar `ValueError("El divisor no puede ser cero")`, o capturar `ZeroDivisionError` en quien llama. |
| ALTO (error) | `calculadora.py:7-8` | `promedio` falla con lista vacía, y su valor por defecto `[]` es justo ese caso. Siempre falla si no se pasa argumento. | `valores=[]` y `sum(valores) / len(valores)` | Usar `valores=None` y, si no hay datos, lanzar `ValueError` o devolver `None`, según lo que se decida. |
| MEDIO (riesgo) | `calculadora.py:7` | Parámetro mutable por defecto. Hoy no se modifica, así que no falla, pero un cambio futuro que lo mute compartiría estado entre llamadas. | `def promedio(valores=[])` | Usar `valores=None` y crear la lista dentro de la función. |
| MEDIO (error) | `calculadora.py:11-14` | `except:` sin tipo captura todo, incluidos `KeyboardInterrupt` y `SystemExit`. Además devuelve `0` ante una entrada inválida, y `"abc"` queda igual que `"0"`. Con `procesar(3.7)` devuelve `3` sin avisar, porque `int()` trunca. | `except:` / `return 0` | Capturar `(ValueError, TypeError)` y relanzar un error claro o devolver `None`. |
| MEDIO (seguridad) | `calculadora.py:2` | Credencial escrita en el código fuente. Quedaría en el historial de Git. Es una constante sin uso en el archivo. | `API_KEY = 'demo-secret'` | Leerla con `os.environ["API_KEY"]` y eliminar la constante. Si el valor fue real, rotarla. |
| BAJO (mantenibilidad) | todo el archivo | No hay docstrings, anotaciones de tipo ni pruebas. `procesar` es un nombre poco descriptivo, y `dividir` y `promedio` no dicen cómo reportan los errores. | Funciones sin documentación | Agregar docstrings y tipos, y renombrar `procesar` (por ejemplo `a_entero`). |

No encontré `eval`, `exec`, comandos del sistema ni consultas SQL, así que no hay riesgo de inyección en este archivo.

## Pruebas recomendadas
- `dividir(10, 2)` da `5.0`, y `dividir(10, 0)` lanza el error esperado.
- `promedio([2, 4, 6])` da `4.0`, `promedio([])` y `promedio()` dan el error o valor definido.
- `procesar("12")` da `12`, `procesar("abc")` y `procesar(None)` dan el comportamiento definido, y `procesar(3.7)` se decide explícitamente.
- Importar el módulo no debe imprimir ni lanzar nada.

## Resultado final
**Requiere correcciones.** Hay tres errores funcionales (el principal rompe la importación) y una credencial hardcodeada. Hay que corregir al menos las líneas 16, 5 y 8 antes de usarlo.
