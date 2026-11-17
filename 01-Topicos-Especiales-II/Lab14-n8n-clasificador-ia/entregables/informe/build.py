# genera informe.html a partir de partes; los números del índice se rellenan desde pages.json
import json, os
pages = json.load(open('pages.json')) if os.path.exists('pages.json') else {}
def P(k): return str(pages.get(k, '0'))

figs = {}
def fig(n, src, cap, alt):
    return f'<figure><img src="../screenshots/{src}" alt="{alt}"><figcaption>Figura {n}. {cap}</figcaption></figure>\n'

idx = [
 ('intro','Introducción',1),
 ('s1','1. Entorno y elección del modelo',1),
 ('s11','1.1 Entorno y credencial',2),
 ('s12','1.2 Gemma 4 31B, descartado',2),
 ('s13','1.3 Comparación y modelo elegido',2),
 ('s2','2. Construcción del workflow',1),
 ('s21','2.1 Entrada y prompt (pasos 1 a 10)',2),
 ('s22','2.2 Primera ejecución sin parser (paso 11)',2),
 ('s23','2.3 Structured Output Parser (pasos 12 a 14)',2),
 ('s24','2.4 Switch y ramas (pasos 15 a 20)',2),
 ('s3','3. Ejecuciones con distintos tickets',1),
 ('s31','3.1 Resumen de las ejecuciones (pasos 21 a 24)',2),
 ('s32','3.2 Caso ambiguo (paso 23)',2),
 ('s33','3.3 Intento de inyección (paso 24)',2),
 ('s4','4. Inspección de una ejecución (paso 25)',1),
 ('s5','5. Cambio de reglas (pasos 26 y 27)',1),
 ('s51','5.1 Regla de negocio en el Switch',2),
 ('s52','5.2 Regla de interpretación en el prompt',2),
 ('s6','6. Retos',1),
 ('s61','6.1 Form Trigger (paso 28)',2),
 ('s62','6.2 Registro en Google Sheets (paso 29)',2),
 ('s7','7. Comparación con una automatización sin IA (paso 30)',1),
 ('s8','8. Qué decidió la IA y qué decidió n8n',1),
 ('s9','9. Preguntas de reflexión',1),
 ('concl','Conclusiones',1),
]
index_html = '<div class="indice">\n  <h1>Índice</h1>\n  <ol>\n'
for k,t,l in idx:
    cls = ' class="n2"' if l==2 else ''
    index_html += f'    <li{cls}><span class="t">{t}</span><span class="dots"></span><span class="p">{P(k)}</span></li>\n'
index_html += '  </ol>\n</div>\n'

body = open('cuerpo.html', encoding='utf8').read()
# sustituye marcadores {{FIG n|archivo|pie|alt}}
import re
def rep(m):
    n, src, cap, alt = m.group(1).split('|')
    return fig(n, src, cap, alt)
body = re.sub(r'^\{\{FIG (.*)\}\}$', rep, body, flags=re.M)
tpl = open('cabecera.html', encoding='utf8').read()
open('informe.html','w',encoding='utf8').write(tpl + index_html + body + '\n</body>\n</html>\n')
