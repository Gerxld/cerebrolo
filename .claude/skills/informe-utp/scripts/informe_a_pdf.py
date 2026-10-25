# -*- coding: utf-8 -*-
"""
Convierte un informe HTML de la asignatura a PDF con el formato institucional.

Requiere Playwright y PyMuPDF, que en este equipo estan instalados bajo `py -3.14`:

    py -3.14 tools/informe_a_pdf.py <ruta/informe.html> <ruta/salida.pdf>

Detalles del formato:
  - Tamano Carta, margenes 2.5 cm, fondos impresos.
  - Numero de pagina centrado en el pie mediante display_header_footer.
  - Chromium NO ejecuta JavaScript dentro de footer_template, asi que el numero
    de la portada no se puede ocultar desde ahi: se tapa despues con PyMuPDF
    dibujando un rectangulo blanco sobre esa zona de la pagina 1.
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright
import pymupdf

FOOTER = """
<div style="width:100%; font-family:'Times New Roman', Times, serif; font-size:10pt;
            color:#111; text-align:center; padding:0 0 6px 0;">
  <span class="pageNumber"></span>
</div>
"""
HEADER = '<div style="display:none"></div>'


def html_a_pdf(html_path: Path, pdf_path: Path) -> None:
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        navegador = p.chromium.launch()
        pagina = navegador.new_page()
        pagina.goto(html_path.resolve().as_uri())
        pagina.wait_for_load_state("networkidle")
        pagina.pdf(
            path=str(pdf_path),
            format="Letter",
            print_background=True,
            display_header_footer=True,
            header_template=HEADER,
            footer_template=FOOTER,
            margin={"top": "2.5cm", "bottom": "2.5cm", "left": "2.5cm", "right": "2.5cm"},
        )
        navegador.close()


def tapar_numero_portada(pdf_path: Path) -> None:
    doc = pymupdf.open(pdf_path)
    portada = doc[0]
    ancho, alto = portada.rect.width, portada.rect.height
    zona = pymupdf.Rect(ancho * 0.25, alto - 48, ancho * 0.75, alto - 6)
    portada.draw_rect(zona, color=None, fill=(1, 1, 1))
    doc.save(pdf_path, incremental=True, encryption=pymupdf.PDF_ENCRYPT_KEEP)
    doc.close()


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    html_path, pdf_path = Path(sys.argv[1]), Path(sys.argv[2])
    if not html_path.exists():
        print(f"No existe el HTML: {html_path}")
        return 1
    html_a_pdf(html_path, pdf_path)
    tapar_numero_portada(pdf_path)
    doc = pymupdf.open(pdf_path)
    print(f"OK  {pdf_path}  ({doc.page_count} paginas, {pdf_path.stat().st_size} bytes)")
    doc.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
