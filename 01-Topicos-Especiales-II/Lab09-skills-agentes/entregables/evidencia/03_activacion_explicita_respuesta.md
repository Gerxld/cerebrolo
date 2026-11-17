# Informe de revisión: `ejemplo/calculadora.py`

## Resumen
La sintaxis es válida: `check_syntax.py` devolvió `OK`. El archivo tiene 4 problemas funcionales o de diseño. Lo más grave es que el módulo se rompe al importarlo. No hay problemas de seguridad: no hay `eval`, `exec`, credenciales ni comandos construidos con texto del usuario. No modifiqué ningún archivo.

## Hallazgos

| Severidad | Archivo / línea | Problema | Evidencia | Corrección |
|-----------|-----------------|----------|-----------|------------|
| CRÍTICO | `calculadora.py:15` | Se ejecuta código a nivel de módulo, y esa llamada siempre falla. Quien haga `import calculadora` recibe `ZeroDivisionError`. | `print(dividir(10, 0))` | Quitarla o moverla a `if __name__ == "__main__":` con un `try/except ZeroDivisionError`. |
| ALTO | `calculadora.py:3-4` | `dividir` no controla la división por cero. | `return a / b` | Validar `b == 0` y lanzar `ValueError("El divisor no puede ser cero")`. |
| ALTO | `calculadora.py:7` | `promedio` falla con una lista vacía: `len(valores)` es 0 y da `ZeroDivisionError`. Por el valor por defecto, llamarla sin argumentos siempre falla. | `sum(valores) / len(valores)` | Si `not valores`, lanzar `ValueError` o devolver `None`, según el contrato que se elija. |
| MEDIO | `calculadora.py:6` | Parámetro mutable por defecto (`[]`). Hoy no se modifica, pero es un riesgo si alguien lo cambia después. | `def promedio(valores=[])` | Usar `valores=None` y crear la lista dentro, o hacer el parámetro obligatorio. |
| MEDIO | `calculadora.py:12-13` | `except:` sin tipo captura todo, incluidos `KeyboardInterrupt` y `SystemExit`. Además devuelve 0 en silencio, y no se distingue un `"0"` válido de una entrada inválida. | `except:` / `return 0` | `except (ValueError, TypeError):` y lanzar un error claro, o devolver `None`. |
| BAJO | `calculadora.py:3, 6, 9` | No hay tipos ni docstrings, y las funciones no tienen pruebas. | `def dividir(a, b):` | Añadir anotaciones (`a: float, b: float -> float`) y docstrings breves. |

## Pruebas recomendadas
- `dividir(10, 2)` da `5.0`.
- `dividir(10, 0)` lanza el error esperado.
- `promedio([])` y `promedio()` se comportan según el contrato definido.
- `promedio([1, 2, 3])` da `2.0`.
- `procesar("42")` da `42`, y `procesar("abc")`, `procesar(None)` y `procesar("0")` se distinguen entre sí.
- `import calculadora` no imprime ni lanza nada.

## Resultado final
**Requiere correcciones.** El módulo no se puede importar por la línea 15, y `dividir` y `promedio` tienen casos límite sin controlar. No encontré riesgos de seguridad. Cuando lo indiques, aplico las correcciones.
