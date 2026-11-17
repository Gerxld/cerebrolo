from datetime import date, timedelta


def _texto_limpio(valor):
    if not isinstance(valor, str):
        raise ValueError("el valor debe ser texto")
    valor = valor.strip()
    if not valor:
        raise ValueError("el texto no puede estar vacío")
    return valor


def _fecha_valida(fecha):
    if not isinstance(fecha, str):
        raise ValueError("la fecha debe ser texto AAAA-MM-DD")
    forma_ok = (
        len(fecha) == 10
        and fecha[4] == "-"
        and fecha[7] == "-"
        and all(c in "0123456789" for c in fecha[:4] + fecha[5:7] + fecha[8:])
    )
    if not forma_ok:
        raise ValueError("formato de fecha inválido, use AAAA-MM-DD")
    return date.fromisoformat(fecha)  # ValueError si no existe en el calendario


def _libro_esta_activo(prestamos, libro):
    return any(p["libro"] == libro and not p["devuelto"] for p in prestamos)


def _contar_activos(prestamos, usuario):
    return sum(1 for p in prestamos if p["usuario"] == usuario and not p["devuelto"])


def registrar_prestamo(prestamos, usuario, libro, fecha):
    usuario = _texto_limpio(usuario)
    libro = _texto_limpio(libro)
    inicio = _fecha_valida(fecha)
    try:
        vence = inicio + timedelta(days=14)
    except OverflowError:
        raise ValueError("el vencimiento supera 9999-12-31") from None
    if _libro_esta_activo(prestamos, libro):
        raise ValueError("el libro ya tiene un préstamo activo")
    if _contar_activos(prestamos, usuario) >= 3:
        raise ValueError("el usuario ya tiene 3 préstamos activos")
    prestamo = {
        "usuario": usuario,
        "libro": libro,
        "fecha_prestamo": fecha,
        "fecha_vencimiento": vence.isoformat(),
        "devuelto": False,
    }
    prestamos.append(prestamo)
    return prestamo

def devolver_prestamo(prestamos, usuario, libro):
    usuario = _texto_limpio(usuario)
    libro = _texto_limpio(libro)
    for prestamo in prestamos:
        if (
            prestamo["usuario"] == usuario
            and prestamo["libro"] == libro
            and not prestamo["devuelto"]
        ):
            prestamo["devuelto"] = True
            return prestamo
    raise ValueError("no existe un préstamo activo de ese libro para el usuario")
