# Informe de revisión

## Resumen
`ejemplo/calculadora.py` tiene sintaxis válida (`check_syntax.py` lo confirmó), pero el archivo tiene problemas en las tres áreas que pediste. Hay un secreto embebido, dos operaciones que fallan con entradas límite y una ejecución al importar que rompe el módulo. No modifiqué el archivo.

## Hallazgos

| Severidad | Archivo / línea | Problema | Evidencia | Corrección |
|---|---|---|---|---|
| CRÍTICO | `calculadora.py:2` | Secreto embebido en el código. Queda en el repositorio y en el historial de Git. | `API_KEY = 'de***'` | Leerlo del entorno: `API_KEY = os.environ["API_KEY"]`. Rotar la clave si fue real. |
| ALTO | `calculadora.py:16` | Código que se ejecuta al importar. Hace una división por cero, así que cualquier `import calculadora` lanza `ZeroDivisionError` antes de usar nada. | `print(dividir(10, 0))` | Quitarlo o ponerlo bajo `if __name__ == "__main__":` con manejo del error. |
| ALTO | `calculadora.py:4-5` | `dividir` no controla `b == 0`. | `return a / b` | Validar `b` y lanzar `ValueError("El divisor no puede ser cero")`. |
| ALTO | `calculadora.py:7-8` | `promedio` falla con una colección vacía. Como el valor por defecto es `[]`, llamarla sin argumentos produce `ZeroDivisionError`. | `sum(valores) / len(valores)` | Comprobar `if not valores:` y lanzar un error claro, o devolver `None` y documentarlo. |
| MEDIO | `calculadora.py:7` | Parámetro mutable por defecto. La lista se crea una sola vez y se comparte entre llamadas. Hoy no se modifica, pero es una trampa si alguien la altera. | `def promedio(valores=[])` | Usar `valores=None` y crear la lista dentro, o hacer el parámetro obligatorio. |
| MEDIO | `calculadora.py:13-14` | `except:` desnudo. Atrapa también `KeyboardInterrupt` y `SystemExit`. Además devuelve `0` ante cualquier entrada inválida, y no se distingue un `"0"` real de un error. | `except:` / `return 0` | Capturar `(ValueError, TypeError)` y propagar o devolver `None`. |
| BAJO | `calculadora.py:10` | `procesar` es un nombre poco descriptivo. Tampoco hay docstrings, tipos ni pruebas. | `def procesar(numero):` | Renombrar a algo como `convertir_a_entero` y añadir docstrings y type hints. |

## Pruebas recomendadas
- `dividir(10, 0)` debe lanzar `ValueError`, no `ZeroDivisionError`.
- `promedio([])` y `promedio()` deben dar un error controlado.
- `promedio([2, 4, 6])` debe dar `4.0`.
- `procesar("abc")`, `procesar(None)` y `procesar("0")` deben distinguirse entre sí.
- `import calculadora` no debe imprimir nada ni lanzar excepciones.

## Resultado final
**Presenta un riesgo importante.** No está listo. Antes de usarlo hay que sacar la clave del código y rotarla, quitar la llamada de la línea 16 y controlar los casos de división por cero y lista vacía.

Enmascaré el valor del secreto como indica el checklist. La clave se llama `demo-secret`, así que puede ser solo de ejemplo. Aun así conviene tratarla como real.
