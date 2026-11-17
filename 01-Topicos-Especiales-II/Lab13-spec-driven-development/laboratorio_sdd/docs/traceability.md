# Trazabilidad (comprobar que nada se implemente por accidente)

Rutas de evidencia relativas a la carpeta entregables/ del laboratorio:
evidencia/ (salidas de terminal), diffs/ (cambios de la IA), prompts/
(interacciones completas) y snapshots/ (copias por etapa).

## 1. Matriz R → AC → tarea → prueba → evidencia

| Req. | AC | Tarea | Prueba | Evidencia |
|---|---|---|---|---|
| R01 | AC01 | T01 | test_r01_registro | rojo: 01_linea_base_roja; verde: 04_v1.0_verde y 07_v1.1_verde; diffs/T01.diff |
| R02 | AC02 | T01 | test_r02_vencimiento | igual que R01 |
| R03 | AC03 | T01 | test_r03_fecha_invalida | igual que R01; casos extra en 05_revision_manual_v1.0 (caso 1 y D3) |
| R04 | AC04 | T01 | test_r04_campos_vacios | igual que R01; casos extra D4 en 05_revision_manual_v1.0 |
| R05 (v1.0, límite 3) | AC05 (v1.0) | T02 | test_r05_maximo_activos (versión de 3) | 03_despues_T02 (error por falta de T03); 04_v1.0_verde; diffs/T02.diff; revisión manual caso 3 |
| R05 (v1.1, límite 2) | AC05 (v1.1) | T06 | test_r05_maximo_activos (versión de 2) | 06_r05_v11_rojo; 07_v1.1_verde; diffs/R05.diff; diffs/test_r05_v1.1.diff; 08_revision_manual_v1.1 |
| R06 | AC06 | T02 | test_r06_libro_unico | 03_despues_T02; 04_v1.0_verde; 07_v1.1_verde; revisión manual caso 2 |
| R07 | AC07 | T03 | test_r07_devolver | 04_v1.0_verde; 07_v1.1_verde; diffs/T03.diff |
| R08 | AC08 | T03 | test_r08_devolucion_inexistente | 04_v1.0_verde; 07_v1.1_verde; D11 en la revisión manual |
| Cierre (todo error es ValueError y la lista queda intacta) | AC03–AC06, AC08 | T01–T03 | los assertEqual sobre self.p en test_r03, r04, r05, r06 y r08 | revisión manual: la salida muestra la lista antes y después en cada caso |

T04 (ejecutar aceptación y revisar errores) se cumple con las corridas 04 y 07
y la revisión manual. T05 (documentar evidencia y revisar diff) se cumple con
este archivo y las secciones 3 y 4.

## 2. Corridas de pruebas (comando: python -m unittest discover -s tests -v)

| Momento | Archivo | Resultado |
|---|---|---|
| Línea base roja (solo firmas) | evidencia/01_linea_base_roja.txt | FAILED (errors=9): NotImplementedError; son 8 pruebas y test_r03 cuenta 2 errores por sus dos subpruebas |
| Después de T01 | evidencia/02_despues_T01.txt | FAILED (failures=2, errors=2): pasan r01 a r04; fallan r05 y r06 (asserts), r07 y r08 (NotImplementedError) |
| Después de T02 | evidencia/03_despues_T02.txt | FAILED (errors=4): r05 a r08 con NotImplementedError; r05 y r06 llegan a llamar devolver_prestamo, que es de T03 |
| v1.0 en verde (después de T03) | evidencia/04_v1.0_verde.txt | OK: 8 pruebas |
| v1.1: r05 actualizada, código sin cambiar | evidencia/06_r05_v11_rojo.txt | FAILED (failures=1): test_r05, "ValueError not raised" |
| v1.1 en verde | evidencia/07_v1.1_verde.txt | OK: 8 pruebas |

## 3. Revisión manual de casos negativos (paso 23)

Script: evidencia/revision_manual.py. Salidas: 05_revision_manual_v1.0.txt
(límite 3) y 08_revision_manual_v1.1.txt (límite 2). En cada caso el script
imprime la lista antes, el error y la lista después, y compara con una copia
profunda.

| Caso | Entrada | Resultado | ¿Lista intacta? |
|---|---|---|---|
| Fecha inválida | Luis / Redes / 2026-02-30 | ValueError | sí |
| Libro ya prestado | Luis / Python (activo de Ana) | ValueError | sí |
| Préstamo activo número 4 (v1.0) o 3 (v1.1) de Ana | Ana / otro libro | ValueError | sí |

Además comprobamos a mano las decisiones de la spec que las ocho pruebas no
tocan (D2, D3, D4, D5, D6, D7, D9, D11 y el borde 9999-12-17): 18 de 18
verificaciones correctas en cada versión. Esas decisiones NO tienen prueba
automatizada; si alguien cambia el código y rompe una, ninguna prueba del
proyecto avisa. Lo dejamos registrado como riesgo conocido.

## 4. Cotejo del código con la especificación (paso 24)

| Req. | Dónde está en prestamos.py (v1.1) |
|---|---|
| R01 | registrar_prestamo, líneas 35–55: arma el dict y lo agrega con un solo append (línea 54) |
| R02 | línea 40: inicio + timedelta(days=14); desborde convertido a ValueError (líneas 41–42) |
| R03 | _fecha_valida, líneas 13–24: forma estricta y fecha real |
| R04 | _texto_limpio, líneas 4–10: tipo str, strip() y vacío |
| R05 | línea 45: _contar_activos(...) >= 2 (era >= 3 en v1.0) |
| R06 | línea 43: _libro_esta_activo(...) |
| R07 | devolver_prestamo, líneas 57–67: pone devuelto = True y devuelve el mismo dict |
| R08 | línea 68: ValueError cuando no hay préstamo activo del par usuario-libro |

Funciones no solicitadas: el módulo tiene dos funciones públicas
(registrar_prestamo y devolver_prestamo) y cuatro ayudantes con guion bajo.
No hay UI, base de datos, imports externos ni uso del reloj del sistema
(solo se importan date y timedelta). La IA no declaró nada como validado; la
validación fue nuestra, con las corridas de la sección 2.

## 5. R05 versión 1.1

| Elemento | Detalle |
|---|---|
| Requisito | R05 v1.1: máximo 2 préstamos activos por usuario; el tercero produce ValueError |
| Cambio de spec | spec.md versión 1.1 (29/10/2026, responsable Gerald Ríos); diffs/spec_v1.0_a_v1.1.diff |
| Prueba | test_r05_maximo_activos: libros iniciales ("A", "B"), intento fallido con "C", longitud esperada 2, devolver "A" y registrar "C" (diffs/test_r05_v1.1.diff) |
| Fallo esperado antes del código | evidencia/06_r05_v11_rojo.txt: ValueError not raised |
| Cambio aplicado por la IA | prestamos.py línea 45: umbral de 3 a 2, y el mensaje de error de "3" a "2" (diffs/R05.diff) |
| Resultado | evidencia/07_v1.1_verde.txt: 8 pruebas OK; R01–R04 y R06–R08 sin regresión (las mismas ocho pruebas, sin tocar, siguen en verde) y 18 de 18 en evidencia/08_revision_manual_v1.1.txt |
