"""Paso 26: herramienta nueva (contar_pruebas) registrada sobre el agente del laboratorio.

No se toca agente_proyecto.py: aqui se agrega la herramienta al diccionario
HERRAMIENTAS del mismo modulo y se reutiliza ejecutar_agente tal cual.
"""
import re

import agente_proyecto as ap


def contar_pruebas() -> str:
    """Cuenta cuántas pruebas unittest hay en el proyecto, por archivo.

    Una prueba es un método cuyo nombre empieza por test_ dentro de un
    archivo test_*.py. No recibe argumentos.
    """
    lineas = []
    total = 0
    for ruta in sorted(ap.BASE.rglob("test_*.py")):
        contenido = ruta.read_text(encoding="utf-8")
        nombres = re.findall(r"^\s*def (test_\w+)\(", contenido, flags=re.M)
        total += len(nombres)
        lineas.append(f"{ruta.relative_to(ap.BASE)}: {len(nombres)} pruebas ({', '.join(nombres)})")
    lineas.append(f"TOTAL: {total}")
    return "\n".join(lineas)


ap.HERRAMIENTAS["contar_pruebas"] = contar_pruebas

if __name__ == "__main__":
    objetivo = input("Objetivo para el agente: ").strip()
    ap.ejecutar_agente(objetivo)
