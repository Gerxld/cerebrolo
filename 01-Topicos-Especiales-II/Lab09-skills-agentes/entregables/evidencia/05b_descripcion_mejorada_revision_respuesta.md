# Informe de revisión: `ejemplo/calculadora.py`

## Resumen
El archivo tiene 15 líneas y una sintaxis válida (`check_syntax.py` lo confirmó). Aun así, falla al importarse o ejecutarse y tiene varios problemas de diseño. No encontré `eval`, `exec`, credenciales ni comandos construidos con texto del usuario. Los problemas de seguridad son de validación de entradas y no hay vulnerabilidades graves. No modifiqué el archivo.

## Hallazgos

| Severidad | Línea | Tipo | Problema | Evidencia | Corrección |
|---|---|---|---|---|---|
| CRÍTICO | 15 | Error funcional | Código que se ejecuta al importar el módulo, con una división por cero segura. | `print(dividir(10, 0))` está a nivel de módulo. Lanza `ZeroDivisionError` al ejecutar el archivo o hacer `import calculadora`. | Eliminarlo o moverlo a `if __name__ == "__main__":` con un caso válido. |
| ALTO | 3-4 | Error funcional | `dividir` no controla `b == 0`. | `return a / b` sin validación. | Hacer `if b == 0: raise ValueError("El divisor no puede ser cero")`, o capturar el error donde se llame. |
| ALTO | 6-7 | Error funcional | `promedio` falla con una colección vacía. | `sum(valores) / len(valores)`. Con `[]`, que además es el valor por defecto, da `ZeroDivisionError`. Así, `promedio()` sin argumentos siempre falla. | Validar `if not valores: raise ValueError(...)`. |
| MEDIO | 6 | Mantenimiento | Parámetro mutable por defecto. | `valores=[]`. La lista se comparte entre llamadas. Hoy no se modifica, pero cualquier cambio futuro que la modifique arrastrará datos entre llamadas. | Usar `valores=None` y crear la lista dentro, o hacer el parámetro obligatorio. |
| ALTO | 10-13 | Error funcional / seguridad | `except:` desnudo que devuelve 0 sin avisar. | `except: return 0`. Atrapa también `KeyboardInterrupt` y `SystemExit`. Además, una entrada inválida como `"abc"` o `None` queda como `0`, indistinguible de un `0` real. En un cálculo, eso produce resultados incorrectos sin ningún aviso. | Capturar `(ValueError, TypeError)` y relanzar con un mensaje claro, o devolver `None` y documentarlo. |
| MEDIO | 9-11 | Validación de entradas | `procesar` acepta tipos inesperados. | `int(numero)` convierte `3.9` a `3` (trunca) y acepta `True` como `1`. No hay límite de longitud para cadenas muy grandes. | Definir qué entradas son válidas (por ejemplo, solo `str` o `int`) y validarlas. |
| BAJO | todo | Calidad | Sin documentación, sin anotaciones de tipo y sin pruebas. | Ninguna función tiene docstring ni tipos. El comentario de la línea 1 solo repite la ruta. | Añadir docstrings, anotaciones (`a: float, b: float -> float`) y pruebas con `pytest`. |
| BAJO | 3, 6, 9 | Estilo | Nombres mezclados y poco precisos. | `procesar` no dice qué hace (convierte a entero). | Renombrarla, por ejemplo a `a_entero`. Mantener un solo idioma en los nombres. |

## Pruebas recomendadas
- `dividir(10, 2)` da `5.0`.
- `dividir(1, 0)` debe lanzar el error esperado.
- `promedio([2, 4, 6])` da `4.0`.
- `promedio([])` y `promedio()` deben lanzar un error claro.
- `promedio` llamado dos veces seguidas no debe compartir estado.
- `procesar("42")` da `42`.
- `procesar("abc")` y `procesar(None)` no deben devolver `0` en silencio.
- `procesar("3.9")` falla con `ValueError` y `procesar(3.9)` devuelve `3`. Hay que decidir cuál es el comportamiento deseado.
- `import calculadora` no debe imprimir ni lanzar nada.

## Resultado final
**Requiere correcciones.** El archivo no se puede importar sin que se produzca un error (línea 15). Las otras dos funciones tienen fallos con entradas límite, y `procesar` oculta errores. Conviene corregir primero la línea 15, luego los casos de división por cero y colección vacía, y después el manejo de excepciones.
