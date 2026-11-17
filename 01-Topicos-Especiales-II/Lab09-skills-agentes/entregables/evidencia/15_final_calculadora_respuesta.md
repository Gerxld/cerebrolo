# Informe de revisión

## Resumen
`ejemplo/calculadora.py` tiene sintaxis válida (comprobada con `check_syntax.py`), pero el archivo falla al importarse y al ejecutarse. La línea 15 llama a `dividir(10, 0)` a nivel de módulo y lanza `ZeroDivisionError`. Además, `promedio` falla con una lista vacía, y tiene un parámetro mutable por defecto. `procesar` oculta los errores con un `except` desnudo. No encontré secretos embebidos, `eval`/`exec` ni construcción de comandos o consultas. No modifiqué el archivo.

## Hallazgos

| Severidad | Archivo / línea | Problema | Evidencia | Corrección |
|-----------|-----------------|----------|-----------|------------|
| ALTO (error) | `calculadora.py:15` | Código de prueba que se ejecuta al importar el módulo, y que termina en excepción. | `print(dividir(10, 0))` | Quitar la línea o moverla bajo `if __name__ == "__main__":` con un manejo del error. |
| ALTO (error) | `calculadora.py:3-4` | `dividir` no controla la división por cero. | `return a / b` | Validar `b == 0` y lanzar `ValueError("El divisor no puede ser cero")`. |
| ALTO (error) | `calculadora.py:6-7` | `promedio` falla con una colección vacía (`ZeroDivisionError`). Con el valor por defecto `[]`, llamarla sin argumentos siempre falla. | `return sum(valores) / len(valores)` | Si `not valores`, lanzar `ValueError` con un mensaje claro, o devolver `None` y documentarlo. |
| MEDIO (riesgo) | `calculadora.py:6` | Parámetro mutable por defecto. Hoy no se modifica la lista, pero es una trampa si la función cambia. | `def promedio(valores=[]):` | Usar `valores=None` y `valores = valores or []`, o hacer el parámetro obligatorio. |
| MEDIO (error/riesgo) | `calculadora.py:10-13` | `except:` desnudo. Captura también `KeyboardInterrupt` y `SystemExit`. Devuelve `0` ante cualquier fallo, y eso se confunde con una entrada válida `"0"`. | `except:` / `return 0` | Capturar `(ValueError, TypeError)` y lanzar un error o devolver `None`, no `0`. |
| BAJO (validación) | `calculadora.py:3, 6, 9` | No hay validación de tipos. `dividir("a", 2)` o `promedio([1, "x"])` dan `TypeError` poco claro. | Funciones sin comprobaciones de tipo | Validar entradas o añadir type hints (`a: float, b: float -> float`). |
| BAJO (mantenibilidad) | `calculadora.py:3-13` | No hay docstrings, hints ni pruebas. `procesar` es un nombre poco descriptivo. | Funciones sin documentación | Añadir docstrings, renombrar a `convertir_a_entero` y crear pruebas. |

Sobre seguridad: no hay hallazgos críticos. El único riesgo cercano es la validación insuficiente de entradas, que ya aparece como BAJO. `int(numero)` no ejecuta código, así que no es un vector de inyección.

## Pruebas recomendadas
- `dividir(10, 2) == 5` y `dividir(10, 0)` lanza un error claro.
- `promedio([])` y `promedio()` se comportan según lo definido, sin `ZeroDivisionError` sin controlar.
- `promedio([1, 2, 3]) == 2`.
- `procesar("42") == 42`, `procesar("0")` frente a `procesar("abc")` (deben distinguirse) y `procesar(None)`.
- Importar el módulo no debe imprimir ni lanzar excepciones.

## Resultado final
**Requiere correcciones.** El módulo no se puede importar sin que falle, y hay tres errores funcionales (líneas 4, 7 y 15). No hay riesgos de seguridad graves, pero el `except:` desnudo y el parámetro mutable conviene corregirlos. Si quieres, aplico las correcciones, pero no toqué el archivo porque pediste que no se modificara.
