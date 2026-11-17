import sys, html, pathlib, re
from playwright.sync_api import sync_playwright
def render(src_lines, titulo, out, prompt_cmd):
    body=[]
    body.append(f'<span class="p">PS C:\laboratorio_chat_web&gt;</span> {html.escape(prompt_cmd)}')
    for l in src_lines:
        e=html.escape(l)
        e=re.sub(r'\.\.\. ok$', '... <span class="ok">ok</span>', e)
        e=re.sub(r'^OK$', '<span class="ok">OK</span>', e)
        e=re.sub(r'(EOFError.*|Traceback.*)', r'<span class="err">\1</span>', e)
        if l.startswith('+') and not l.startswith('+++'): e=f'<span class="ok">{e}</span>'
        elif l.startswith('-') and not l.startswith('---'): e=f'<span class="err">{e}</span>'
        body.append(e)
    page=f'''<html><meta charset="utf-8"><style>
body{{margin:0;background:#012456;}} .w{{width:1100px;background:#012456;color:#eee;font:15px/1.35 Consolas,monospace;padding:14px 18px;white-space:pre-wrap;}}
.t{{background:#1f1f1f;color:#ccc;padding:6px 18px;font:13px Segoe UI,sans-serif;width:1100px}}
.p{{color:#ffd}} .ok{{color:#5fd75f}} .err{{color:#ff6b6b}}</style>
<div class="t">{html.escape(titulo)}</div><div class="w">{chr(10).join(body)}</div></html>'''
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1136,'height':200}); pg.set_content(page)
        pg.locator('body').screenshot(path=out); b.close()
E_=None
def rd(p): return pathlib.Path(p).read_text(encoding='utf-8').splitlines()
def rd8(p):
    return pathlib.Path(p).read_text(encoding='utf-8', errors='replace').splitlines()
render(rd('../unittest_v4.txt'),'Windows PowerShell','term_unittest_antes.png','python -m unittest -v   # estado tras el refactor (5 pruebas)')
render(rd('../unittest_final.txt'),'Windows PowerShell','term_unittest_final.png','python -m unittest -v   # estado final (7 pruebas)')
l=rd('../prueba_final_app.txt'); render(l,'Windows PowerShell','term_app_final.png','python app.py   # entradas: 2 tareas, una prioridad inválida (urgente), completar la 2')
render(rd('../prueba_eof_antes.txt')[-8:],'Windows PowerShell','term_eof_antes.png','python app_v2.py   # Ctrl+Z en la prioridad, antes de la corrección')
render(rd('../prueba_eof_despues.txt')[-4:],'Windows PowerShell','term_eof_despues.png','python app.py   # mismo caso, después de la corrección')
d=rd('../diff_multiarchivo.txt'); render(d[:46],'Windows PowerShell','term_diff.png','git diff --no-index _snapshot_antes ../laboratorio_chat_web   # primeras líneas (app.py)')
