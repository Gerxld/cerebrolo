"""Paso 25: la misma pregunta sobre el proyecto, sin herramientas ni contexto."""
from ollama import chat

MODELO = "qwen3:4b"

respuesta = chat(
    model=MODELO,
    messages=[{
        "role": "user",
        "content": "¿En qué archivo se valida el email de este proyecto?"
    }],
)
print(respuesta.message.content)
