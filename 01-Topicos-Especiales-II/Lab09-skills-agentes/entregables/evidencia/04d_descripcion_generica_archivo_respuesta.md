Leí `ejemplo/usuarios.py`, pero no dijiste cuál es el problema. Esto es lo que veo en el código:

1. **`ejecutar_codigo` es el problema más serio** (línea 8-9). `eval(codigo)` ejecuta cualquier expresión de Python que reciba, así que si `codigo` viene de un usuario o de un archivo externo, esa persona puede correr lo que quiera en tu máquina, por ejemplo `__import__("os").system(...)`. Si solo necesitas leer datos literales (números, listas, diccionarios), usa `ast.literal_eval`. Si necesitas calcular expresiones, conviene un parser propio. Si no tiene un uso real, lo mejor es eliminar la función.

2. **`buscar_usuario` devuelve `None` en silencio** cuando no encuentra el id (línea 3-6). Quien la llame y haga `usuario["nombre"]` recibirá un `TypeError` poco claro. Puedes devolver `None` de forma explícita y documentarlo, o lanzar una excepción como `LookupError`.

3. **El parámetro `id` tapa la función integrada `id()`**. No rompe nada aquí, pero conviene renombrarlo a `usuario_id`.

4. Si algún diccionario no tiene la clave `"id"`, `usuario["id"]` lanza `KeyError`. Podrías usar `usuario.get("id")`.

Una versión corregida de `buscar_usuario`:

```python
def buscar_usuario(usuarios, usuario_id):
    for usuario in usuarios:
        if usuario.get("id") == usuario_id:
            return usuario
    return None
```

¿Qué te está fallando en concreto? Si tienes un error, un traceback o un resultado inesperado, pégalo y lo reviso. Si quieres que aplique estos cambios al archivo, dímelo y lo hago.
