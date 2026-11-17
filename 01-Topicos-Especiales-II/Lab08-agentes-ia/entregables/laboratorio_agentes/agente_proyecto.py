from pathlib import Path
from ollama import chat

MODELO = "qwen3:4b"
BASE = Path("proyecto").resolve()
REPORTES = Path("reportes").resolve()


def ruta_segura(nombre: str) -> Path:
    ruta = (BASE / nombre).resolve()
    if BASE not in ruta.parents and ruta != BASE:
        raise ValueError("Ruta fuera de la carpeta autorizada")
    return ruta


def listar_archivos() -> str:
    """Lista los archivos disponibles en el proyecto."""
    archivos = [
        str(p.relative_to(BASE))
        for p in BASE.rglob("*")
        if p.is_file()
    ]
    return "\n".join(sorted(archivos))


def leer_archivo(nombre: str) -> str:
    """Lee un archivo de texto dentro del proyecto.

    Args:
        nombre: Ruta relativa del archivo dentro del proyecto.
    """
    ruta = ruta_segura(nombre)
    if not ruta.is_file():
        return "Archivo no encontrado"
    return ruta.read_text(encoding="utf-8")


def buscar_texto(texto: str) -> str:
    """Busca texto en todos los archivos del proyecto.

    Args:
        texto: Texto que se desea encontrar.
    """
    resultados = []
    for ruta in BASE.rglob("*.py"):
        contenido = ruta.read_text(encoding="utf-8")
        for numero, linea in enumerate(contenido.splitlines(), 1):
            if texto.lower() in linea.lower():
                resultados.append(
                    f"{ruta.relative_to(BASE)}:{numero}: {linea.strip()}"
                )
    return "\n".join(resultados) if resultados else "Sin coincidencias"


def guardar_reporte(nombre: str, contenido: str) -> str:
    """Guarda un reporte Markdown dentro de la carpeta reportes.

    Args:
        nombre: Nombre del archivo sin rutas.
        contenido: Contenido del reporte.
    """
    nombre = Path(nombre).name
    if not nombre.endswith(".md"):
        nombre += ".md"

    ruta = REPORTES / nombre
    ruta.write_text(contenido, encoding="utf-8")
    return f"Reporte guardado en {ruta}"


HERRAMIENTAS = {
    "listar_archivos": listar_archivos,
    "leer_archivo": leer_archivo,
    "buscar_texto": buscar_texto,
    "guardar_reporte": guardar_reporte,
}

INSTRUCCIONES = """
Eres un agente de análisis de proyectos de software.

Objetivo:
resolver solicitudes utilizando únicamente la evidencia disponible
en la carpeta del proyecto.

Reglas:
- utiliza herramientas cuando necesites inspeccionar el proyecto;
- no inventes archivos ni contenido;
- no intentes acceder fuera de la carpeta autorizada;
- antes de guardar un reporte, reúne la evidencia necesaria;
- cuando el objetivo esté completo, responde claramente y termina.
"""


def ejecutar_agente(objetivo: str, max_iteraciones: int = 8):
    mensajes = [
        {"role": "system", "content": INSTRUCCIONES},
        {"role": "user", "content": objetivo},
    ]

    herramientas = list(HERRAMIENTAS.values())

    for iteracion in range(1, max_iteraciones + 1):
        print(f"\n--- Iteración {iteracion} ---")

        respuesta = chat(
            model=MODELO,
            messages=mensajes,
            tools=herramientas,
            think=False,
        )

        mensajes.append(respuesta.message)

        if not respuesta.message.tool_calls:
            print("\nRESPUESTA FINAL:")
            print(respuesta.message.content)
            return respuesta.message.content

        for llamada in respuesta.message.tool_calls:
            nombre = llamada.function.name
            argumentos = llamada.function.arguments

            print(f"Herramienta: {nombre}")
            print(f"Argumentos: {argumentos}")

            if nombre not in HERRAMIENTAS:
                resultado = "Herramienta no autorizada"
            else:
                try:
                    resultado = HERRAMIENTAS[nombre](**argumentos)
                except Exception as e:
                    resultado = f"ERROR: {e}"

            print(f"Observación: {resultado}")

            mensajes.append({
                "role": "tool",
                "tool_name": nombre,
                "content": str(resultado),
            })

    return "El agente alcanzó el máximo de iteraciones."


if __name__ == "__main__":
    objetivo = input("Objetivo para el agente: ").strip()
    ejecutar_agente(objetivo)
