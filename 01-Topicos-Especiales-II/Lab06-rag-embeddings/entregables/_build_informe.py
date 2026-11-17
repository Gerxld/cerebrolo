# -*- coding: utf-8 -*-
"""Arma informe/informe.html desde _head.html + cuerpo.html, calcula el índice con la paginación real y genera el PDF."""
import re, html, subprocess, sys
from pathlib import Path
import pymupdf

R = Path(__file__).parent
SK = r"C:\Cerebrolo\.claude\skills\informe-utp\scripts\informe_a_pdf.py"
PDF = R / "Lab06_TopicosII_Rios_Gerald.pdf"

def cuerpo_html():
    c = (R / "informe/cuerpo.html").read_text(encoding="utf-8")
    n = [0]
    def fig(m):
        n[0] += 1
        f, cap = m.group(1).strip(), m.group(2).strip()
        base = R / "screenshots"
        partes = sorted(base.glob(f + "*.png")) if not (base / (f + ".png")).exists() else [base / (f + ".png")]
        imgs = "".join(f'<img src="../screenshots/{p.name}" alt="Figura {n[0]}">' for p in partes)
        return f'<figure>{imgs}<figcaption>Figura {n[0]}. {html.escape(cap)}</figcaption></figure>'
    c = re.sub(r"^@FIG (\S+) \| (.+)$", fig, c, flags=re.M)
    codigo = (R / "laboratorio_rag/rag_universidad.py").read_text(encoding="utf-8")
    c = c.replace("@CODIGO", html.escape(codigo))
    return c

def titulos(c):
    return [(int(m.group(1)), re.sub(r"<[^>]+>", "", m.group(2))) for m in re.finditer(r"<h([12])>(.*?)</h\1>", c)]

def armar(paginas):
    c = cuerpo_html()
    items = []
    for nivel, t in titulos(c):
        cls = ' class="n2"' if nivel == 2 else ""
        items.append(f'<li{cls}><span class="t">{html.escape(t)}</span><span class="dots"></span><span class="p">{paginas.get(t, "?")}</span></li>')
    indice = '<div class="indice">\n<h1>Índice</h1>\n<ol>\n' + "\n".join(items) + "\n</ol>\n</div>\n\n"
    head = (R / "informe/_head.html").read_text(encoding="utf-8")
    (R / "informe/informe.html").write_text(head + indice + c + "\n</body>\n</html>\n", encoding="utf-8")
    return titulos(c)

def pdf():
    subprocess.run(["py", "-3.14", SK, str(R / "informe/informe.html"), str(PDF)], check=True)

def paginas_reales(tit):
    doc = pymupdf.open(PDF)
    res = {}
    for nivel, t in tit:
        for i in range(2, len(doc)):  # saltar portada e índice
            lineas = [l.strip() for l in doc[i].get_text().splitlines()]
            if t in lineas:
                res[t] = i + 1
                break
    return res

if __name__ == "__main__":
    tit = armar({})
    pdf()
    pag = paginas_reales(tit)
    tit = armar(pag); pdf()
    pag2 = paginas_reales(tit)
    print("estable:", pag == pag2, "| sin pagina:", [t for _, t in tit if t not in pag2])
    for _, t in tit: print(pag2.get(t), t)
