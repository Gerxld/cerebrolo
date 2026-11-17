---
name: python-code-review
description: Revisa código Python existente para detectar errores funcionales, riesgos de seguridad y problemas de mantenibilidad. Úsala cuando el usuario solicite code review, auditoría o evaluación técnica de archivos Python; no usar para enseñar sintaxis básica o crear código nuevo desde cero.
---

# Python Code Review

Realiza una revisión técnica del código Python proporcionado o de los archivos
Python que el usuario indique.

## Flujo

1. Identifica los archivos que deben revisarse.
2. Lee `references/checklist.md`.
3. Ejecuta `python scripts/check_syntax.py <archivo>` para cada archivo revisado. Este paso es obligatorio y no modifica nada: el script solo comprueba la sintaxis y no escribe archivos en el proyecto.
4. Revisa el código usando el checklist.
5. No modifiques archivos a menos que el usuario lo solicite explícitamente.
6. Entrega el resultado usando `assets/report-template.md`.
7. Antes de finalizar, verifica que cada hallazgo incluya evidencia concreta.

## Reglas

- Prioriza errores funcionales y riesgos de seguridad.
- Distingue entre error, riesgo y sugerencia de estilo.
- No inventes líneas o comportamientos que no existan en el código.
- Si no encuentras un problema, no lo inventes para completar el informe.
- Propón una corrección breve para cada hallazgo.

## Verificación final

Antes de responder:
- confirma que se revisaron todos los archivos solicitados;
- confirma que los hallazgos tienen evidencia;
- confirma que no se modificó código sin permiso;
- confirma que el formato coincide con assets/report-template.md
