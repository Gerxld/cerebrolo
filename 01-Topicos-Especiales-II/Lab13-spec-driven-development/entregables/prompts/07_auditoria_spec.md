# Paso 7. Auditoría de ambigüedades de spec.md

Fecha y hora: 29/10/2026 10:54
Comando (desde laboratorio_sdd, prompt por entrada estándar): `claude -p --model sonnet`

## Prompt

```text
Revisa esta especificación como analista QA. Identifica
contradicciones, reglas no comprobables o decisiones implícitas.
Devuélveme preguntas y cambios propuestos, NO código.
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
```

## Respuesta de la IA

# Revisión QA: especificación de préstamos v1.0

## 1. Contradicciones e inconsistencias

| # | Hallazgo | Dónde |
|---|---|---|
| C1 | **"Todo error produce ValueError" no se puede cumplir tal cual.** `9999-12-31 + 14 días` desborda. Una entrada que no sea texto (`None`, `int`, `date`) normalmente produce `TypeError`. Ninguno de los dos casos está contemplado. | Cierre vs. R02, R03, R04 |
| C2 | **`devuelto` no se inicializa.** R01 dice "agrega un dict", pero nunca dice que nace con `devuelto=False`. R05 y R06 dependen de ese valor. | R01 vs. Estructura |
| C3 | **R04 y R01 no dicen si `strip()` ocurre antes o después de validar.** "Los textos se recortan" no aclara si la fecha cuenta como texto. `" 2026-01-05 "` sería válida o inválida según el orden. | R01, R03, R04 |
| C4 | **R07 no dice si `devolver_prestamo` recorta sus argumentos.** Si registro `"Ana "` y devuelvo con `"Ana "`, el valor guardado es `"Ana"` y no coincide. | R01 vs. R07 |
| C5 | **El objetivo habla de "registrar y devolver", pero no hay consulta ni listado.** Nadie puede comprobar los límites de R05 y R06 sin leer la lista a mano. Es una laguna de alcance, no un error. | Objetivo |

## 2. Reglas no comprobables o ambiguas

- **R03, "fecha válida".** No dice qué rango de años es válido, ni si `2026-1-5` (sin ceros) cumple el formato. Tampoco dice si se permiten fechas futuras o muy antiguas. Falta una lista cerrada de casos válidos e inválidos.
- **R05 y R06, "activo".** Nunca se define. Se entiende como `devuelto == False`, pero debe decirse.
- **R06, identidad del libro.** Se identifica por el texto. No se define si `"Quijote"` y `"quijote"` son el mismo libro, ni si cuentan los acentos o los espacios internos (`"Don  Quijote"`). Lo mismo aplica al usuario en R05. Sin esto, el límite no se puede probar.
- **R08.** Reúne dos casos ("inexistente" y "ya devuelto") bajo el mismo `ValueError`. Si no hay mensaje o tipo definido, ninguna prueba puede distinguir qué falló. Pasa igual con R03 al R06, que también acaban en `ValueError`.
- **"No modifica la lista".** No dice si también protege los dicts ya existentes. Tampoco dice qué pasa si `prestamos` no es una lista o contiene registros mal formados.
- **R01 y R07, "lo devuelve".** No aclara si es el mismo objeto que está en la lista o una copia. Esto cambia lo que prueba un test (`is` o `==`).

## 3. Decisiones implícitas que deberían ser explícitas

1. Se puede volver a prestar un libro ya devuelto, y por el mismo usuario. Se infiere de R06, pero no está escrito.
2. Un libro es una sola copia. Un título equivale a un ejemplar.
3. No se registra fecha de devolución. Se entiende que es por la exclusión de multas, pero hay que confirmarlo.
4. Se permite registrar préstamos con fecha pasada o futura, sin comparar con la fecha actual. Hoy no hay reloj en la spec, así que no hay nada que probar al respecto.
5. Cuando una entrada rompe varias reglas a la vez (por ejemplo R05 y R06), no hay orden de validación definido.
6. La lista se modifica en el lugar. La spec no dice si ese efecto lateral es deseado.
7. Si `devolver_prestamo` recibe un libro prestado a otro usuario, se trata como "inexistente".
8. `fecha_prestamo` se guarda normalizada. No se dice si se guarda tal cual la recibió o ya limpia.

## 4. Preguntas para el autor

1. ¿Qué tipos de entrada se aceptan? ¿Un `TypeError` para entradas que no son texto es aceptable, o también debe ser `ValueError`?
2. ¿Cuál es el rango de años permitido? ¿Qué se hace en `9999-12-31`?
3. ¿`2026-1-5` es válida, o el formato exige ceros (`2026-01-05`)?
4. ¿La comparación de usuario y libro distingue mayúsculas, acentos y espacios internos?
5. ¿El orden de validación es fijo? Si lo es, ¿cuál es?
6. ¿Los errores llevan un mensaje distinguible (por ejemplo, un código por regla)?
7. ¿`devolver_prestamo` también recorta los textos?
8. ¿Se devuelve el mismo dict que está en la lista o una copia?
9. Si hay un usuario con 3 préstamos activos y uno se devuelve, ¿puede registrar otro de inmediato?
10. ¿Qué hacer con una lista de entrada inválida (`None`, no lista, registros sin las claves esperadas)?

## 5. Cambios propuestos a la especificación

- **R01:** añadir que el dict nace con `devuelto=False`. Fijar el orden: primero recortar usuario y libro, luego validar. Aclarar que la fecha se valida tal cual llega, sin recortar. Indicar que se devuelve el mismo objeto insertado.
- **R02:** quedan fuera de rango las fechas cuyo resultado supere `9999-12-31`; eso produce `ValueError`.
- **R03:** sustituir "válida" por una definición cerrada. Por ejemplo: exactamente 10 caracteres, `AAAA-MM-DD` con ceros, calendario real (incluidos bisiestos) y años entre 1900 y 9998. Agregar una tabla de ejemplos válidos e inválidos.
- **R04:** exigir que usuario y libro sean `str`, o decir que cualquier otro tipo produce `ValueError`.
- **R05 y R06:** definir "activo = `devuelto == False`". Definir la clave de comparación (por ejemplo, texto recortado y sensible a mayúsculas, o sin distinguir mayúsculas). Aclarar que la comparación excluye la entrada que se está registrando.
- **R07:** indicar que usuario y libro se recortan igual que en R01. Indicar que se busca el préstamo activo con ese par y que, si no existe, se aplica R08.
- **R08:** separar los dos casos con mensajes distintos, o declarar explícitamente que no se distinguen.
- **Estructura:** especificar el tipo de `fecha_prestamo` (`str AAAA-MM-DD`) y de `devuelto` (`bool`). Añadir una cláusula sobre `prestamos` inválido.
- **Cierre:** reescribir como "Todo error de validación produce `ValueError`, incluidas las entradas de tipo incorrecto y el desbordamiento de fecha. La lista y sus elementos quedan idénticos a como estaban antes de la llamada". Así se puede probar comparando una copia profunda de antes y después.
- **Versión:** pasar a 1.1 y añadir una sección "Supuestos" con los puntos de la sección 3.

Si quiere, convierto esto en una matriz de trazabilidad (regla → casos de prueba) cuando se aclaren las preguntas.
