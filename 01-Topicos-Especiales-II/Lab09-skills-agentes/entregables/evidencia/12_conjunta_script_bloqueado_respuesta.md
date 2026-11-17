# Informe de revisión

## Resumen
Revisé `ejemplo/calculadora.py` y `ejemplo/usuarios.py` leyendo el código con el checklist de la skill. No modifiqué ningún archivo.

**El paso obligatorio `check_syntax.py` no se ejecutó.** El entorno pidió aprobación para el comando y la sesión no es interactiva, así que no corrió con ninguno de los dos archivos. A simple vista la sintaxis de ambos es válida, pero eso no sustituye al script. Puedes correrlo tú o aprobar el comando y lo ejecuto.

Los hallazgos son errores funcionales (división por cero, lista vacía, un `print` que se ejecuta al importar) y un riesgo de seguridad grave (`eval`). No hay secretos embebidos en ninguno de los dos archivos.

## Hallazgos

| Severidad | Archivo / línea | Problema | Evidencia | Corrección |
|-----------|-----------------|----------|-----------|------------|
| CRÍTICO | `usuarios.py:8-9` | Ejecución arbitraria de código con `eval` sobre una entrada sin validar. | `return eval(codigo)` | Eliminar la función. Para evaluar literales usar `ast.literal_eval`. Para operaciones concretas, usar una lista blanca de funciones. |
| ALTO | `calculadora.py:15` | Código ejecutable a nivel de módulo. Al importar el archivo se llama `dividir(10, 0)` y falla con `ZeroDivisionError`. Ningún otro módulo ni prueba puede importarlo. | `print(dividir(10, 0))` | Moverlo a `if __name__ == "__main__":` y usar un caso válido, o quitarlo. |
| ALTO | `calculadora.py:3-4` | `dividir` no controla `b == 0`. | `return a / b` | Lanzar `ValueError("El divisor no puede ser cero")` o devolver un error explícito. |
| ALTO | `calculadora.py:6-7` | `promedio` falla con lista vacía: el valor por defecto `[]` siempre da `len(valores) == 0`. | `def promedio(valores=[]): return sum(valores) / len(valores)` | Validar `if not valores: raise ValueError(...)`. Usar `valores=None` o hacer el parámetro obligatorio. |
| MEDIO | `calculadora.py:6` | Parámetro mutable por defecto (`[]`), que se comparte entre llamadas. Hoy no se modifica, pero es una trampa si alguien lo cambia después. | `valores=[]` | `valores=None` y crear la lista dentro de la función si hace falta. |
| MEDIO | `calculadora.py:10-13` | `except:` sin tipo captura todo, incluso `KeyboardInterrupt` y `SystemExit`. Además, devolver `0` ante cualquier fallo confunde un error con un `0` legítimo, y `int(3.9)` da `3` sin avisar. | `except: return 0` | Capturar `(ValueError, TypeError)` y decidir si se lanza un error o se devuelve `None`. |
| MEDIO | `usuarios.py:3-6` | `buscar_usuario` devuelve `None` implícito cuando no hay coincidencia, y el llamador puede fallar más adelante. `usuario["id"]` lanza `KeyError` si algún dict no tiene esa clave. | `for usuario in usuarios: if usuario["id"] == id: return usuario` | Usar `usuario.get("id")`, devolver `None` de forma explícita y documentarlo, o lanzar una excepción propia. |
| BAJO | `usuarios.py:3` | El parámetro `id` tapa la función incorporada `id()`. | `def buscar_usuario(usuarios, id):` | Renombrarlo a `id_usuario`. |
| BAJO | ambos archivos | Sin docstrings, sin type hints y sin pruebas. | Ninguna función documentada. | Añadir docstrings con tipos y un archivo de pruebas. |

## Pruebas recomendadas
- `dividir(10, 0)` debe lanzar un error controlado, y `dividir(10, 2)` debe dar `5.0`.
- `promedio([])` y `promedio()` deben fallar con un mensaje claro. `promedio([2, 4])` debe dar `3.0`.
- `procesar("12")`, `procesar("abc")`, `procesar(None)` y `procesar("3.5")` para fijar qué debe devolver cada caso.
- `import ejemplo.calculadora` no debe lanzar ni imprimir nada.
- `buscar_usuario([], 1)`, un id inexistente y un dict sin clave `"id"`.
- Si `ejecutar_codigo` se conservara, comprobar que `ejecutar_codigo("__import__('os').system('echo x')")` queda rechazado. Lo recomendable es borrar la función.

## Resultado final
El código **presenta un riesgo importante y requiere correcciones** antes de usarse. Lo más urgente es eliminar o reemplazar el `eval` de `usuarios.py`. Después hay que sacar el `print` de nivel de módulo en `calculadora.py` y controlar la división por cero y la lista vacía.
