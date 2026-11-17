"""Paso 23 (complemento): prueba directa de ruta_segura, sin modelo de por medio."""
import agente_proyecto as ap

casos = [
    "usuarios.py",
    "../secreto.txt",
    r"..\secreto.txt",
    "subcarpeta/../../secreto.txt",
    str(ap.BASE.parent / "secreto.txt"),
    r"C:\Windows\win.ini",
    ".",
]
for c in casos:
    try:
        print(f"ruta_segura({c!r}) -> {ap.ruta_segura(c)}")
    except ValueError as e:
        print(f"ruta_segura({c!r}) -> ERROR: {e}")
