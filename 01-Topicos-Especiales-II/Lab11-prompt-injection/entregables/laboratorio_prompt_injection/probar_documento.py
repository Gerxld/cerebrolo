"""Ayudante de laboratorio: pasa un documento cualquiera por la versión
vulnerable o por la endurecida.

Uso:
    python probar_documento.py vulnerable documentos/archivo.txt
    python probar_documento.py seguro documentos/archivo.txt
    python probar_documento.py confirmar documentos/archivo.txt   (paso 21, lee s/n por stdin)
"""
import sys
from pathlib import Path

modo, ruta = sys.argv[1], sys.argv[2]
texto = Path(ruta).read_text(encoding='utf-8')
print(f'\n--- {Path(ruta).name} ({modo}) ---')

if modo == 'vulnerable':
    from vulnerable import resumir_vulnerable
    print(resumir_vulnerable(texto))
else:
    from analizador_seguro import (analizar, validar_salida, aplicar_reglas,
                                   confirmar_accion)
    salida = analizar(texto)
    print('Salida del modelo:', salida)
    try:
        datos = validar_salida(salida)
        estado = aplicar_reglas(datos)
        print('Validación:', estado)
        if modo == 'confirmar':
            autorizado = confirmar_accion(estado)
            print('Acción autorizada por el humano:' if estado == 'REQUIERE_CONFIRMACION_HUMANA'
                  else 'Acción sin confirmación requerida:', autorizado)
            print('RESULTADO FINAL:', 'EJECUTADA (simulada)' if autorizado else 'CANCELADA')
    except Exception as e:
        print('BLOQUEADO:', e)
