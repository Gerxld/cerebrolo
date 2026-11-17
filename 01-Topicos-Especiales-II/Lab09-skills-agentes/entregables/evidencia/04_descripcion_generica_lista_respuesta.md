# Qué es una lista en Python

Una **lista** es una colección ordenada y modificable de elementos. Se escribe entre corchetes `[ ]`, con los elementos separados por comas.

- **Ordenada:** cada elemento tiene una posición (índice), y el primero es el 0.
- **Modificable:** puedes agregar, quitar o cambiar elementos después de crearla.
- **Heterogénea:** puede mezclar tipos (números, textos, otras listas).
- **Admite repetidos:** el mismo valor puede aparecer varias veces.

## Ejemplo 1: crear una lista y acceder a sus elementos

```python
frutas = ["manzana", "banana", "naranja"]

print(frutas[0])    # manzana
print(frutas[-1])   # naranja (el índice negativo cuenta desde el final)
print(len(frutas))  # 3
```

## Ejemplo 2: agregar, modificar y quitar

```python
numeros = [10, 20, 30]

numeros.append(40)      # [10, 20, 30, 40]
numeros[1] = 25         # [10, 25, 30, 40]
numeros.remove(10)      # [25, 30, 40]

print(numeros)
```

## Ejemplo 3: recorrerla con un ciclo

```python
notas = [85, 90, 78, 92]

total = 0
for nota in notas:
    total += nota

print("Promedio:", total / len(notas))  # Promedio: 86.25
```

## Métodos que más vas a usar

| Método | Qué hace |
|---|---|
| `append(x)` | Agrega `x` al final |
| `insert(i, x)` | Inserta `x` en la posición `i` |
| `remove(x)` | Quita la primera aparición de `x` |
| `pop(i)` | Quita y devuelve el elemento en `i` (el último si no pasas índice) |
| `sort()` | Ordena la lista en el mismo lugar |
| `len(lista)` | Cuenta los elementos |

Si quieres, te preparo ejercicios para practicar o te explico la diferencia con tuplas y diccionarios.
