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

Versión 1.0 revisada: fecha 29/10/2026; aprobador(es) Gerald Ríos
