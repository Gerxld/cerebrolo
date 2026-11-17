import re, sys
raw, out, preg, ini, fin = sys.argv[1:]
t = open(raw, encoding="utf-8", errors="replace").read()
t = re.sub(r"\x1b\[[0-9;?]*[A-Za-z]", "", t)
t = re.sub(r"[\u2800-\u28ff]\s*", "", t).replace("\r", "").strip()
B = chr(92)
OLLAMA = B.join(["C:", "Users", "HOME", "AppData", "Local", "Programs", "Ollama", "ollama.exe"])
cab = "Comando: " + OLLAMA + " run qwen2.5:3b \"" + preg + "\"   (sin documentos, sin RAG)"
with open(out, "w", encoding="utf-8") as f:
    f.write(cab + "\nHora de inicio: " + ini + "\n" + "-" * 40 + "\n" + t + "\n" + "-" * 40 + "\nHora de fin: " + fin + "\n")
