import json
import urllib.request

modelo = "qwen2.5-coder:3b"
prompt = "Escribe una prueba unittest para una función dividir(a, b)."

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
