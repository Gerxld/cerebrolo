Usa `int()` sobre cada elemento. Hay dos formas habituales:

```python
cadenas = ["1", "2", "3", "42"]

# Con list comprehension
enteros = [int(c) for c in cadenas]

# Con map
enteros = list(map(int, cadenas))

print(enteros)  # [1, 2, 3, 42]
```

Si alguna cadena puede no ser un número válido, `int()` lanza `ValueError`. Para manejarlo, puedes filtrar o capturar el error:

```python
cadenas = ["1", "dos", "3", " 4 ", ""]

enteros = []
for c in cadenas:
    try:
        enteros.append(int(c))
    except ValueError:
        print(f"Se omite {c!r}: no es un entero válido")

print(enteros)  # [1, 3, 4]
```

Ten en cuenta lo siguiente:
- `int()` ignora los espacios alrededor (`" 4 "` pasa a `4`), pero falla con la cadena vacía y con decimales como `"3.5"`.
- Para `"3.5"`, convierte primero a `float` (`int(float("3.5"))`, que da `3`) si de verdad quieres truncar.
- Si los números vienen en otra base, pásala como segundo argumento: `int("ff", 16)` da `255`.
