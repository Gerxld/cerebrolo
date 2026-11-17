"""Paso 24 sin modelo: el mismo JSON con borrar_cuenta contra la copia sin allowlist."""
import json
from analizador_sin_allowlist import validar_salida, aplicar_reglas

crudo = json.dumps({'categoria': 'acceso', 'prioridad': 'alta',
                    'resumen': 'Cliente sin acceso',
                    'accion_sugerida': 'borrar_cuenta'}, ensure_ascii=False)
print('JSON:', crudo)
try:
    print('Validación:', aplicar_reglas(validar_salida(crudo)))
except Exception as e:
    print('BLOQUEADO:', e)
