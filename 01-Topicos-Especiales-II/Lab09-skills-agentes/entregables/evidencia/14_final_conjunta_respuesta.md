# Informe de revisión

## Resumen
Ambos archivos tienen sintaxis válida (`check_syntax.py` dio OK en los dos). Aun así, contienen errores funcionales claros y un riesgo de seguridad grave en `usuarios.py`. No modifiqué ningún archivo.

## Hallazgos

| Severidad | Archivo / línea | Problema | Evidencia | Corrección |
|-----------|-----------------|----------|-----------|------------|
| CRÍTICO | usuarios.py:8-9 | Ejecución arbitraria de código con `eval` sobre una entrada sin validar | `return eval(codigo)` | Eliminar la función. Si se necesita evaluar literales, usar `ast.literal_eval`. Si se necesita una calculadora, parsear con `ast` y una lista blanca de operadores. |
| ALTO | calculadora.py:15 | Llamada a nivel de módulo que se ejecuta al importar y lanza `ZeroDivisionError` | `print(dividir(10, 0))` | Quitar la línea o moverla a `if __name__ == "__main__":` con un caso que no falle. |
| ALTO | calculadora.py:3-4 | `dividir` no controla el divisor cero | `return a / b` | Validar `b == 0` y lanzar `ValueError("El divisor no puede ser cero")`, o capturar `ZeroDivisionError` con un mensaje claro. |
| ALTO | calculadora.py:6-7 | `promedio` falla con lista vacía (`ZeroDivisionError`) | `return sum(valores) / len(valores)` | Si `not valores`, lanzar `ValueError` o devolver `None`, y documentar cuál de los dos hace. |
| MEDIO | calculadora.py:6 | Parámetro mutable por defecto. Hoy no se modifica, pero es una trampa si alguien lo cambia después. | `def promedio(valores=[])` | Usar `valores=None` o hacerlo obligatorio, ya que un promedio sin datos no tiene sentido. |
| MEDIO | calculadora.py:10-13 | `except:` desnudo que oculta cualquier error, incluso `KeyboardInterrupt`, y devuelve 0 sin avisar. Así `"abc"` y `"0"` dan el mismo resultado. | `except:` / `return 0` | Capturar `(ValueError, TypeError)` y lanzar un error claro, o devolver `None` para distinguir la entrada inválida. |
| MEDIO | usuarios.py:3-6 | `buscar_usuario` devuelve `None` implícito cuando no hay coincidencia. Además, `usuario["id"]` lanza `KeyError` si algún dict no tiene esa clave. | `for ... if usuario["id"] == id: return usuario` (sin `return` final) | Devolver `None` explícito o lanzar un error propio. Usar `usuario.get("id")` si las claves pueden faltar. |
| BAJO | usuarios.py:3 | El parámetro `id` tapa la función integrada `id()` | `def buscar_usuario(usuarios, id)` | Renombrar a `usuario_id`. |
| BAJO | ambos | Sin docstrings, sin type hints y sin pruebas. Eso dificulta el mantenimiento y no hay nada que cubra los casos límite. | Ninguna función documentada | Añadir docstrings y tipos, y un archivo de pruebas. |

No encontré credenciales ni secretos embebidos en ninguno de los dos archivos.

## Pruebas recomendadas
- `dividir(10, 0)` debe dar un error controlado, no un traceback.
- `promedio([])` y `promedio([1, 2, 3])`.
- `procesar("abc")`, `procesar("12")`, `procesar(None)` y `procesar("3.5")`. Hoy los casos 1, 3 y 4 devuelven 0 sin avisar.
- `buscar_usuario([], 1)`, un id inexistente y un dict sin clave `"id"`.
- Importar `calculadora` no debe imprimir ni fallar.
- Si se mantiene `ejecutar_codigo`, probar `"__import__('os').system('...')"`. Debe ser rechazado.

## Resultado final
**Presenta un riesgo importante y requiere correcciones.** Hay que corregir primero `eval` en `usuarios.py`. Después, `calculadora.py` falla nada más importarse por la línea 15 y no controla ni el divisor cero ni la lista vacía.
