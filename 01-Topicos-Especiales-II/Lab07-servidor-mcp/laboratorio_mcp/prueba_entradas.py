"""Entradas incómodas contra server.py: qué acepta y qué rechaza el servidor tal como está."""
import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

params = StdioServerParameters(command=sys.executable, args=["server.py"])


async def llamar(session, nombre, args, etiqueta):
    r = await session.call_tool(nombre, args)
    texto = r.content[0].text if r.content else ""
    print(f"{etiqueta}\n  -> is_error={r.is_error} texto={texto[:120]!r}")


async def leer(session, uri, etiqueta):
    try:
        r = await session.read_resource(uri)
        t = r.contents[0].text
        if len(t) > 150:
            print(f"{etiqueta}\n  -> {t[:40]!r}... ({len(t)} caracteres en total)")
        else:
            print(f"{etiqueta}\n  -> {t!r}")
    except Exception as e:
        print(f"{etiqueta}\n  -> excepción {type(e).__name__}: {str(e)[:120]}")


async def main() -> None:
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("== calcular_promedio")
            await llamar(session, "calcular_promedio", {"notas": ["90", "80"]}, 'notas como texto ["90", "80"]')
            await llamar(session, "calcular_promedio", {"notas": [True, False]}, "notas booleanas [true, false]")
            await llamar(session, "calcular_promedio", {"notas": [100.0] * 1_000_000}, "lista de 1 000 000 de notas")
            await llamar(session, "calcular_promedio", {"notas": [-0.01, 50]}, "nota -0.01")
            await llamar(session, "estado_estudiante", {"promedio": 70.99}, "estado_estudiante 70.99 (umbral 71)")
            print("\n== curso://estudiante/{nombre}")
            await leer(session, "curso://estudiante/Ana", "nombre normal")
            await leer(session, "curso://estudiante/Ana%0AEstado:%20graduado", "nombre con salto de línea codificado (%0A)")
            await leer(session, "curso://estudiante/..%2F..%2Fsecreto.txt", "nombre tipo ruta (..%2F..%2Fsecreto.txt)")
            await leer(session, "curso://estudiante/" + "A" * 5000, "nombre de 5000 caracteres")
            await leer(session, "curso://estudiante/", "nombre vacío")


asyncio.run(main())
