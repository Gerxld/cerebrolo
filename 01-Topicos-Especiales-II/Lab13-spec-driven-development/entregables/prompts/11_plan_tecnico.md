# Paso 11. Plan técnico propuesto por la IA (sin implementación)

Fecha y hora: 29/10/2026 10:55
Comando (desde laboratorio_sdd, prompt por entrada estándar): `claude -p --model sonnet`

## Prompt

```text
Diseña un plan técnico para esta spec aprobada. Usa solo
Python estándar, funciones puras salvo modificación explícita
de la lista, datetime.date para fechas y unittest para pruebas.
Define interfaces, estructura y riesgos. NO escribas el código.

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

[contenido de docs/constitution.md]
# Constitución del proyecto

- Python estándar; sin paquetes externos ni base de datos.
- Sin interfaz gráfica; la entrega es un módulo reutilizable.
- Entradas inválidas producen ValueError sin alterar la lista.
- Fechas deterministas: nunca usar la fecha actual del sistema.
- No implementar nada sin criterio de aceptación verificable.
- Toda modificación exige actualizar la spec y las pruebas.
```

## Respuesta de la IA

# Plan técnico: préstamos de libros (spec 1.0 revisada)

## 1. Estructura de archivos

```
laboratorio_sdd/
├── docs/               spec.md, constitution.md, plan.md (este plan)
├── prestamos.py        módulo reutilizable, sin UI ni I/O
└── test_prestamos.py   unittest
```

- `prestamos.py` solo importa `datetime` (`date`, `timedelta`) y `re` si hace falta. No usa `date.today()` ni `datetime.now()`, por la constitución.
- Se ejecuta con `python -m unittest -v`.

## 2. Interfaces

**Constantes públicas**
- `PLAZO_DIAS = 14` (R02)
- `MAX_ACTIVOS_POR_USUARIO = 3` (R05)

**Funciones públicas.** Son las dos únicas que modifican algo, y solo lo que la spec permite.

| Función | Efecto | Retorno |
|---|---|---|
| `registrar_prestamo(prestamos, usuario, libro, fecha)` | Añade un dict al final de `prestamos` | Ese mismo dict (D7) |
| `devolver_prestamo(prestamos, usuario, libro)` | Pone `devuelto=True` en un dict existente | Ese mismo dict (D7) |

**Ayudantes privados.** Son puros: no tocan la lista ni los dicts.

| Función | Responsabilidad | Reglas |
|---|---|---|
| `_normalizar_texto(valor) -> str` | Exige `str`, hace `strip()` y rechaza el vacío. | R04, D2, D4 |
| `_parsear_fecha(texto) -> date` | Valida el formato estricto y la fecha real. No recorta nada. | R03, D3 |
| `_calcular_vencimiento(fecha: date) -> str` | Suma 14 días y devuelve `AAAA-MM-DD`. Convierte `OverflowError` en `ValueError`. | R02, D4 |
| `_buscar_activo(prestamos, usuario, libro) -> dict \| None` | Busca el préstamo activo con ese par exacto. | R08, D11 |
| `_libro_esta_activo(prestamos, libro) -> bool` | Busca un préstamo activo de ese libro, de cualquier usuario. | R06 |
| `_contar_activos(prestamos, usuario) -> int` | Cuenta los préstamos activos del usuario. | R05 |

Una función con un solo uso, como `_libro_esta_activo` o `_contar_activos`, puede quedar inline si resulta más legible. La separación de arriba es solo una sugerencia.

## 3. Algoritmos (en prosa)

**`registrar_prestamo`**
1. Normalizar `usuario` y luego `libro` con `_normalizar_texto`. Es el primer paso del orden fijado en D8 (R04).
2. `_parsear_fecha(fecha)` (R03).
3. Si `_libro_esta_activo(...)`, lanzar `ValueError` (R06).
4. Si `_contar_activos(...) >= 3`, lanzar `ValueError` (R05).
5. Calcular el vencimiento. El desborde también es `ValueError` y debe ocurrir antes de modificar nada.
6. Construir el dict con los cinco campos: `fecha_prestamo` tal como llegó (ya validada), el vencimiento y `devuelto=False`.
7. Hacer `append` y devolver el dict.

El `append` es la única mutación y va al final. Ningún fallo puede ocurrir después de él, así que no hace falta rollback.

**`devolver_prestamo`**
1. Normalizar `usuario` y `libro`, igual que en el registro (D5).
2. `_buscar_activo`. Si devuelve `None`, lanzar `ValueError`. Eso cubre R08, el préstamo ya devuelto y D11.
3. Asignar `devuelto = True` y devolver el dict.

## 4. Decisiones de implementación

- **Fecha:** no usar `date.fromisoformat`. Desde Python 3.11 acepta formatos como `20260901`, que D3 rechaza. Se hace en dos pasos:
  1. Comprobar `isinstance(str)`, longitud 10, guiones en las posiciones 4 y 7, y que los demás caracteres estén en `"0123456789"`. No usar `str.isdigit()` ni `\d` sin `re.ASCII`, porque aceptan dígitos Unicode como `２０２６`.
  2. Construir `date(a, m, d)` y capturar el `ValueError` para meses o días imposibles, bisiestos y el año `0000`.
- **Comparaciones:** igualdad exacta de `str` sobre el texto ya recortado. No usar `lower()` ni normalización Unicode (D6).
- **"Activo":** `not p["devuelto"]`.
- **Mensajes de error:** libres y descriptivos, porque no son parte del contrato. Una sola clase de excepción, `ValueError`.
- **Parámetro `prestamos`:** se asume lista bien formada (supuesto de la spec, sin validación).
- **Tipos:** `usuario` o `libro` que no sean `str`, o una fecha que no sea `str`, producen `ValueError`, nunca `TypeError` (D4).

## 5. Estrategia de pruebas (`unittest`)

**Convenciones**
- Cada test de error toma una copia con `copy.deepcopy` antes de llamar y comprueba `assertRaises(ValueError)` y que la lista sea igual después. Así se cubre "la lista queda intacta" y la inalterabilidad de los dicts previos.
- Un helper del test arma listas con N préstamos activos.
- Ninguna prueba depende del reloj del sistema.

| Clase de prueba | Casos clave | Cubre |
|---|---|---|
| `TestRegistrar` | Ana/Python/2026-09-01 produce los cinco campos exactos con `devuelto is False`. Se recortan los espacios. El retorno es el mismo objeto (`is`) que `lista[-1]`. | AC01, R01, D1, D2, D7 |
| `TestVencimiento` | 2026-09-01 → 2026-09-15. Cruces de mes y año: 2026-12-25 → 2027-01-08. Bisiesto: 2028-02-20 → 2028-03-05. Límite: 9999-12-17 → 9999-12-31 es válido; 9999-12-18 → `ValueError`. | AC02, R02, D4 |
| `TestFecha` | Inválidas: `2026-1-5`, `20260901`, ` 2026-09-01`, `2026-09-01 `, `01/09/2026`, `2026-02-30`, `2027-02-29`, `2026-13-01`, `2026-00-10`, `0000-01-01`, dígitos Unicode (`２０２６-09-01`), `""`, `None`, `20260901` como int. Válidas: `2028-02-29`, `0001-01-01`. | AC03, R03, D3 |
| `TestTextoVacio` | `""`, `"   "`, `"\t\n"`, `None`, `123`, para usuario y para libro por separado. | AC04, R04, D4 |
| `TestLimiteUsuario` | 3 libros distintos se aceptan; el 4.º falla. Tras devolver uno, el 4.º se acepta. Otro usuario no se ve afectado. Los devueltos no cuentan. | AC05, R05 |
| `TestLibroUnico` | Mismo libro, otro usuario: falla. Mismo libro y mismo usuario: falla. Tras devolverlo, se puede prestar al mismo u otro usuario. | AC06, R06, D9 |
| `TestComparacion` | `Ana`/`ana` son usuarios distintos. `Python`/`python` son libros distintos. `Clean Code` y `Clean  Code` (dos espacios) son distintos. Acentos distintos. | D6 |
| `TestDevolver` | Pone `devuelto is True` y retorna el mismo dict. Con espacios en los argumentos funciona (D5). | AC07, R07, D5, D7 |
| `TestDevolverErrores` | Inexistente, ya devuelto, libro activo de otro usuario, argumentos vacíos o no `str`. En todos hay `ValueError` y la lista no cambia. | AC08, R08, D11 |
| `TestOrdenYAtomicidad` | Entradas con varios fallos a la vez, para comprobar que el resultado es `ValueError` y la lista no cambia. | D8 |

**Limitación de D8:** como el mensaje no es parte del contrato, el orden de validación no se puede observar desde fuera. Solo se prueba el invariante (siempre `ValueError`, nunca cambios). Esto no impide implementarlo en el orden fijado.

## 6. Trazabilidad

| Requisito | Código | Prueba |
|---|---|---|
| R01, AC01 | `registrar_prestamo` | `TestRegistrar` |
| R02, AC02 | `_calcular_vencimiento` | `TestVencimiento` |
| R03, AC03 | `_parsear_fecha` | `TestFecha` |
| R04, AC04 | `_normalizar_texto` | `TestTextoVacio` |
| R05, AC05 | `_contar_activos` | `TestLimiteUsuario` |
| R06, AC06 | `_libro_esta_activo` | `TestLibroUnico` |
| R07, AC07 | `devolver_prestamo` | `TestDevolver` |
| R08, AC08 | `_buscar_activo` | `TestDevolverErrores` |

## 7. Riesgos

| # | Riesgo | Mitigación |
|---|---|---|
| 1 | `fromisoformat` es más permisivo en 3.11+ y daría falsos válidos. | Validación manual previa del formato (sección 4) y pruebas con `20260901`. |
| 2 | `isdigit()` y `\d` aceptan dígitos Unicode. | Lista explícita de caracteres ASCII y prueba con dígitos de ancho completo. |
| 3 | `date + timedelta` lanza `OverflowError`, no `ValueError`. | Capturarlo y reconvertirlo; probar el borde 9999-12-17/18. |
| 4 | Mutar la lista antes de terminar las validaciones. | Todas las comprobaciones primero, un único `append` al final; pruebas con `deepcopy`. |
| 5 | `TypeError` filtrado al llamar `.strip()` sobre un no `str`. | `isinstance` antes de cualquier operación; pruebas con `None`, int y bytes. |
| 6 | `devuelto` con un valor truthy distinto de `True`. | Asignar literalmente `True`; las pruebas usan `assertIs`. |
| 7 | Devolver una copia en lugar del dict de la lista (D7). | Pruebas con `assertIs`. |
| 8 | Cuenta de activos o libro único sobre registros devueltos. | Pruebas que mezclan activos y devueltos. |
| 9 | Aliasing del dict devuelto: quien llama puede mutarlo y corromper la lista. | Está aceptado por D7. Se deja una nota en el docstring. |
| 10 | `strip()` también recorta espacios Unicode, que quizá no se esperaban. | Es el comportamiento definido por D2. No se usa ningún `strip` personalizado. |
| 11 | Dependencia accidental del reloj. | Revisar que `prestamos.py` no use `today()` ni `now()`. |

## 8. Orden de trabajo sugerido

1. Crear `test_prestamos.py` con las pruebas de fecha, vencimiento y texto (ayudantes puros). Verificar que fallan.
2. Implementar `_normalizar_texto`, `_parsear_fecha` y `_calcular_vencimiento`.
3. Pruebas de `registrar_prestamo` (AC01, AC05, AC06, D6, D7, D9) y luego su implementación.
4. Pruebas de `devolver_prestamo` (AC07, AC08, D5, D11) y luego su implementación.
5. Revisión final: matriz de trazabilidad, riesgo 11 y la suite completa.

## 9. Fuera de este plan

Cualquier cambio de comportamiento exige actualizar primero la spec y las pruebas (constitución). Por eso las dudas que aparezcan al programar vuelven a `docs/spec.md` antes de tocar el código. Los cambios del cliente de la Fase D irían en la versión 1.1.

Si quieres, guardo este plan en `docs/plan.md`.
