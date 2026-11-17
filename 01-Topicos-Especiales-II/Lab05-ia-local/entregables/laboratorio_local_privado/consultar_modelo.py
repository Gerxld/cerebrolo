import json
import urllib.request
from pathlib import Path

modelo = "qwen2.5-coder:3b"

# Paso 20: el código se lee desde calculadora.py y se arma el prompt de revisión
codigo = Path(__file__).with_name("calculadora.py").read_text(encoding="utf-8")
prompt = (
    "Actúa como revisor de código Python. "
    "Revisa el siguiente código y dime en pocas líneas si todavía le falta "
    "algún caso límite. No lo reescribas completo.\n\n" + codigo
)

# Verificación previa: qué se va a entregar al modelo (primeros 100 caracteres)
print("Primeros 100 caracteres del prompt:")
print(repr(prompt[:100]))
print("-" * 40)

data = json.dumps({
    "model": modelo,
    "prompt": prompt,
    "stream": False
}).encode("utf-8")

request = urllib.request.Request(
    "http://localhost:11434/api/generate",
    data=data,
    headers={"Content-Type": "application/json"}
)

with urllib.request.urlopen(request) as response:
    resultado = json.loads(response.read().decode("utf-8"))

print(resultado["response"])
