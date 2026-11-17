def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero.")
    return a / b

def promedio(valores):
    if not valores:
        raise ValueError("La lista de valores no puede estar vacía.")
    return sum(valores) / len(valores)

def porcentaje(valor, total):
    if total == 0:
        raise ValueError("El total no puede ser cero.")
    return (valor / total) * 100

def mediana(valores):
    if not valores:
        raise ValueError("La lista de valores no puede estar vacía.")

    valores_ordenados = sorted(valores)
    n = len(valores_ordenados)

    if n % 2 == 1:
        # Cantidad impar de elementos
        return valores_ordenados[n // 2]
    else:
        # Cantidad par de elementos
        medio1 = valores_ordenados[n // 2 - 1]
        medio2 = valores_ordenados[n // 2]
        return (medio1 + medio2) / 2
