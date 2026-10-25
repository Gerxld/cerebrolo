# -*- coding: utf-8 -*-
"""
Rasteriza paginas de un PDF a PNG para revisarlas con Read (en este equipo Read
no renderiza PDF porque falta poppler).

    py -3.14 verificar_pdf.py <archivo.pdf> [carpeta_salida] [paginas]

  paginas: "1,2,5" o "1-3". Por defecto: todas.
  carpeta_salida: por defecto <carpeta del pdf>/_preview

Tambien imprime el numero de paginas y la primera linea de texto de cada una,
util para cotejar el indice contra la paginacion real.
"""
import sys
from pathlib import Path

import pymupdf


def parse_paginas(spec: str, total: int) -> list[int]:
    if not spec:
        return list(range(1, total + 1))
    out = []
    for parte in spec.split(","):
        if "-" in parte:
            a, b = parte.split("-")
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(parte))
    return [p for p in out if 1 <= p <= total]


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    pdf = Path(sys.argv[1])
    salida = Path(sys.argv[2]) if len(sys.argv) > 2 else pdf.parent / "_preview"
    salida.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf)
    paginas = parse_paginas(sys.argv[3] if len(sys.argv) > 3 else "", doc.page_count)
    print(f"{pdf.name}: {doc.page_count} paginas")
    for n in paginas:
        pag = doc[n - 1]
        png = salida / f"pag_{n:02d}.png"
        pag.get_pixmap(dpi=90).save(png)
        texto = next((l.strip() for l in pag.get_text().splitlines() if l.strip()), "")
        print(f"  {n:>3}  {png.name}  | {texto[:70]}")
    doc.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
