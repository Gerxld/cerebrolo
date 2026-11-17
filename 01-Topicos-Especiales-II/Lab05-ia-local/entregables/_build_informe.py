# -*- coding: utf-8 -*-
r"""Regenera todo: capturas de terminal -> informe.html -> PDF (con indice paginado) -> ZIP.
Uso (desde cualquier carpeta):  py -3.14 C:\Cerebrolo\01-Topicos-Especiales-II\Lab05-ia-local\entregables\_build_informe.py
"""
import re, subprocess, sys, zipfile, shutil
from pathlib import Path
import pymupdf

E = Path(__file__).parent
NOMBRE = "Lab05_TopicosII_Rios_Gerald"
PDF = E / f"{NOMBRE}.pdf"
SHOTS = E / "screenshots"

# 1. capturas
subprocess.run(["py", "-3.14", str(E / "_captura_terminal.py")], check=True, cwd=E, env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})

head = (E / "informe" / "_head.html").read_text(encoding="utf-8")
cuerpo_src = (E / "informe" / "cuerpo.html").read_text(encoding="utf-8")

contador = [0]
def fig(m):
    key, cap = m.group(1), m.group(2)
    rutas = sorted(SHOTS.glob(f"{key}.png")) + sorted(SHOTS.glob(f"{key}_*.png"))
    out = []
    for i, r in enumerate(rutas):
        contador[0] += 1
        c = cap if i == 0 else cap.split(" (evidencia")[0] + " (continuación)."
        out.append(f'<figure>\n  <img src="../screenshots/{r.name}" alt="{key}">\n  <figcaption>Figura {contador[0]}. {c}</figcaption>\n</figure>')
    return "\n".join(out)

BS = chr(92)

def offline():
    rutas = sorted(SHOTS.glob("c10_paso16_offline*.png"))
    if not rutas:
        return (f'<p>[PENDIENTE: ejecución offline de Gerald — evidencia{BS}16_offline.txt]</p>\n'
                f'<div class="hueco">[PENDIENTE: captura de la ejecución sin Internet (evidencia{BS}16_offline.txt)]</div>')
    cap = "Pasos 16 y 17: consulta al modelo con el Wi-Fi apagado (evidencia/16_offline.txt)."
    return ('<p>Corrimos el script el 30/10/2026 a las 12:59 con el Wi-Fi apagado. La salida deja constancia de tres cosas: '
            '<code>Test-NetConnection</code> a 8.8.8.8 devolvió <code>TcpTestSucceeded: False</code>, <code>Resolve-DnsName ollama.com</code> '
            'falló con «No hay servidores DNS configurados para el sistema local» y <code>Get-NetAdapter</code> mostró el Wi-Fi como '
            '<code>Disconnected</code>. En esas condiciones <code>ollama list</code> siguió mostrando los modelos descargados y '
            '<code>qwen2.5-coder:3b</code> respondió en 8.1 s que <code>mediana</code> calcula la mediana de la lista y que, si la lista '
            'está vacía, lanza una excepción. La respuesta es correcta y coincide con el código. El tiempo fue casi el mismo que en la '
            'prueba con red (9.1 s), lo que tiene sentido: la red no interviene en la inferencia.</p>\n'
            '<p>Para el paso 17 usamos el mismo modelo local, sin variantes con «cloud» en el nombre, y no abrimos ningún servicio web '
            'mientras duró la prueba. Toda la inferencia ocurrió en el equipo.</p>\n'
            + fig(re.match(r"(.*)\|(.*)", "c10_paso16_offline|" + cap)))

def expandir():
    contador[0] = 0
    t = cuerpo_src
    # las figuras se numeran en orden de aparición; {{OFFLINE}} se expande en su sitio
    def sub(m):
        if m.group(0) == "{{OFFLINE}}":
            return offline()
        return fig(m)
    return re.sub(r"\{\{FIG:([^|]+)\|(.*?)\}\}|\{\{OFFLINE\}\}", sub, t)

cuerpo = expandir()
(E / "informe" / "cuerpo_expandido.html").write_text(cuerpo, encoding="utf-8")

portada = """<body>

<div class="portada">
  <div class="logos">
    <img src="../assets/utp.png" alt="Logo UTP">
    <img src="../assets/fisc.png" alt="Logo FISC">
  </div>
  <div class="titulo-bloque">
    <p>Universidad Tecnológica de Panamá</p>
    <p>Facultad de Ingeniería de Sistemas Computacionales</p>
    <p>Lic. en Desarrollo y Gestión de Software</p>
    <p style="margin-top:1em;">Tópicos Especiales II</p>
    <p>Laboratorio 5 — IA local y privada con Ollama</p>
    <p>1GS241</p>
  </div>
  <div class="presentado">
    <p>Presentado por:</p>
    <p class="nombres">Ríos, Gerald (8-987-741)</p>
  </div>
  <div class="revisado">
    <p>Revisado por:</p>
    <p class="nombres">Profesor Regis Rivera</p>
  </div>
  <div class="fecha">
    <p>Fecha de entrega</p>
    <p class="nombres">30 / 10 / 2026</p>
  </div>
</div>
"""
heads = [(m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).replace("&lt;", "<").replace("&gt;", ">"))
         for m in re.finditer(r'<(h[12]) class="sec">(.*?)</\1>', cuerpo)]

def indice(pags):
    out = ['<div class="indice">\n  <h1>Índice</h1>\n  <ol>']
    for (tag, t), p in zip(heads, pags):
        cls = ' class="n2"' if tag == "h2" else ""
        out.append(f'    <li{cls}><span class="t">{t}</span><span class="dots"></span><span class="p">{p}</span></li>')
    out.append("  </ol>\n</div>\n")
    return "\n".join(out)

def build(pags):
    html = head + portada + "\n" + indice(pags) + "\n" + cuerpo.replace(' class="sec"', "") + "\n</body>\n</html>\n"
    (E / "informe" / "informe.html").write_text(html, encoding="utf-8")
    subprocess.run(["py", "-3.14", r"C:\Cerebrolo\.claude\skills\informe-utp\scripts\informe_a_pdf.py",
                    str(E / "informe" / "informe.html"), str(PDF)], check=True)

def paginas():
    doc = pymupdf.open(PDF)
    pags = []
    for tag, t in heads:
        n = None
        for i in range(2, len(doc)):
            lineas = [l.strip() for l in doc[i].get_text().splitlines()]
            if t in lineas:
                n = i + 1
                break
        pags.append(n if n else "?")
    n = len(doc); doc.close()
    return pags, n

pags = ["0"] * len(heads)
for _ in range(4):
    build(pags)
    nuevas, total = paginas()
    print(nuevas, total)
    if nuevas == pags:
        break
    pags = nuevas

# 3. ZIP (sin __pycache__)
carpeta = E / "laboratorio_local_privado"
for pc in carpeta.rglob("__pycache__"):
    shutil.rmtree(pc, ignore_errors=True)
zpath = E / f"{NOMBRE}.zip"
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(carpeta.rglob("*")):
        if f.is_file() and "__pycache__" not in f.parts and f.suffix != ".pyc":
            z.write(f, Path("laboratorio_local_privado") / f.relative_to(carpeta))
print("ZIP:", zpath, len(zipfile.ZipFile(zpath).namelist()), "archivos")
