# Informe de revisión

## Resumen
`ejemplo/usuarios.py` tiene 9 líneas y dos funciones. La sintaxis es válida (`check_syntax.py` dio OK). `ejecutar_codigo` es un problema grave de seguridad. `buscar_usuario` falla en silencio cuando no encuentra al usuario y tiene problemas menores de robustez y nombres. No encontré credenciales ni secretos embebidos. No modifiqué el archivo.

## Hallazgos

| Severidad | Archivo / línea | Problema | Evidencia | Corrección |
|-----------|-----------------|----------|-----------|------------|
| CRÍTICO | `usuarios.py:8-9` | **Seguridad.** `eval` sobre una cadena recibida por parámetro permite ejecución arbitraria de código (RCE). Quien controle `codigo` puede leer archivos, ejecutar comandos o borrar datos. | `return eval(codigo)` | Eliminar la función. Si hace falta evaluar literales, usar `ast.literal_eval`. Si hace falta evaluar operaciones, usar una lista blanca de operaciones o un parser propio. |
| ALTO | `usuarios.py:3-6` | **Error funcional.** Si ningún usuario coincide, la función termina sin `return` y devuelve `None` sin avisar. El llamador que haga `buscar_usuario(...)["nombre"]` fallará con `TypeError`. | `for ... if usuario["id"] == id: return usuario` y no hay retorno final | Devolver `None` de forma explícita y documentarlo (`-> dict \| None`), o lanzar una excepción propia como `UsuarioNoEncontrado`. |
| MEDIO | `usuarios.py:5` | **Error funcional.** `usuario["id"]` lanza `KeyError` si algún diccionario no tiene la clave `id`. Si `usuarios` es `None`, también falla. No hay validación de entradas. | `if usuario["id"] == id:` | Usar `usuario.get("id") == id` y validar que `usuarios` sea iterable. |
| MEDIO | `usuarios.py:3` | **Mantenibilidad.** El parámetro `id` oculta la función incorporada `id()`. | `def buscar_usuario(usuarios, id):` | Renombrarlo a `usuario_id`. |
| BAJO | `usuarios.py:3-9` | **Mantenibilidad.** Faltan docstrings, anotaciones de tipo y pruebas. La búsqueda lineal es O(n), lo que puede pesar con muchos usuarios. | Ninguna de las dos funciones tiene docstring ni tipos | Añadir docstrings y tipos. Si la lista crece, indexar por id en un `dict`. |

## Pruebas recomendadas
- `buscar_usuario([{"id": 1}], 1)` debe devolver el usuario.
- `buscar_usuario([{"id": 1}], 99)` y `buscar_usuario([], 1)` deben dar el resultado definido para "no encontrado" (hoy dan `None`).
- `buscar_usuario([{"nombre": "x"}], 1)` no debe lanzar `KeyError`.
- `buscar_usuario(None, 1)` debe fallar con un error claro.
- Con `ejecutar_codigo`, `"__import__('os').system('echo pwned')"` demuestra la ejecución arbitraria. Si la función se conserva, esa entrada debe ser rechazada.

## Resultado final
**Presenta un riesgo importante.** No debe usarse tal cual. Hay que eliminar `ejecutar_codigo` antes de cualquier uso con datos externos. `buscar_usuario` requiere correcciones menores y pruebas.
