# Informe de revisión

## Resumen
`ejemplo/calculadora.py` tiene sintaxis válida (`check_syntax.py` dijo OK). Son 15 líneas con tres funciones y una llamada suelta al final. Esa llamada hace que el módulo falle al importarlo. Las funciones no validan sus entradas y `procesar` oculta los errores. No encontré secretos embebidos, ni `eval`/`exec`, ni construcción de comandos o consultas, así que no hay hallazgos de seguridad críticos. No modifiqué el archivo.

## Hallazgos

| Archivo / línea | Severidad | Problema | Corrección | Evidencia |
|---|---|---|---|---|
| calculadora.py:15 | CRÍTICO (error funcional) | Código ejecutado a nivel de módulo: `dividir(10, 0)` lanza `ZeroDivisionError` en cuanto se ejecuta o importa el archivo. Ningún otro módulo puede importar `dividir`, `promedio` o `procesar`. | Borrar la línea o moverla a `if __name__ == "__main__":` con una llamada que no falle, o con el error capturado. | `print(dividir(10, 0))` |
| calculadora.py:3-4 | ALTO (error funcional) | `dividir` no controla `b == 0`. Tampoco valida los tipos, así que un `None` o un `str` lanzan `TypeError`. | `if b == 0: raise ValueError("El divisor no puede ser cero")`, o capturar `ZeroDivisionError` en quien llama. | `return a / b` |
| calculadora.py:6-7 | ALTO (error funcional) | `promedio` falla con una colección vacía: `len(valores)` es 0, y por el valor por defecto `[]` la llamada sin argumentos siempre falla. | Comprobar `if not valores: raise ValueError("Se requiere al menos un valor")`. | `return sum(valores) / len(valores)` |
| calculadora.py:6 | MEDIO (mantenibilidad) | Parámetro mutable por defecto (`valores=[]`). Hoy no se modifica la lista, pero es un patrón frágil: si alguien añade `valores.append(...)`, el estado se comparte entre llamadas. Además, el valor por defecto no tiene sentido, porque nunca produce un resultado válido. | Quitar el valor por defecto, o usar `valores=None` y crear la lista dentro. | `def promedio(valores=[]):` |
| calculadora.py:12-13 | ALTO (error funcional / riesgo) | `except:` desnudo captura todo, incluso `KeyboardInterrupt` y `SystemExit`. Además devuelve `0` ante cualquier fallo, y `procesar("abc")` y `procesar("0")` dan el mismo resultado. Un dato corrupto se vuelve un cero válido y puede falsear cálculos posteriores. `procesar(3.9)` devuelve `3` sin avisar, porque `int()` trunca. | `except (ValueError, TypeError):` y relanzar o devolver `None`, o registrar el error. Decidir si los decimales se aceptan. | `except:` / `return 0` |
| calculadora.py:3, 6, 9 | BAJO (calidad) | Sin docstrings, sin anotaciones de tipo y sin pruebas. Los nombres mezclan funciones de cálculo con una de conversión (`procesar`), cuyo nombre no dice qué hace. | Añadir docstrings y tipos (`def dividir(a: float, b: float) -> float`). Renombrar `procesar` a `a_entero`. | Todo el archivo |

## Pruebas recomendadas
- `dividir(10, 2) == 5.0`. `dividir(10, 0)` debe lanzar un error controlado.
- `promedio([2, 4, 6]) == 4`. `promedio([])` y `promedio()` deben lanzar un error claro.
- `procesar("12") == 12`. `procesar("abc")`, `procesar(None)` y `procesar("3.9")` deben comportarse como se decida, sin devolver `0` en silencio.
- Importar el módulo (`import ejemplo.calculadora`) no debe ejecutar nada ni fallar.

## Resultado final
**Requiere correcciones antes de usarse.** El archivo no se puede importar por la línea 15, y `dividir` y `promedio` fallan con entradas límite. El `except:` desnudo es el riesgo de mantenimiento más importante, porque oculta los errores en vez de mostrarlos.

Si quieres, aplico las correcciones y agrego las pruebas.
