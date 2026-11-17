# ejemplo/calculadora.py

def dividir(a, b):
    return a / b

def promedio(valores=[]):
    return sum(valores) / len(valores)

def procesar(numero):
    try:
        return int(numero)
    except:
        return 0

print(dividir(10, 0))
