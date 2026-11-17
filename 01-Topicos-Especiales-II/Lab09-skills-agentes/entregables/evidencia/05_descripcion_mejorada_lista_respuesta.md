# Qué es una lista en Python

Una lista es una colección **ordenada** y **modificable** de elementos. Se escribe entre corchetes `[]`, con los elementos separados por comas.

- **Ordenada:** cada elemento tiene una posición (índice) y el primero es el 0.
- **Modificable:** puedes agregar, quitar o cambiar elementos después de crearla.
- **Admite tipos mezclados:** puede tener números, texto, otras listas, etc.
- **Admite repetidos:** el mismo valor puede aparecer varias veces.

## Ejemplo 1: crear y acceder a elementos

```python
frutas = ["manzana", "banana", "naranja"]

print(frutas[0])    # manzana (primer elemento)
print(frutas[-1])   # naranja (último elemento)
print(len(frutas))  # 3 (cantidad de elementos)
```

## Ejemplo 2: agregar, modificar y eliminar

```python
numeros = [10, 20, 30]

numeros.append(40)      # [10, 20, 30, 40]
numeros[1] = 25         # [10, 25, 30, 40]
numeros.remove(30)      # [10, 25, 40]

print(numeros)
```

## Ejemplo 3: recorrer una lista con un ciclo

```python
notas = [85, 90, 78, 92]

total = 0
for nota in notas:
    total += nota

promedio = total / len(notas)
print(f"Promedio: {promedio}")  # Promedio: 86.25
```

**Otros métodos útiles:** `insert()`, `pop()`, `sort()`, `reverse()` y `index()`. También puedes cortar listas con *slicing*, por ejemplo `notas[1:3]` devuelve `[90, 78]`.
