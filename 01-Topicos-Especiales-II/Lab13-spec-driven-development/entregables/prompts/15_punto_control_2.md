# Paso 15. Segundo punto de control: huecos señalados por la IA

Fecha y hora: 29/10/2026 10:56
Comando (desde laboratorio_sdd, prompt por entrada estándar): `claude -p --model sonnet`

## Prompt

```text
Segundo punto de control. Revisa spec, plan, tareas y trazabilidad.
Señala huecos: tareas que introduzcan funciones fuera de alcance y requisitos
que no tengan al menos una tarea y una prueba. NO escribas código ni
corrijas los documentos; solo lista los huecos.

[contenido de docs/spec.md]
# Especificación: préstamos de libros (versión 1.0)
Objetivo: registrar y devolver préstamos sin base de datos.
Fuera de alcance: UI, login, multas, renovaciones, persistencia.

R01: registrar_prestamo(prestamos, usuario, libro, fecha)
     agrega un dict y lo devuelve. Los textos se recortan.
R02: fecha_vencimiento = fecha_prestamo + 14 días calendario.
R03: fecha debe ser válida y tener formato AAAA-MM-DD.
R04: usuario y libro no pueden quedar vacíos tras strip().
R05: cada usuario admite a lo sumo 3 préstamos activos.
R06: un libro admite a lo sumo un préstamo activo global.
R07: devolver_prestamo(prestamos, usuario, libro)
     marca devuelto=True y devuelve ese dict.
R08: devolver algo inexistente o ya devuelto produce ValueError.

Estructura: usuario, libro, fecha_prestamo,
fecha_vencimiento (str AAAA-MM-DD), devuelto (bool).
Todo error produce ValueError y no modifica la lista.

## Decisiones de negocio (paso 5, fijadas por el enunciado)

- Máximo 3 préstamos activos por usuario.
- Un libro no puede estar prestado a dos usuarios a la vez.
- Plazo de exactamente 14 días calendario.
- La fecha se recibe como AAAA-MM-DD.
- Devolver un préstamo inexistente o ya devuelto produce ValueError.
- No hay persistencia ni autenticación.

## Decisiones tomadas tras la auditoría QA (paso 7)

La IA devolvió 5 contradicciones, varias reglas ambiguas y 10 preguntas
(archivo entregables/prompts/07_auditoria_spec.md). Resolvimos así:

Aceptadas:
- D1 (C2): el dict nace con devuelto=False; "activo" significa devuelto == False.
- D2 (C3): usuario y libro se recortan con strip() antes de validar; la fecha NO
  se recorta, se valida tal como llega.
- D3 (R03): formato estricto. Exactamente 10 caracteres ASCII con forma
  [0-9]{4}-[0-9]{2}-[0-9]{2} y fecha real de calendario (bisiestos incluidos).
  "2026-1-5", "20260901", " 2026-09-01" y "01/09/2026" son inválidas;
  "2026-09-01" y "2028-02-29" son válidas.
- D4 (C1): si fecha_prestamo + 14 días supera 9999-12-31, se produce ValueError
  (no OverflowError). Un usuario, libro o fecha que no sea str también produce
  ValueError (no TypeError).
- D5 (C4): devolver_prestamo recorta usuario y libro igual que el registro.
- D6: la comparación de usuario y libro distingue mayúsculas, acentos y espacios
  internos (texto recortado, comparación exacta). "Ana" y "ana" son usuarios distintos.
- D7: registrar_prestamo y devolver_prestamo devuelven el mismo dict que está en
  la lista, no una copia.
- D8: orden de validación fijo en registrar_prestamo: tipo/vacío (R04), fecha
  (R03), libro activo (R06), límite del usuario (R05). Con cualquier fallo la
  lista y sus dicts quedan como antes de la llamada.
- D9: un libro ya devuelto puede volver a prestarse, al mismo u otro usuario.
- D10: un título equivale a un solo ejemplar; no se registra fecha de devolución;
  se admiten fechas pasadas o futuras porque no se compara con el reloj del sistema.
- D11: devolver un libro que tiene préstamo activo de otro usuario cuenta como
  inexistente (R08).

Rechazadas:
- Rango de años 1900–9998 (R03): inventa un límite que el cliente no pidió.
  Basta con lo que acepta datetime.date (año 0001–9999) más D4.
- Pasar la spec a 1.1 por estas aclaraciones: la 1.1 queda reservada para el
  cambio de requisitos del cliente (Fase D). Estas aclaraciones forman parte de
  la 1.0 revisada.
- Mensajes o códigos de error distinguibles por regla: las pruebas y los AC solo
  exigen ValueError. El texto del mensaje no es parte del contrato.
- Validar el parámetro prestamos (None, no lista, registros mal formados): la
  lista la proporciona quien llama (plan técnico). Queda como supuesto, no como
  requisito.
- Añadir una función de consulta o listado (C5): fuera de alcance; la lista se
  inspecciona directamente.

Respuestas a las preguntas de negocio del paso 4: solo libros físicos y un
ejemplar por título; sin tipos de usuario; sin multas ni renovaciones; sin
reservas; los datos de un préstamo son los cinco campos de la estructura.

## Criterios de aceptación

AC01 (R01): al registrar Ana / Python / 2026-09-01,
  queda un préstamo activo con los valores acordados.
AC02 (R02): el vencimiento es 2026-09-15.
AC03 (R03): fecha malformada o imposible → ValueError.
AC04 (R04): texto vacío o espacios → ValueError.
AC05 (R05): al intentar el cuarto préstamo activo → ValueError.
AC06 (R06): libro activo repetido, incluso otro usuario → ValueError.
AC07 (R07): devolver cambia devuelto a True.
AC08 (R08): devolver sin préstamo activo → ValueError.
En cada caso fallido, la lista queda intacta.

## Punto de control 1 (antes de programar)

[x] Alcance explícito: el objetivo y el "fuera de alcance" (UI, login, multas,
    renovaciones, persistencia) están escritos; D10 y el rechazo de la función
    de consulta cierran lo que quedaba abierto.
[x] R01–R08 sin contradicciones: las cinco contradicciones de la IA (C1–C5)
    quedaron resueltas con D1, D2, D4, D5 o descartadas con razón. Releímos
    R05 y R06 juntas y no chocan, porque D8 fija cuál se evalúa primero.
[x] AC01–AC08 verificables: cada AC se puede comprobar con una prueba unittest
    y un resultado esperado concreto (valor o ValueError). AC03 y AC04 llevan
    ejemplos en D3 y en las pruebas del paso 17.
[x] Fechas y límites definidos: formato en D3, plazo de 14 días en R02,
    desborde en D4, límite de 3 en R05, un libro por préstamo activo en R06.
[x] Comportamiento ante errores definido: todo error es ValueError y la lista
    queda intacta (cierre de la estructura, D4 y D8).

Control de aprobación

Versión 1.0 revisada: fecha 29/10/2026; aprobador(es) Gerald Ríos

[contenido de docs/plan.md]
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

[contenido de docs/tasks.md]
# Tareas

T01 [R01–R04]: registrar datos, validar, calcular fecha.
T02 [R05–R06]: rechazar exceso y libro prestado.
T03 [R07–R08]: registrar devolución o error.
T04 [R01–R08]: ejecutar aceptación y revisar errores.
T05 [R01–R08]: documentar evidencia y revisar diff.
Regla: ejecutar las tareas en orden, una por iteración.

[contenido de docs/traceability.md]
# Trazabilidad (comprobar que nada se implemente por accidente)

Nota: ejemplo de requisito conectado con prueba, tarea y evidencia.

| Requisito | Aceptación | Tarea | Evidencia esperada |
|---|---|---|---|
| R01–R04 | AC01–AC04 | T01 | test_r01 a test_r04 |
| R05–R06 | AC05–AC06 | T02 | test_r05 y test_r06 |
| R07–R08 | AC07–AC08 | T03 | test_r07 y test_r08 |
```

## Respuesta de la IA

# Punto de control 2: huecos detectados

Revisé solo el texto que pegaste. No abrí `prestamos.py` ni `tests/`, así que no sé qué prueban en realidad.

## A. Requisitos sin al menos una tarea y una prueba

A nivel de rango, R01–R08 tienen tarea y prueba (`test_r01` a `test_r08`). Los huecos están en lo que la spec decide y nadie cubre:

1. **Decisiones D1–D11 sin tarea ni prueba propia.** La trazabilidad solo llega a R01–R08.
   - **D3:** formato estricto. AC03 dice "malformada o imposible", pero nada exige rechazar `20260901`, `2026-1-5`, dígitos Unicode ni aceptar `2028-02-29`.
   - **D4:** desborde de `9999-12-31` y entradas que no son `str`, que deben dar `ValueError` y no `TypeError`.
   - **D5:** `devolver_prestamo` recorta usuario y libro. No está en T03.
   - **D6:** comparación exacta (`Ana` ≠ `ana`).
   - **D7:** se devuelve el mismo dict de la lista, no una copia. R07 lo dice, pero AC07 solo verifica `devuelto=True`.
   - **D8:** orden de validación R04 → R03 → R06 → R05.
   - **D9:** un libro devuelto puede volver a prestarse.
   - **D11:** devolver un libro activo de otro usuario cuenta como inexistente.
2. **R05 sin prueba de borde.** AC05 solo cubre el cuarto préstamo. Falta que el tercero sí se acepte y que un préstamo devuelto libere cupo (D1).
3. **R08 sin separar sus dos casos.** AC08 junta "inexistente" y "ya devuelto" en una sola prueba.
4. **Regla transversal sin ID.** "Todo error → `ValueError` y la lista queda intacta" no es un requisito numerado. No tiene tarea ni fila en la trazabilidad, y solo AC08 la menciona de forma general.
5. **Riesgo "solo revisión manual" sin registro.** El plan dice que esos casos quedan "anotados en `traceability.md`". Esa nota no existe en el archivo que pegaste.
6. **Referencia posiblemente rota.** El checkpoint 1 dice que AC03 y AC04 llevan ejemplos "en las pruebas del paso 17", pero el plan limita las pruebas a las ocho de aceptación. Hay que verificar que esos ejemplos existan.

## B. Problemas en tareas y plan

1. **Pasos del plan sin tarea.** Los pasos 1 y 2 (crear las firmas vacías y escribir las pruebas con la línea base roja) no tienen ID en `tasks.md`.
2. **T04 y T05 no coinciden con el plan.**
   - `tasks.md`: T04 es "ejecutar aceptación y revisar errores" y T05 es "documentar evidencia y revisar diff".
   - `plan.md`: T04–T05 es "correr aceptación completa, registrar evidencia y revisar el diff".
   - "Revisar errores" no tiene criterio de salida.
3. **T01 y T02 se pisan.** T01 dice "agregar", y D8 exige que R06 y R05 se evalúen antes del `append`. Entre T01 y T02 la función aceptaría cualquier préstamo, y T02 tendría que reordenar el código de T01. Falta decir dónde van las validaciones.
4. **Tareas sin definición de terminado.** Ninguna tarea cita las D que debe cumplir ni los AC que la cierran. T01 agrupa cuatro requisitos y no distingue qué prueba la deja en verde.
5. **AC01 vago.** "Los valores acordados" no dice cuáles son (usuario, libro, fecha, vencimiento y `devuelto=False`).

## C. Trazabilidad

1. El encabezado dice "ejemplo". La tabla parece una plantilla y no la matriz final.
2. No tiene filas para D1–D11, ni para T04/T05, ni para la regla de "lista intacta".
3. "Evidencia esperada" solo trae nombres de prueba. No hay resultados ni comandos.
4. Las filas agrupan rangos (R01–R04 → T01). No se puede ver qué requisito falla si falla una prueba.

## D. Funciones fuera de alcance

No encontré ninguna tarea que añada una función explícitamente fuera de alcance: UI, login, multas, renovaciones, persistencia o la función de consulta que se rechazó. Dos puntos a vigilar:

- Los ayudantes privados `_libro_esta_activo` y `_contar_activos` se mencionan en el plan como "trabajo de T02". T02 no los nombra. Debe quedar escrito que son internos y no parte de la API.
- "Revisar el diff" en T05 debería incluir comprobar que no aparecen funciones públicas nuevas. Hoy no lo dice.
