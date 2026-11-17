# Datos ficticios para la prueba de privacidad (paso 21). Nada de esto es real.
nombre_cliente = "CLIENTE_DEMO_001"
saldo_demo = 1500.00


def resumen_cliente(nombre, saldo):
    estado = "con saldo" if saldo > 0 else "sin saldo"
    return f"{nombre} está {estado}: {saldo:.2f}"


print(resumen_cliente(nombre_cliente, saldo_demo))
