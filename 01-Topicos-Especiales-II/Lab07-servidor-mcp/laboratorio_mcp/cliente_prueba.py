"""Cliente de prueba por stdio: lista lo que declara server.py y llama cada capacidad."""
import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

params = StdioServerParameters(command=sys.executable, args=["server.py"])


def mostrar(titulo: str, valor) -> None:
    print(f"\n--- {titulo}")
    print(valor)


async def main() -> None:
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            info = await session.initialize()
            mostrar("initialize", f"servidor={info.server_info.name} protocolo={info.protocol_version}")

            tools = await session.list_tools()
            mostrar("tools/list", [t.name for t in tools.tools])
            recursos = await session.list_resources()
            mostrar("resources/list", [str(r.uri) for r in recursos.resources])
            plantillas = await session.list_resource_templates()
            mostrar("resources/templates/list", [t.uri_template for t in plantillas.resource_templates])
            prompts = await session.list_prompts()
            mostrar("prompts/list", [p.name for p in prompts.prompts])

            r = await session.call_tool("calcular_promedio", {"notas": [90, 80, 100]})
            mostrar("calcular_promedio [90, 80, 100]", f"is_error={r.is_error} structured={r.structured_content} texto={r.content[0].text!r}")
            r = await session.call_tool("calcular_promedio", {"notas": [95, 120]})
            mostrar("calcular_promedio [95, 120]", f"is_error={r.is_error} texto={r.content[0].text!r}")
            r = await session.call_tool("calcular_promedio", {"notas": []})
            mostrar("calcular_promedio []", f"is_error={r.is_error} texto={r.content[0].text!r}")

            for promedio in (90, 71, 65, 150):
                r = await session.call_tool("estado_estudiante", {"promedio": promedio})
                mostrar(f"estado_estudiante {promedio}", f"is_error={r.is_error} texto={r.content[0].text!r}")

            leido = await session.read_resource("curso://reglas-entrega")
            mostrar("resources/read curso://reglas-entrega", leido.contents[0].text)
            leido = await session.read_resource("curso://estudiante/Gerald")
            mostrar("resources/read curso://estudiante/Gerald", leido.contents[0].text)

            p = await session.get_prompt("revisar_codigo", {"codigo": "def f(x): return x / 0"})
            mostrar("prompts/get revisar_codigo", f"role={p.messages[0].role}\n{p.messages[0].content.text}")


asyncio.run(main())
