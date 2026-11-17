# -*- coding: utf-8 -*-
import re, subprocess, sys
from pathlib import Path
import pymupdf

E = Path(__file__).parent
L7 = Path(r"C:\Cerebrolo\01-Topicos-Especiales-II\Lab07-servidor-mcp\entregables\informe\informe.html").read_text(encoding="utf-8")
head = L7[:L7.index("<body>")]
head = re.sub(r"<title>.*?</title>", "<title>Laboratorio 8 — Agente de IA local con tool calling</title>", head)
cuerpo = (E / "informe" / "cuerpo.html").read_text(encoding="utf-8")

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
    <p>Laboratorio 8 — Agente de IA local con tool calling</p>
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
                    str(E / "informe" / "informe.html"), str(E / "Lab08_TopicosII_Rios_Gerald.pdf")], check=True)

def paginas():
    doc = pymupdf.open(E / "Lab08_TopicosII_Rios_Gerald.pdf")
    pags = []
    for tag, t in heads:
        n = None
        for i in range(2, len(doc)):
            lineas = [l.strip() for l in doc[i].get_text().splitlines()]
            if t in lineas:
                n = i + 1
                break
        pags.append(n if n else "?")
    return pags, len(doc)

pags = ["0"] * len(heads)
for _ in range(3):
    build(pags)
    nuevas, total = paginas()
    print(nuevas, total)
    if nuevas == pags:
        break
    pags = nuevas
