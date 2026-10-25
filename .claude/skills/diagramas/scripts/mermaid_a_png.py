# -*- coding: utf-8 -*-
"""
Renderiza uno o varios archivos Mermaid (.mmd) a PNG usando Playwright
(instalado bajo `py -3.14`) y Mermaid desde CDN. No necesita mermaid-cli.

    py -3.14 mermaid_a_png.py <archivo.mmd | carpeta> [escala]

  Genera <archivo>.png al lado de cada .mmd. Escala por defecto: 2 (nítido al imprimir).
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

HTML = """<!doctype html><html><head><meta charset="utf-8">
<style>body{margin:0;background:#fff;font-family:'Times New Roman',serif}#d{display:inline-block;padding:16px}</style>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script></head>
<body><div id="d"><pre class="mermaid">%s</pre></div>
<script>
mermaid.initialize({startOnLoad:false, theme:'neutral',
  themeVariables:{fontFamily:"'Times New Roman', serif", fontSize:'16px'}});
mermaid.run().then(()=>{document.body.dataset.ok='1'}).catch(e=>{document.body.dataset.err=String(e)});
</script></body></html>"""


def render(pagina, mmd: Path, escala: float) -> None:
    codigo = mmd.read_text(encoding="utf-8").replace("&", "&amp;").replace("<", "&lt;")
    pagina.set_content(HTML % codigo)
    pagina.wait_for_function("document.body.dataset.ok || document.body.dataset.err", timeout=30000)
    err = pagina.evaluate("document.body.dataset.err")
    if err:
        raise RuntimeError(f"{mmd.name}: {err}")
    png = mmd.with_suffix(".png")
    pagina.locator("#d").screenshot(path=str(png))
    print(f"OK  {png}")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    objetivo = Path(sys.argv[1])
    escala = float(sys.argv[2]) if len(sys.argv) > 2 else 2
    archivos = sorted(objetivo.glob("*.mmd")) if objetivo.is_dir() else [objetivo]
    fallos = 0
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pagina = nav.new_page(device_scale_factor=escala, viewport={"width": 1400, "height": 1000})
        for mmd in archivos:
            try:
                render(pagina, mmd, escala)
            except Exception as e:  # sigue con los demás y reporta
                fallos += 1
                print(f"ERROR  {e}")
        nav.close()
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
