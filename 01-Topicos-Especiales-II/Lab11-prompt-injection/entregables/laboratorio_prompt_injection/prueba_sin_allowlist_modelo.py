"""Paso 24 con modelo: la copia sin allowlist procesa el ticket de borrar_cuenta."""
from pathlib import Path
import analizador_sin_allowlist as a

texto = Path('documentos/ticket_accion_borrar.txt').read_text(encoding='utf-8')
salida = a.analizar(texto)
print('Salida del modelo:', salida)
try:
    print('Validación:', a.aplicar_reglas(a.validar_salida(salida)))
except Exception as e:
    print('BLOQUEADO:', e)
