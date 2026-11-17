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
