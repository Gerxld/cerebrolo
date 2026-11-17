from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError

mcp = MCPServer("AsistenteAcademico")


@mcp.tool()
def calcular_promedio(notas: list[float]) -> float:
    """Calcula el promedio de una lista de notas entre 0 y 100."""
    if not notas:
        raise ToolError("Debe proporcionar al menos una nota")
    if any(n < 0 or n > 100 for n in notas):
        raise ToolError("Las notas deben estar entre 0 y 100")
    return round(sum(notas) / len(notas), 2)


@mcp.tool()
def estado_estudiante(promedio: float) -> str:
    """Clasifica el estado académico a partir del promedio."""
    if promedio < 0 or promedio > 100:
        raise ToolError("Promedio fuera de rango")
    return "APROBADO" if promedio >= 71 else "REPROBADO"


@mcp.resource("curso://reglas-entrega")
def reglas_entrega() -> str:
    """Reglas vigentes para entregar laboratorios."""
    return (
        "1. Entregar código fuente.\n"
        "2. Incluir README con instrucciones.\n"
        "3. No incluir contraseñas ni claves API.\n"
        "4. Ejecutar pruebas antes de entregar."
    )


@mcp.resource("curso://estudiante/{nombre}")
def ficha_estudiante(nombre: str) -> str:
    """Devuelve una ficha académica de ejemplo."""
    return f"Estudiante: {nombre}\nCurso: Desarrollo con IA\nEstado: activo"


@mcp.prompt()
def revisar_codigo(codigo: str) -> str:
    """Construye una solicitud de revisión de código para un estudiante."""
    return (
        "Revisa el siguiente código como docente. "
        "Identifica errores, riesgos y una mejora concreta.\n\n"
        f"{codigo}"
    )


if __name__ == "__main__":
    mcp.run()
