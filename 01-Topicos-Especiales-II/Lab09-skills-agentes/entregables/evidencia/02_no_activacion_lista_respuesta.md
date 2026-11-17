# Qué es una lista en Python

Una lista es una colección **ordenada** y **modificable** de elementos. Se escribe entre corchetes `[]` y separa los elementos con comas. Sus características principales son estas:

- **Ordenada:** cada elemento tiene una posición (índice) que empieza en 0.
- **Mutable:** puedes agregar, quitar o cambiar elementos después de crearla.
- **Heterogénea:** puede mezclar tipos de datos (números, textos, otras listas).
- **Permite repetidos:** el mismo valor puede aparecer varias veces.

## Ejemplo 1: crear y acceder a elementos

```python
frutas = ["manzana", "banano", "naranja"]

print(frutas[0])    # manzana (primer elemento)
print(frutas[-1])   # naranja (último elemento)
print(len(frutas))  # 3
```

## Ejemplo 2: modificar la lista

```python
numeros = [10, 20, 30]

numeros.append(40)      # agrega al final -> [10, 20, 30, 40]
numeros[1] = 25         # cambia un valor -> [10, 25, 30, 40]
numeros.remove(10)      # elimina un valor -> [25, 30, 40]

print(numeros)          # [25, 30, 40]
```

## Ejemplo 3: recorrer una lista con un ciclo

```python
notas = [85, 90, 78, 92]

suma = 0
for nota in notas:
    suma += nota

promedio = suma / len(notas)
print(f"Promedio: {promedio}")  # Promedio: 86.25
```

## Resumen de métodos comunes

| Método | Qué hace |
|---|---|
| `append(x)` | Agrega `x` al final |
| `insert(i, x)` | Inserta `x` en la posición `i` |
| `remove(x)` | Elimina la primera aparición de `x` |
| `pop()` | Quita y devuelve el último elemento |
| `sort()` | Ordena la lista |
| `len(lista)` | Devuelve la cantidad de elementos |
