# Informe de revisión

## Resumen
`ejemplo/usuarios.py` tiene dos funciones y 9 líneas. El script `check_syntax.py` confirma que la sintaxis es válida, y no modifiqué el archivo. El problema grave es `ejecutar_codigo`, que pasa texto a `eval` sin ningún control. `buscar_usuario` tiene fallos menores. No hay secretos embebidos.

## Hallazgos

| Severidad | Archivo / línea | Problema | Evidencia | Corrección |
|-----------|-----------------|----------|-----------|------------|
| CRÍTICO (seguridad) | `usuarios.py:9` | `eval` ejecuta cualquier expresión Python que reciba. Si `codigo` viene de un usuario, un archivo o una red, permite ejecución remota de código. | `return eval(codigo)` | Eliminar la función. Si solo se necesitan literales, usar `ast.literal_eval(codigo)`. Si se necesitan operaciones, definir una tabla de operaciones permitidas. |
| ALTO (funcional) | `usuarios.py:3-6` | Si no hay coincidencia, la función devuelve `None` de forma implícita. Quien la llame y use el resultado, por ejemplo `buscar_usuario(...)["nombre"]`, fallará con `TypeError`. Tampoco se distingue «no existe» de un error. | No hay `return` ni `raise` tras el `for` | Devolver `None` de forma explícita y documentarlo, o lanzar un `LookupError` con un mensaje claro. |
| MEDIO (funcional) | `usuarios.py:5` | `usuario["id"]` lanza `KeyError` si algún diccionario no tiene la clave `id`. Una sola entrada mal formada rompe toda la búsqueda. Si `usuarios` es `None`, también falla con `TypeError`. | `if usuario["id"] == id:` | Usar `usuario.get("id") == id_usuario` y validar que `usuarios` sea iterable. |
| MEDIO (mantenimiento) | `usuarios.py:3` | El parámetro `id` tapa la función integrada `id()`. Además no hay tipos ni docstrings, y no queda claro si el id es `int` o `str`. Una comparación `1 == "1"` da `False` sin avisar. | `def buscar_usuario(usuarios, id):` | Renombrarlo a `id_usuario`, agregar anotaciones de tipo y docstring, y definir un tipo único de id. |
| BAJO (rendimiento) | `usuarios.py:4-6` | La búsqueda es lineal, O(n) por consulta. Con muchos usuarios y consultas repetidas se vuelve lenta. | Recorrido con `for` | Si se consulta mucho, indexar en un diccionario `{u["id"]: u for u in usuarios}`. |
| BAJO (calidad) | archivo completo | No hay pruebas ni manejo explícito de errores. Los nombres de las funciones tampoco indican que `ejecutar_codigo` es peligrosa. | Solo existen las dos funciones | Agregar pruebas con `pytest` (ver abajo). |

## Pruebas recomendadas
- Buscar un id que existe y comprobar que devuelve el usuario correcto.
- Buscar un id inexistente, con lista vacía y con lista llena. Debe dar el comportamiento definido (`None` o excepción).
- Lista con un diccionario sin clave `id`, con `usuarios=None` y con id de tipo distinto (`"1"` contra `1`).
- Ids duplicados: hoy devuelve el primero sin avisar.
- Si se conserva `ejecutar_codigo`: comprobar que rechaza `__import__("os").system("...")` y que solo acepta lo permitido.

## Resultado final
**Presenta un riesgo importante y requiere correcciones.** `ejecutar_codigo` no debe usarse tal como está. Para dejar `buscar_usuario` listo hay que definir qué pasa cuando no hay coincidencia y validar los datos de entrada.
