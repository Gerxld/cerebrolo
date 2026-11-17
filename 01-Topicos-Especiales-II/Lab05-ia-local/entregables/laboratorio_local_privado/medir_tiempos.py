import json, time, urllib.request
from pathlib import Path

MODELO = "qwen2.5-coder:3b"
codigo = Path(__file__).with_name("calculadora.py").read_text(encoding="utf-8")
PRUEBAS = [
    ("corta", "Dime en una frase qué hace la función sum en Python."),
    ("calculadora.py", "Actúa como revisor de código Python. Analiza el siguiente código y detecta casos límite o errores. "
                       "No cambies los nombres de las funciones.\n\n" + codigo),
]

def consultar(prompt):
    data = json.dumps({"model": MODELO, "prompt": prompt, "stream": False}).encode("utf-8")
    req = urllib.request.Request("http://localhost:11434/api/generate", data=data,
                                 headers={"Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req) as r:
        res = json.loads(r.read().decode("utf-8"))
    return time.time() - t0, res

for ronda in (1, 2):
    for nombre, prompt in PRUEBAS:
        seg, res = consultar(prompt)
        toks = res.get("eval_count", 0)
        ev = res.get("eval_duration", 1) / 1e9
        print(f"ronda {ronda} | {nombre:15s} | prompt={res.get('prompt_eval_count')} tokens | "
              f"respuesta={toks} tokens | total={seg:5.1f} s | carga={res.get('load_duration',0)/1e9:4.1f} s | "
              f"generacion={toks/ev:4.1f} tokens/s")
        if ronda == 1:
            print("   respuesta:", res["response"].strip().replace("\n", "\n   ")[:600])
