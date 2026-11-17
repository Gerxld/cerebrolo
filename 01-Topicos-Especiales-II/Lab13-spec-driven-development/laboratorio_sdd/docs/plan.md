# Plan técnico v1.0
- Archivo: prestamos.py; funciones registrar_prestamo y
  devolver_prestamo. tests/test_prestamos.py para aceptación.
- date.fromisoformat + comprobación de formato estricto.
- timedelta(days=14) para vencimiento.
- Validar todo ANTES de append() o de mutar un dict.
- No dependencias externas, red, BD ni fecha del sistema.
- La lista de préstamos la proporciona quien llama.

## Orden de implementación

1. Crear prestamos.py con las firmas vacías (NotImplementedError).
2. Escribir tests/test_prestamos.py y comprobar la línea base roja.
3. T01 (R01–R04): normalizar textos, validar fecha, calcular vencimiento, agregar.
4. T02 (R05–R06): rechazar el cuarto préstamo activo y el libro ya prestado.
5. T03 (R07–R08): devolver o fallar.
6. T04–T05: correr aceptación completa, registrar evidencia y revisar el diff.

## Evaluación crítica del plan que propuso la IA (paso 11)

La respuesta completa está en entregables/prompts/11_plan_tecnico.md. Tomamos
de ella solo lo que cambia la conducta del código y dejamos fuera el resto.

Aceptado:
- No confiar solo en date.fromisoformat. Desde Python 3.11 acepta "20260901",
  que la spec rechaza (D3). Por eso el plan dice "comprobación de formato
  estricto" y la validación revisa primero la forma (10 caracteres, guiones en
  las posiciones 4 y 7, solo dígitos ASCII) y después construye la fecha.
- No usar isdigit() ni \d sin ASCII, porque aceptan dígitos Unicode.
- Convertir OverflowError en ValueError al sumar los 14 días (D4).
- Comprobar isinstance(str) antes de strip(), para que None o un entero
  produzcan ValueError y no TypeError (D4).
- Un solo append() al final, después de todas las validaciones, y asignar
  devuelto = True literal.

Rechazado:
- Poner el archivo de pruebas en la raíz (test_prestamos.py). La estructura
  del paso 2 lo fija en tests/ y el comando del paso 18 usa -s tests.
- Las diez clases de prueba con decenas de casos (Unicode, 9999-12-31,
  comparación por mayúsculas...). El enunciado trae las ocho pruebas de
  aceptación y la regla es no alterar las pruebas fuera de test_r05 en la
  Fase D. Esos casos quedan anotados como riesgo cubierto solo por revisión
  manual (ver traceability.md), no como pruebas nuevas.
- Constantes y seis ayudantes privados como estructura obligatoria. La propia
  IA dijo que era "solo una sugerencia"; además _libro_esta_activo y
  _contar_activos son trabajo de T02 y no deben aparecer en T01.
- Reordenar el trabajo escribiendo pruebas por bloques. El orden del
  laboratorio es: todas las pruebas primero (línea base roja) y luego T01, T02
  y T03.
