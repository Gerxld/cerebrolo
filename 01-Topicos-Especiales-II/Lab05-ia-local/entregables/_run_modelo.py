# -*- coding: utf-8 -*-
"""Ejecuta `ollama run <modelo>` con un prompt (por stdin) y guarda evidencia completa.
Uso: py _run_modelo.py NN_nombre prompt.txt [--titulo "texto"]
El prompt exacto queda en el .txt de evidencia, junto con comando, horas y duracion."""
import subprocess, sys, re, time, datetime
from pathlib import Path
OLLAMA = str(Path.home() / "AppData/Local/Programs/Ollama/ollama.exe")
MODELO = "qwen2.5-coder:3b"
EV = Path(__file__).parent / "laboratorio_local_privado" / "evidencia"
ANSI = re.compile(r"\x1b\[[0-9;?]*[A-Za-z]|\x1b\][^\x07]*\x07")

def main():
    nombre, pfile = sys.argv[1], Path(sys.argv[2])
    prompt = pfile.read_text(encoding="utf-8").strip("\n")
    t0 = time.time(); ini = datetime.datetime.now()
    r = subprocess.run([OLLAMA, "run", MODELO], input=prompt.encode("utf-8"),
                       capture_output=True)
    dur = time.time() - t0; fin = datetime.datetime.now()
    out = ANSI.sub("", r.stdout.decode("utf-8", "replace")).replace("\r", "")
    err = ANSI.sub("", r.stderr.decode("utf-8", "replace")).replace("\r", "").strip()
    txt = (f"Fecha y hora de inicio: {ini:%Y-%m-%d %H:%M:%S}\n"
           f"Comando: {OLLAMA} run {MODELO}   (prompt entregado por entrada estandar)\n"
           f"{'-'*60}\nPROMPT ENVIADO:\n{prompt}\n{'-'*60}\nRESPUESTA DEL MODELO:\n{out.strip()}\n"
           f"{'-'*60}\n" + (f"stderr: {err[-300:]}\n" if err and not err.startswith("failed") and len(err) > 3 and "pulling" in err else "")
           + f"Codigo de salida: {r.returncode}\n"
           f"Fecha y hora de fin: {fin:%Y-%m-%d %H:%M:%S}\nTiempo transcurrido: {dur:.1f} s\n")
    (EV / f"{nombre}.txt").write_text(txt, encoding="utf-8")
    print(f"{nombre}: {dur:.1f} s, {len(out)} caracteres")
main()
