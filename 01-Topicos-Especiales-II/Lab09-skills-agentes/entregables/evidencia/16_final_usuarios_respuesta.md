# Informe de revisión

## Resumen
`ejemplo/usuarios.py` tiene 10 líneas y dos funciones. La sintaxis es válida (`check_syntax.py` dio OK). El problema grave es `ejecutar_codigo`, que ejecuta con `eval` cualquier texto que reciba. `buscar_usuario` funciona en el caso normal, pero no controla los casos límite. No hay secretos embebidos. No modifiqué el archivo.

## Hallazgos

| Severidad | Archivo / línea | Problema | Evidencia | Corrección |
|-----------|-----------------|----------|-----------|------------|
| CRÍTICO | `usuarios.py:8-9` | Ejecución de código arbitrario con `eval`. Si `codigo` viene de un usuario, un archivo o una petición, quien lo controle puede ejecutar comandos en el sistema. | `return eval(codigo)` | Eliminar la función. Si hace falta evaluar literales, usar `ast.literal_eval`. Si hace falta evaluar operaciones, usar una lista blanca de operaciones o un parser de expresiones. |
| ALTO | `usuarios.py:3-6` | Devuelve `None` de forma implícita cuando no encuentra al usuario. El llamador no puede distinguir «no existe» de un error, y un uso como `buscar_usuario(...)["nombre"]` lanza `TypeError`. | El `for` termina sin `return` final. | Devolver `None` de forma explícita y documentarlo, o lanzar una excepción propia (`UsuarioNoEncontrado`). Agregar anotaciones de tipo (`-> dict \| None`). |
| MEDIO | `usuarios.py:4-5` | `usuario["id"]` lanza `KeyError` si algún diccionario no tiene la clave `id`. También falla con `TypeError` si `usuarios` es `None` o un elemento no es un diccionario. Una sola entrada mal formada rompe toda la búsqueda. | `if usuario["id"] == id:` | Usar `usuario.get("id") == id` y validar que `usuarios` sea iterable. |
| MEDIO | `usuarios.py:3` | El parámetro `id` tapa la función incorporada `id()` de Python. Además es un nombre poco descriptivo. | `def buscar_usuario(usuarios, id):` | Renombrarlo a `usuario_id`. |
| BAJO | `usuarios.py:3-6` | La búsqueda es lineal. Con muchas búsquedas sobre una lista grande se vuelve lenta. | Recorrido con `for` en cada llamada. | Si se busca seguido, indexar los usuarios en un diccionario `{id: usuario}`. |
| BAJO | `usuarios.py:3,8` | No hay docstrings, tipos ni pruebas. No hay forma de saber el formato esperado de `usuarios` (lista de diccionarios con `id`). | Ambas funciones sin documentación. | Agregar docstrings y anotaciones de tipo, y pruebas unitarias. |
| BAJO | `usuarios.py:1` | Mantenimiento: el módulo mezcla dos responsabilidades sin relación. Una busca usuarios y la otra evalúa código. | `buscar_usuario` y `ejecutar_codigo` en el mismo archivo. | Quitar `ejecutar_codigo`. Con eso el módulo queda con una sola responsabilidad. |

## Pruebas recomendadas
- `buscar_usuario([], 1)` debe devolver `None` (o lanzar la excepción elegida) sin fallar.
- `buscar_usuario([{"nombre": "Ana"}], 1)` no debe lanzar `KeyError`.
- `buscar_usuario(None, 1)` debe dar un error comprensible.
- IDs duplicados: confirmar qué comportamiento se espera (hoy devuelve el primero).
- Tipos distintos: `buscar_usuario([{"id": "1"}], 1)` devuelve `None` porque compara `"1"` con `1`. Definir si se acepta.
- `ejecutar_codigo("__import__('os').system('whoami')")` ejecuta un comando del sistema. Es la prueba que demuestra el riesgo, y después de la corrección debe fallar o no existir.

## Resultado final
**Presenta un riesgo importante y requiere correcciones.** No debe usarse tal cual mientras exista `ejecutar_codigo`. Después de eliminar esa función y endurecer `buscar_usuario`, el archivo quedaría en buen estado.
