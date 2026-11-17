# -*- coding: utf-8 -*-
"""Renderiza los .txt de evidencia como terminal oscura y los guarda como PNG (screenshots/).
Uso: py -3.14 _captura_terminal.py [nombre_png ...]   (sin argumentos: todas las que tengan evidencia)"""
import sys, html, re
from pathlib import Path
from playwright.sync_api import sync_playwright

AQUI = Path(__file__).parent
EV = AQUI / "laboratorio_local_privado" / "evidencia"
OUT = AQUI / "screenshots"

def render(txt, png, titulo, ancho=1000, chunk=1050):
    texto = Path(txt).read_text(encoding="utf-8-sig")
    lineas = []
    for l in texto.splitlines():
        e = html.escape(l)
        if re.match(r"^(PROMPT ENVIADO:|RESPUESTA DEL MODELO:|===)", l):
            e = f'<span class="it">{e}</span>'
        elif re.match(r"^(PS>|>|Comando:)", l):
            e = f'<span class="tool">{e}</span>'
        elif re.match(r"^(ERROR:|FAIL:|FAILED|ATENCION|Fallo|Traceback|\w+Error:|\w+Error.*!=)", l):
            e = f'<span class="err">{e}</span>'
        elif re.search(r"\bOK\b|\.\.\. ok|Listo\.", l):
            e = f'<span class="ok">{e}</span>'
        lineas.append(e)
    doc = f"""<html><head><meta charset="utf-8"><style>
body{{margin:0;background:#0c0c0c;}}
.barra{{background:#2d2d2d;color:#ddd;font:13px Segoe UI,Arial;padding:6px 12px;}}
pre{{margin:0;padding:12px 14px;color:#cccccc;font:14px/1.35 Consolas,'Courier New',monospace;white-space:pre-wrap;word-break:break-word;width:{ancho-28}px}}
.it{{color:#f9f1a5;font-weight:bold}} .tool{{color:#3a96dd}} .err{{color:#f14c4c}} .ok{{color:#16c60c}}
</style></head><body><div class="barra">{html.escape(titulo)}</div><pre>{chr(10).join(lineas)}</pre></body></html>"""
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": ancho, "height": 400})
        pg.set_content(doc)
        h = pg.evaluate("document.documentElement.scrollHeight")
        top = pg.evaluate("document.querySelector('pre').getBoundingClientRect().top") + 12
        lh = 14 * 1.35
        n1 = int((chunk - top) // lh)
        paso = int(chunk // lh)
        cortes = [0, top + n1 * lh]
        while cortes[-1] < h - 2:
            cortes.append(cortes[-1] + paso * lh)
        cortes[-1] = h
        n = len(cortes) - 1
        rutas = []
        for i in range(n):
            ruta = f"{png}_{i+1}.png" if n > 1 else f"{png}.png"
            pg.screenshot(path=ruta, full_page=True, clip={"x": 0, "y": cortes[i], "width": ancho, "height": cortes[i+1] - cortes[i]})
            rutas.append(Path(ruta).name)
        b.close()
        return rutas

TRABAJOS = [
    ("01_05_entorno", "c01_entorno", "Pasos 1 a 5 - equipo, Ollama y modelos"),
    ("06_conversacion_local", "c02_paso06", "Paso 6 - conversacion local"),
    ("10_revision_codigo", "c03_paso10", "Paso 10 - revision de calculadora.py"),
    ("11_validacion_casos_limite", "c04_paso11", "Paso 11 - validacion manual"),
    ("12_generar_pruebas", "c05_paso12", "Paso 12 - pruebas generadas por el modelo"),
    ("13_pruebas_antes", "c06_paso13", "Paso 13 - pruebas antes de la correccion"),
    ("14_correccion_minima", "c07_paso14", "Paso 14 - correccion minima"),
    ("15_pruebas_despues", "c08_paso15", "Paso 15 - pruebas despues de la correccion"),
    ("16_prueba_script_con_red", "c09_paso16_prueba", "Paso 16 - prueba del script CON red (no es la prueba offline)"),
    ("16_offline", "c10_paso16_offline", "Pasos 16 y 17 - ejecucion SIN Internet"),
    ("19_consultar_modelo_basico", "c11_paso19", "Paso 19 - consultar_modelo_basico.py"),
    ("20_consultar_modelo_archivo", "c12_paso20", "Paso 20 - consultar_modelo.py con calculadora.py"),
    ("21_privacidad_demo", "c13_paso21", "Paso 21 - privacidad consciente"),
    ("22_medicion_tiempos", "c14_paso22", "Paso 22 - tiempos"),
    ("23_reto_mediana_propuesta", "c15_paso23a", "Paso 23 - propuesta del modelo"),
    ("23b_mediana_pruebas_primer_intento", "c16_paso23b", "Paso 23 - primer intento de pruebas"),
    ("23c_explicar_fallo_mediana", "c17_paso23c", "Paso 23 - explicacion del fallo"),
    ("23d_mediana_pruebas_final", "c18_paso23d", "Paso 23 - pruebas finales"),
]

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    filtro = sys.argv[1:]
    for f, out, t in TRABAJOS:
        if filtro and out not in filtro: continue
        if not (EV / f"{f}.txt").exists(): continue
        for old in OUT.glob(f"{out}*.png"): old.unlink()
        print(out, render(EV / f"{f}.txt", str(OUT / out), t))
