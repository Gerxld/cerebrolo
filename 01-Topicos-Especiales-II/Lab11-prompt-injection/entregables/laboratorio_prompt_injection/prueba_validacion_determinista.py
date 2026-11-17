"""Pasa a validar_salida() JSON fabricados a mano (sin modelo) para probar
que la capa determinista bloquea por sí sola, sin depender de lo que diga el LLM."""
import json
from analizador_seguro import validar_salida, aplicar_reglas

CASOS = {
    'accion fuera de la allowlist (borrar_cuenta)': {
        'categoria': 'acceso', 'prioridad': 'alta',
        'resumen': 'Cliente sin acceso', 'accion_sugerida': 'borrar_cuenta'},
    'prioridad inventada (critica)': {
        'categoria': 'acceso', 'prioridad': 'critica',
        'resumen': 'Cliente sin acceso', 'accion_sugerida': 'responder'},
    'accion ausente': {
        'categoria': 'acceso', 'prioridad': 'baja', 'resumen': 'x'},
    'salida valida (escalar)': {
        'categoria': 'acceso', 'prioridad': 'alta',
        'resumen': 'Cliente sin acceso', 'accion_sugerida': 'escalar'},
    'salida valida (responder)': {
        'categoria': 'horario', 'prioridad': 'baja',
        'resumen': 'Consulta de horario', 'accion_sugerida': 'responder'},
}

for nombre, obj in CASOS.items():
    crudo = json.dumps(obj, ensure_ascii=False)
    print(f'\n[{nombre}]\nJSON: {crudo}')
    try:
        print('Validación:', aplicar_reglas(validar_salida(crudo)))
    except Exception as e:
        print('BLOQUEADO:', e)
