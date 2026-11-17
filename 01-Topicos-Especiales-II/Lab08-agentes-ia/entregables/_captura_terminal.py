# -*- coding: utf-8 -*-
"""Renderiza un .txt de evidencia como pagina de terminal oscura y la guarda como PNG."""
import sys, html, re
from pathlib import Path
from playwright.sync_api import sync_playwright

def render(txt, png, titulo, ancho=1000, chunk=1050, maxchunks=None):
    texto = Path(txt).read_text(encoding="utf-8")
    lineas = []
    for l in texto.splitlines():
        e = html.escape(l)
        if re.match(r"^--- Iteración \d+ ---", l) or l.startswith("RESPUESTA FINAL"):
            e = f'<span class="it">{e}</span>'
        elif l.startswith("Herramienta:"):
            e = f'<span class="tool">{e}</span>'
        elif l.startswith("Argumentos:"):
            e = f'<span class="arg">{e}</span>'
        elif re.search(r"ERROR|Ruta fuera|no autorizada", l):
            e = f'<span class="err">{e}</span>'
        elif re.search(r"\bOK\b|guardado", l):
            e = f'<span class="ok">{e}</span>'
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
            ruta = f"{png}_{i+1}.png" if (n > 1 or maxchunks) else f"{png}.png"
            pg.screenshot(path=ruta, full_page=True, clip={"x": 0, "y": i*chunk, "width": ancho, "height": min(chunk, h - i*chunk)})
            rutas.append(ruta)
        b.close()
        return rutas

if __name__ == "__main__":
    ev = Path("laboratorio_agentes/evidencia")
    trabajos = [
        ("01_02_04_entorno", "01_entorno", "Pasos 1, 2 y 4", None),
        ("07_pruebas_del_proyecto", "02_pruebas", "Paso 7", None),
        ("18_ejecucion_principal_intento1", "03_ejec18_intento1", "Paso 18, intento 1", None),
        ("18b_ejecucion_principal_intento2", "04_ejec18_intento2", "Paso 18, intento 2", None),
        ("21_objetivo_simple_valueerror", "05_paso21", "Paso 21", 1),
        ("22_informacion_inexistente", "06_paso22", "Paso 22", None),
        ("23_ruta_fuera_de_proyecto", "07_paso23", "Paso 23", 1),
        ("23b_prueba_directa_ruta_segura", "08_paso23b", "Paso 23, prueba directa", None),
        ("24_limite_max_iteraciones", "09_paso24", "Paso 24", None),
        ("25_llamada_sin_herramientas", "10_paso25", "Paso 25", None),
        ("26_herramienta_nueva_contar_pruebas", "11_paso26", "Paso 26", 1),
        ("27_reto_autonomo_intento1", "12_paso27_intento1", "Paso 27, intento 1", 1),
        ("27b_reto_autonomo_intento2", "13_paso27_intento2", "Paso 27, intento 2", None),
    ]
    filtro = sys.argv[1:] 
    for f, out, t, mc in trabajos:
        if filtro and out not in filtro: continue
        if not (ev / f"{f}.txt").exists(): continue
        print(render(ev / f"{f}.txt", f"screenshots/{out}", t, maxchunks=mc))
