# -*- coding: utf-8 -*-
"""Renderiza un .txt de evidencia como terminal oscura y lo guarda como PNG (Playwright)."""
import sys, html, re
from pathlib import Path
from playwright.sync_api import sync_playwright

def render(txt, png, titulo, ancho=1000, chunk=1050, maxchunks=None):
    texto = Path(txt).read_text(encoding="utf-8")
    lineas = []
    for l in texto.splitlines():
        e = html.escape(l)
        if l.startswith("--- CHUNKS") or l.startswith("--- RESPUESTA"):
            e = f'<span class="it">{e}</span>'
        elif l.startswith("Comando:") or l.startswith("Hora de"):
            e = f'<span class="arg">{e}</span>'
        elif re.match(r"^\d\. \S+\.txt \| similitud", l):
            e = f'<span class="tool">{e}</span>'
        elif re.search(r"No encuentro esa información", l):
            e = f'<span class="ok">{e}</span>'
        elif re.search(r"Traceback|Error|ERROR", l):
            e = f'<span class="err">{e}</span>'
        lineas.append(e)
    doc = f"""<html><head><meta charset="utf-8"><style>
body{{margin:0;background:#0c0c0c;}}
.barra{{background:#2d2d2d;color:#ddd;font:13px Segoe UI,Arial;padding:6px 12px;}}
pre{{margin:0;padding:12px 14px;color:#cccccc;font:14px/1.35 Consolas,'Courier New',monospace;white-space:pre-wrap;word-break:break-word;width:{ancho-28}px}}
.it{{color:#f9f1a5;font-weight:bold}} .tool{{color:#3a96dd}} .arg{{color:#61d6d6}} .err{{color:#f14c4c}} .ok{{color:#16c60c}}
</style></head><body><div class="barra">{html.escape(titulo)}</div><pre>{chr(10).join(lineas)}</pre></body></html>"""
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": ancho, "height": 400})
        pg.set_content(doc)
        h = pg.evaluate("document.documentElement.scrollHeight")
        n = max(1, -(-h // chunk))
        if maxchunks: n = min(n, maxchunks)
        rutas = []
        for i in range(n):
            ruta = f"{png}_{i+1}.png" if n > 1 else f"{png}.png"
            pg.screenshot(path=ruta, full_page=True, clip={"x": 0, "y": i*chunk, "width": ancho, "height": min(chunk, h - i*chunk)})
            rutas.append(ruta)
        b.close()
        return rutas

if __name__ == "__main__":
    ev = Path("laboratorio_rag/evidencia")
    # (archivo sin .txt, nombre de la captura, título de la barra)
    trabajos = [l.split("|") for l in Path("_capturas.lista").read_text(encoding="utf-8").splitlines() if l.strip()]
    for f, out, t in trabajos:
        if not (ev / f"{f}.txt").exists(): continue
        print(render(ev / f"{f}.txt", f"screenshots/{out}", t))
