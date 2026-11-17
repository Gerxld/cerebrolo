# laboratorio_mcp

Servidor MCP `AsistenteAcademico` (Lab 7, Tópicos Especiales II).

## Requisitos
Python 3.13, uv, Node.js/npx.

## Uso
```
uv sync
uv run mcp dev server.py          # abre MCP Inspector
uv run python cliente_prueba.py   # cliente de respaldo (stdio)
uv run python prueba_entradas.py  # entradas incómodas (análisis de seguridad)
```

## Contenido
- Tools: `calcular_promedio`, `estado_estudiante`
- Resources: `curso://reglas-entrega`, `curso://estudiante/{nombre}`
- Prompt: `revisar_codigo`
