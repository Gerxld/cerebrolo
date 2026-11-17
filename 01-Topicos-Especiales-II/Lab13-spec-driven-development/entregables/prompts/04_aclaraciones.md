# Paso 4. Pedir aclaraciones a la IA (sin código)

Fecha y hora: 29/10/2026 10:53
Comando (desde laboratorio_sdd, prompt por entrada estándar): `claude -p --model sonnet`

## Prompt

```text
Actúa como analista de requisitos. Necesito un gestor de préstamos
de libros para un laboratorio. Haz preguntas sobre reglas ambiguas,
casos límite y datos de entrada. NO generes código ni arquitectura.
```

## Respuesta de la IA

# Gestor de préstamos de libros: preguntas de levantamiento de requisitos

Agrupé las preguntas por tema. Marqué con ⭐ las que más cambian el alcance, para que empecemos por esas.

## 1. Contexto y alcance
1. ⭐ ¿Qué se presta: solo libros físicos, o también manuales, revistas, tesis, material digital o equipos?
2. ⭐ ¿Quién usa el sistema: solo el encargado del laboratorio, o los estudiantes también (autoservicio)?
3. ¿Hay un sistema o registro previo (Excel, cuaderno) del que haya que migrar datos?
4. ¿Cuántos libros y usuarios se esperan aproximadamente? ¿Hay varias sedes o laboratorios?

## 2. Libros y ejemplares
5. ⭐ ¿Un título puede tener varios ejemplares? ¿Se prestan y controlan por separado?
6. ¿Qué datos son obligatorios de un libro (título, autor, ISBN, edición, código interno)? ¿El ISBN es único?
7. ¿Hay libros que no se pueden sacar del laboratorio (solo consulta en sala)?
8. ¿Se pueden dar de baja libros (perdidos, dañados)? ¿Qué pasa con su historial?
9. ¿Se necesita registrar el estado físico del libro al prestarlo y al devolverlo?

## 3. Usuarios
10. ⭐ ¿Quién puede pedir prestado: estudiantes, docentes, personal externo? ¿Los límites son distintos por tipo?
11. ¿Qué datos identifican al usuario (cédula, carné, correo, teléfono)? ¿Hay que validar que sea un usuario activo?
12. ¿Un usuario puede quedar bloqueado o sancionado? ¿Quién lo decide y cómo se levanta?

## 4. Reglas del préstamo
13. ⭐ ¿Cuántos libros puede tener prestados a la vez una misma persona?
14. ⭐ ¿Cuál es el plazo estándar de préstamo (días, horas)? ¿Varía por tipo de libro o de usuario?
15. ¿Los plazos cuentan días calendario o hábiles? ¿Qué pasa si vence en fin de semana, feriado o cierre del laboratorio?
16. ¿Se puede renovar? ¿Cuántas veces, y con qué condiciones (por ejemplo, que nadie lo haya reservado)?
17. ¿Se permiten reservas o lista de espera cuando un libro está prestado?
18. ¿Se puede prestar un libro a alguien que ya tiene un vencido pendiente?
19. ¿Quién autoriza el préstamo: es automático o requiere aprobación?

## 5. Devoluciones y sanciones
20. ⭐ ¿Hay multas o penalizaciones por atraso? ¿Son monetarias, bloqueo temporal, o ambas?
21. Si hay multa, ¿cómo se calcula (por día, por libro, con tope máximo)? ¿Se registra el pago?
22. ¿Qué pasa si un libro se devuelve dañado o se pierde? ¿Se cobra reposición?
23. ¿Se permiten devoluciones parciales (devuelve 2 de 3 libros)?
24. ¿Alguien más (otra persona) puede devolver el libro en nombre del usuario?

## 6. Casos límite
25. ¿Qué hacer si se intenta prestar un ejemplar ya prestado, o devolver uno que no figura como prestado?
26. ¿Puede alguien tomar el mismo título dos veces a la vez (dos ejemplares)?
27. Si se corrige un error de registro (préstamo equivocado), ¿se permite anular o editar? ¿Queda rastro?
28. ¿Se puede registrar un préstamo con fecha pasada (por ejemplo, se olvidó anotarlo)?
29. ¿Qué pasa con los préstamos activos al cierre del semestre o si el usuario se retira?

## 7. Datos de entrada y salida
30. ⭐ ¿Qué datos exactos se capturan en un préstamo (usuario, libro, fecha, fecha de vencimiento, observaciones, quién lo registró)?
31. ¿Los datos se ingresan a mano o hay escáner de código de barras / carné?
32. ¿Qué formatos y validaciones se esperan (ISBN válido, fechas, longitudes de texto)?
33. ¿Qué consultas y reportes se necesitan: préstamos vencidos, historial por usuario, libros más prestados, disponibilidad?
34. ¿Hay que exportar o imprimir algo (comprobante, reporte en Excel/PDF)?

## 8. No funcionales
35. ¿Necesita autenticación y roles (administrador, auxiliar)? ¿Quién puede modificar el catálogo?
36. ¿Se notifica a los usuarios (correo, aviso de vencimiento)?
37. ¿Hay restricciones de privacidad sobre los datos de usuarios y su historial?
38. ¿Hay restricciones tecnológicas del laboratorio (sistema operativo, sin internet, entrega única)?

---

**Para avanzar rápido**, respóndeme primero las ⭐ (preguntas 1, 2, 5, 10, 13, 14, 20 y 30). Con eso puedo redactar una primera versión de los requisitos y dejar marcado lo que quede pendiente como supuesto. Si algo no está definido, dímelo y lo anoto como "decisión pendiente" en vez de inventarlo.
