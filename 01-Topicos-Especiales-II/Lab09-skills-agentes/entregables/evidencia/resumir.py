"""Convierte la salida stream-json de `claude -p` en un resumen legible.
Uso: python resumir.py entrada.jsonl salida.txt [informe.md]"""
import json, sys

entrada, salida = sys.argv[1], sys.argv[2]
informe = sys.argv[3] if len(sys.argv) > 3 else None
lineas, final, skills, tools = [], "", [], []
with open(entrada, encoding="utf-8") as f:
    for n, raw in enumerate(f, 1):
        ev = json.loads(raw)
        t = ev.get("type")
        if t == "system" and ev.get("subtype") == "init":
            lineas.append(f"[linea {n}] init: model={ev.get('model')} cwd={ev.get('cwd')}")
            lineas.append(f"[linea {n}] skills disponibles: {ev.get('skills')}")
        elif t == "assistant":
            for b in ev["message"]["content"]:
                if b["type"] == "tool_use":
                    inp = json.dumps(b["input"], ensure_ascii=False)
                    lineas.append(f"[linea {n}] TOOL_USE {b['name']}: {inp[:300]}")
                    tools.append(b["name"])
                    if b["name"] == "Skill":
                        skills.append((n, b["input"].get("skill")))
                elif b["type"] == "text" and b["text"].strip():
                    lineas.append(f"[linea {n}] ASISTENTE: {b['text'][:200].strip()}...")
        elif t == "user":
            c = ev["message"]["content"]
            if isinstance(c, list):
                for b in c:
                    if b.get("type") == "tool_result":
                        r = b.get("content")
                        if isinstance(r, list):
                            r = " ".join(x.get("text", "") for x in r)
                        lineas.append(f"[linea {n}] TOOL_RESULT: {str(r)[:200].strip()}")
        elif t == "result":
            final = ev.get("result", "")
            lineas.append(f"[linea {n}] RESULT: turns={ev.get('num_turns')} costo_usd={ev.get('total_cost_usd')}")
lineas.append("")
lineas.append(f"Herramientas usadas: {tools}")
lineas.append(f"Skill invocada: {skills if skills else 'NINGUNA'}")
lineas.append("")
lineas.append("=== RESPUESTA FINAL ===")
lineas.append(final)
open(salida, "w", encoding="utf-8").write("\n".join(lineas) + "\n")
if informe:
    open(informe, "w", encoding="utf-8").write(final + "\n")
