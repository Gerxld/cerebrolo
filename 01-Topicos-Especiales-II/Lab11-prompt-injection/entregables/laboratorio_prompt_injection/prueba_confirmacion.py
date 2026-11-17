"""Paso 21 sin modelo: confirmar_accion() con el estado que exige aprobación humana.
La respuesta (s/n) llega por stdin."""
from analizador_seguro import confirmar_accion

autorizado = confirmar_accion('REQUIERE_CONFIRMACION_HUMANA')
print('Acción autorizada por el humano:', autorizado)
print('RESULTADO FINAL:', 'EJECUTADA (simulada)' if autorizado else 'CANCELADA')
