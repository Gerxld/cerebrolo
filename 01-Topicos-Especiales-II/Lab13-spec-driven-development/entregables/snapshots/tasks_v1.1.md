# Tareas

T01 [R01–R04]: registrar datos, validar, calcular fecha.
T02 [R05–R06]: rechazar exceso y libro prestado.
T03 [R07–R08]: registrar devolución o error.
T04 [R01–R08]: ejecutar aceptación y revisar errores.
T05 [R01–R08]: documentar evidencia y revisar diff.
Regla: ejecutar las tareas en orden, una por iteración.

## Criterios de salida (añadidos en el punto de control 2)

- T01 termina cuando test_r01 a test_r04 pasan. Las validaciones van antes del
  append(); T02 agregará sus dos comprobaciones en ese mismo lugar, sin
  reordenar lo de T01.
- T02 termina cuando test_r05 y test_r06 pasan y T01 sigue en verde.
- T03 termina cuando test_r07 y test_r08 pasan y T01 y T02 siguen en verde.
- T04 termina cuando los ocho tests pasan y se revisaron a mano los casos
  negativos (fecha inválida, libro ya prestado, cuarto préstamo) comprobando
  que la lista no cambia.
- T05 termina cuando traceability.md tiene la evidencia de cada requisito y el
  diff no muestra funciones públicas nuevas. Los ayudantes internos, si los
  hay, llevan guion bajo inicial y no son parte de la API.

## Punto de control 2 (plan y tareas)

[x] Ninguna tarea introduce funciones fuera de alcance (UI, login, multas,
    renovaciones, persistencia, consulta). La IA tampoco encontró ninguna.
[x] Cada requisito tiene al menos una tarea (T01–T03) y una prueba
    (test_r01 a test_r08).
[x] Huecos señalados por la IA (prompts/15_punto_control_2.md) y decisión:
    - Aceptados: regla transversal "error → ValueError y lista intacta" sin
      fila propia (se agrega a la matriz); D3–D11 sin prueba automatizada
      (se revisan a mano y se registra en traceability.md); referencia floja
      del punto de control 1 (corregida en spec.md); T04/T05 sin criterio de
      salida y T01/T02 sin lugar definido (se agregan arriba).
    - Rechazados: pruebas nuevas para D1–D11 y separar test_r08 en dos (el
      enunciado fija ocho pruebas; test_r08 ya prueba "inexistente" y "ya
      devuelto" en la misma prueba); "falta prueba de borde en R05" (test_r05
      ya acepta el tercero y comprueba que devolver libera cupo); pasos 1 y 2
      del plan como tareas (son preparación, no implementación).
    - Corregimos documentos antes de tocar código.

## Cambio de requisitos v1.1 (29/10/2026)

T06 [R05 v1.1]: bajar el límite de préstamos activos por usuario de 3 a 2.
  Orden: (1) spec v1.1 actualizada, (2) test_r05_maximo_activos actualizada y
  en rojo, (3) cambio limitado en prestamos.py, (4) las ocho pruebas en verde,
  (5) traceability.md con R05 v1.1.
  Alcance: solo la regla del límite dentro de registrar_prestamo. No cambian
  otras funciones, otras pruebas ni otros requisitos.
  Estado: spec v1.1 hecha; prueba actualizada y en rojo (evidencia/06_r05_v11_rojo.txt).
