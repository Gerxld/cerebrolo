import fitz, json, re, sys
doc = fitz.open('../Lab14_TopicosII_Rios_Gerald.pdf')
heads = {'intro':'Introducción','s1':'1. Entorno y elección del modelo','s11':'1.1 Entorno y credencial','s12':'1.2 Gemma 4 31B, descartado','s13':'1.3 Comparación y modelo elegido','s2':'2. Construcción del workflow','s21':'2.1 Entrada y prompt (pasos 1 a 10)','s22':'2.2 Primera ejecución sin parser (paso 11)','s23':'2.3 Structured Output Parser (pasos 12 a 14)','s24':'2.4 Switch y ramas (pasos 15 a 20)','s3':'3. Ejecuciones con distintos tickets','s31':'3.1 Resumen de las ejecuciones (pasos 21 a 24)','s32':'3.2 Caso ambiguo (paso 23)','s33':'3.3 Intento de inyección (paso 24)','s4':'4. Inspección de una ejecución (paso 25)','s5':'5. Cambio de reglas (pasos 26 y 27)','s51':'5.1 Regla de negocio en el Switch','s52':'5.2 Regla de interpretación en el prompt','s6':'6. Retos','s61':'6.1 Form Trigger (paso 28)','s62':'6.2 Registro en Google Sheets (paso 29)','s7':'7. Comparación con una automatización sin IA (paso 30)','s8':'8. Qué decidió la IA y qué decidió n8n','s9':'9. Preguntas de reflexión','concl':'Conclusiones'}
out={}
for k,h in heads.items():
    for i in range(2, len(doc)):
        lines=[l.strip() for l in doc[i].get_text().split('\n')]
        if h in lines:
            out[k]=i+1; break
    else: print('NO',k)
json.dump(out,open('pages.json','w'))
print(out)
