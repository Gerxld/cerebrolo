# Informe de revisión

Archivo revisado: `ejemplo/calculadora.py`. El archivo no se modificó. El chequeo de sintaxis dio `OK`, es decir, el archivo compila.

## Resumen
El archivo tiene 3 funciones pequeñas y una llamada suelta al final. Esa llamada hace que el módulo falle apenas se ejecuta o se importa. Las funciones tampoco manejan los casos límite más obvios (divisor cero, lista vacía) y `procesar` oculta cualquier error. No hay secretos, `eval`/`exec` ni construcción de comandos o consultas, así que no hay problemas de seguridad graves. Solo hay un riesgo menor de validación de entradas.

## Hallazgos

| Severidad | Archivo / línea | Problema | Evidencia | Corrección |
|-----------|-----------------|----------|-----------|------------|
| ALTO (error funcional) | `calculadora.py:15` | Código ejecutable a nivel de módulo que siempre lanza `ZeroDivisionError`. Al ejecutar el archivo termina con traceback, y al importarlo desde otro módulo también falla. | `print(dividir(10, 0))` | Quitarla o moverla bajo `if __name__ == "__main__":` con un caso válido, o capturando el error de forma explícita. |
| ALTO (error funcional) | `calculadora.py:3-4` | `dividir` no controla el divisor cero. El error sale sin mensaje comprensible. | `return a / b` | `if b == 0: raise ValueError("El divisor no puede ser cero")`, o devolver un resultado controlado según lo que se defina. |
| ALTO (error funcional) | `calculadora.py:6-7` | `promedio` con lista vacía divide entre cero. Es además el comportamiento por defecto: `promedio()` sin argumentos falla siempre. | `def promedio(valores=[]):` `return sum(valores) / len(valores)` | Validar `if not valores: raise ValueError("Se necesita al menos un valor")`. |
| MEDIO (mantenibilidad) | `calculadora.py:6` | Parámetro mutable por defecto. Hoy no se modifica la lista, así que no causa un fallo, pero es un riesgo si alguien la muta después, porque la lista se comparte entre llamadas. | `valores=[]` | Usar `valores=None` y crear la lista dentro, o hacer el parámetro obligatorio (lo más natural aquí). |
| MEDIO (error / mantenibilidad) | `calculadora.py:10-13` | `except:` sin tipo captura todo, incluidos `KeyboardInterrupt` y `SystemExit`. Además devuelve `0` ante cualquier fallo, y no se distingue una entrada inválida (`"abc"`) de una entrada que realmente vale 0 (`"0"`). | `except:` `return 0` | `except (ValueError, TypeError):` y levantar un error propio o devolver `None` para que quien llama pueda distinguir el caso. |
| BAJO (error funcional) | `calculadora.py:11` | `int()` trunca sin avisar: `int(3.9)` da `3`, y `int(True)` da `1`. Con una cadena como `"3.9"` falla y cae en el `except`, devolviendo `0`. Si se esperan decimales, el resultado es incorrecto. | `return int(numero)` | Decidir el tipo esperado. Si se admiten decimales, usar `float()`. |
| BAJO (seguridad) | `calculadora.py:3-11` | Validación de entradas insuficiente: no se comprueba el tipo de los argumentos. Con tipos inesperados las funciones fallan con errores poco claros (por ejemplo, `dividir("a", 2)` da `TypeError`). No hay vector de ataque concreto, pues no se usa `eval` ni se leen datos externos. | `def dividir(a, b):` sin comprobaciones | Validar tipos o documentar el contrato en una docstring, según dónde se vaya a usar. |
| BAJO (calidad) | Todo el archivo | No hay docstrings, anotaciones de tipo ni pruebas. Los nombres de las funciones están bien, pero `procesar` no dice qué procesa. | Ninguna función documentada | Añadir docstrings y tipos (`def dividir(a: float, b: float) -> float`). Renombrar `procesar` a algo como `a_entero`. |

## Pruebas recomendadas
- `dividir(10, 2)` da `5.0` y `dividir(10, 0)` lanza el error definido.
- `promedio([2, 4, 6])` da `4.0` y `promedio([])` lanza el error definido.
- `promedio()` sin argumentos.
- `procesar("12")` da `12`. `procesar("abc")`, `procesar(None)` y `procesar("0")` deben poder distinguirse.
- `procesar(3.9)` y `procesar("3.9")`: confirmar el comportamiento esperado.
- Importar el módulo (`import calculadora`) sin que ejecute nada ni falle.

## Resultado final
Requiere correcciones antes de usarse. El problema más urgente es la línea 15, que rompe el módulo en cuanto se carga. Después van los casos de división por cero y el `except` sin tipo. No hay riesgo importante de seguridad en lo que contiene el archivo.
