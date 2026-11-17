# Informe de revisión: `ejemplo/calculadora.py`

## Resumen
El archivo tiene 15 líneas y la sintaxis es válida (`check_syntax.py`: OK). Aun así, falla al ejecutarse y tiene varios problemas de diseño. No encontré secretos, `eval`, `exec` ni construcción de comandos o consultas, así que no hay vulnerabilidades clásicas. Los problemas de seguridad son de robustez y de validación de entradas. No modifiqué el archivo.

## Hallazgos

| Severidad | Archivo / línea | Tipo | Problema | Evidencia | Corrección |
|---|---|---|---|---|---|
| CRÍTICO | `calculadora.py:15` | Error funcional | Hay una llamada a nivel de módulo que revienta. Al importar o ejecutar el archivo lanza `ZeroDivisionError` y termina con traceback. | `print(dividir(10, 0))` | Quitarla o moverla a `if __name__ == "__main__":` con un caso válido o con manejo del error. |
| ALTO | `calculadora.py:3-4` | Error funcional | `dividir` no controla el divisor cero, ni entradas que no sean numéricas. | `return a / b` | Validar `b == 0` y lanzar `ValueError("El divisor no puede ser cero")`. Dejar que el llamador decida cómo mostrarlo. |
| ALTO | `calculadora.py:6-7` | Error funcional | `promedio()` sin argumentos usa la lista vacía por defecto, y `len(valores)` es 0. Eso da `ZeroDivisionError`. También falla con cualquier lista vacía. | `sum(valores) / len(valores)` | Comprobar `if not valores: raise ValueError(...)`. |
| ALTO | `calculadora.py:12-13` | Error funcional / seguridad | El `except:` desnudo atrapa todo, incluso `KeyboardInterrupt` y `SystemExit`. Devuelve `0` ante cualquier fallo. Una entrada inválida como `"abc"` o `None` se confunde con un cero real y el error queda oculto. Eso puede producir cálculos silenciosamente incorrectos. | `except: return 0` | Capturar solo `(ValueError, TypeError)`. Relanzar o devolver `None`, y no `0`, para distinguir la entrada inválida. |
| MEDIO | `calculadora.py:6` | Mantenimiento | Parámetro mutable por defecto (`valores=[]`). La lista se comparte entre llamadas. Hoy no se modifica, pero es un riesgo latente si alguien agrega `append`. | `def promedio(valores=[])` | Usar `valores=None` y crear la lista dentro, o hacer el parámetro obligatorio. |
| MEDIO | `calculadora.py:9-11` | Seguridad / validación | `procesar` usa `int()` sin validar el rango ni el origen de `numero`. `int()` trunca los decimales de forma silenciosa si le pasas un `float` (`int(3.9)` da `3`). Con cadenas enormes puede ser lento. | `return int(numero)` | Definir qué formatos acepta, validar el rango y documentar el truncamiento. |
| BAJO | General | Calidad | No hay docstrings, anotaciones de tipo ni pruebas. Los nombres mezclan español con parámetros genéricos (`a`, `b`). | Todo el archivo | Añadir tipos (`a: float, b: float -> float`), docstrings y un archivo de pruebas. |
| BAJO | General | Calidad | Los efectos secundarios a nivel de módulo (`print` en la línea 15) hacen que no se pueda importar para probar. | `print(...)` en el nivel superior | Proteger con `__main__`. |

## Pruebas recomendadas
- `dividir(10, 2)` da `5.0`. `dividir(10, 0)` debe lanzar un error controlado.
- `promedio([1, 2, 3])` da `2.0`. `promedio([])` y `promedio()` deben lanzar un error claro.
- `procesar("42")` da `42`. `procesar("abc")`, `procesar(None)` y `procesar("")` no deben devolver `0` sin avisar.
- `procesar(3.9)` para confirmar el truncamiento.
- Importar el módulo y comprobar que no ejecuta nada ni imprime nada.

## Resultado final
**Requiere correcciones antes de usarse.** El archivo ni siquiera se puede importar sin que falle (línea 15). Después, lo más urgente es el divisor cero en `dividir` y el promedio de listas vacías. Luego, el `except:` desnudo, que esconde errores.
