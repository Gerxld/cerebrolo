# CLAUDE.md — Gerencia de Proyectos Informáticos

Reglas específicas de esta materia. Las reglas generales (formato UTP, tipos de trabajo, estructura de carpetas, skills, "no inventar") están en `C:\Cerebrolo\CLAUDE.md` y no se repiten aquí. Si algo choca, manda este archivo; por encima manda el enunciado del profesor. Español panameño neutro, con tuteo, nunca voseo.

## Identidad de las entregas

| Campo | Valor |
|---|---|
| Asignatura | Gerencia de Proyectos Informáticos (teoría + laboratorio) |
| Grupo | `[PENDIENTE: confirmar]` |
| Profesor | `[PENDIENTE]` |
| Teoría | Martes 5:50–8:15 p.m., aula 3-306 |
| Laboratorio | Miércoles 5:50–7:25 p.m., aula 3-411 |
| Estudiante | Ríos, Gerald (8-987-741) |
| Integrantes de grupo | `[PENDIENTE]` |

No inventes integrantes, cédulas ni el nombre del profesor. Mientras estén pendientes, la portada lleva el marcador `[PENDIENTE]` visible y se avisa a Gerald antes de cerrar el PDF. Cuando se confirmen, se anotan en esta tabla y no se vuelven a preguntar.

## Teoría y laboratorio

Esto es una suposición razonable, **por confirmar con el sílabo y el primer enunciado**. No la trates como regla hasta confirmarla.

| | Teoría (martes) | Laboratorio (miércoles) |
|---|---|---|
| Producción habitual | Asignaciones, investigaciones, casos de estudio, parciales, quizzes, posible exposición | Aplicar la teoría a un proyecto: artefactos de gestión sobre un caso o proyecto de curso, a menudo en grupo |
| Formato por defecto | Asignación o investigación según el verbo del enunciado ("responda" vs. "investigue") | Laboratorio o proyecto, con informe y evidencias |
| Evidencia | Argumentación y fuentes | Artefactos completos y cálculos reproducibles (Gantt, EDT, tablas, hojas de cálculo) |

Un entregable de proyecto suele ir acumulándose entre laboratorios: lo que se entrega en un laboratorio es insumo del siguiente (el alcance alimenta la EDT, la EDT al cronograma, el cronograma al presupuesto). Guarda la coherencia entre entregas: mismo nombre de proyecto, mismos supuestos, mismas cifras base. Si un dato cambia, revisa los artefactos anteriores que lo usan.

## Marco metodológico de referencia

Usa el marco que pida el enunciado. Si no pide ninguno, cita el que corresponda y dilo expresamente.

- **PMBOK Guide, 7ª ed. (PMI, 2021).** Se organiza en 12 principios (administración, equipo, interesados, valor, pensamiento sistémico, liderazgo, adaptación al contexto, calidad, complejidad, riesgo, adaptabilidad y resiliencia, cambio) y 8 dominios de desempeño (interesados, equipo, enfoque de desarrollo y ciclo de vida, planificación, trabajo del proyecto, entrega, medición, incertidumbre). Ya no está organizada por procesos.
- **PMBOK Guide, 6ª ed. (PMI, 2017).** Es la vista que los cursos latinoamericanos siguen enseñando: 49 procesos, 5 grupos de procesos (inicio, planificación, ejecución, monitoreo y control, cierre) y 10 áreas de conocimiento (integración, alcance, cronograma, costos, calidad, recursos, comunicaciones, riesgos, adquisiciones, interesados). Los artefactos del catálogo siguen sobre todo esta vista.
- **Scrum Guide 2020 (Schwaber y Sutherland).** Un equipo Scrum; tres roles (Product Owner, Scrum Master, Developers); cinco eventos (Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective); tres artefactos con su compromiso (Product Backlog con Product Goal, Sprint Backlog con Sprint Goal, Incremento con Definition of Done).
- **Enfoques híbridos.** Planificación de alcance, presupuesto y riesgos de forma predictiva a alto nivel, con ejecución iterativa en sprints. Si el enunciado pide un híbrido, explica qué parte es predictiva, cuál es ágil y por qué.

Aclara siempre qué edición usas. No mezcles terminología de las dos ediciones sin decirlo.

## Catálogo de artefactos

Para cada uno: lo que debe llevar y cómo se renderiza. Diagramas (EDT, Gantt, red) con la skill `diagramas`; matrices y tablas en HTML dentro de `informe-utp`; hoja de cálculo con la skill global `xlsx` solo si el enunciado la pide o si el cálculo es largo y conviene entregarlo editable.

**Acta de constitución (project charter).** Título y propósito/justificación, objetivos medibles, requisitos de alto nivel, descripción y entregables principales, riesgos de alto nivel, hitos, presupuesto estimado, criterios de éxito, interesados clave, gerente del proyecto con su autoridad, patrocinador y firmas. Tabla en HTML.

**Enunciado del alcance.** Descripción del alcance del producto, entregables, criterios de aceptación, exclusiones (lo que no entra), supuestos y restricciones. Las exclusiones explícitas evitan el crecimiento descontrolado del alcance.

**EDT/WBS y diccionario.** Descomposición jerárquica por entregables, no por actividades; regla del 100% (los hijos suman todo el trabajo del padre, sin solapes); codificación 1, 1.1, 1.1.1; paquetes de trabajo en el nivel más bajo. Diccionario: código, nombre, descripción del trabajo, responsable, entregables, criterios de aceptación, duración/costo estimado. EDT con `diagramas` (árbol); diccionario como tabla HTML.

**Cronograma (Gantt y CPM).** Lista de actividades con duración, predecesoras y tipo de dependencia (FS por defecto). Pasada hacia adelante: ES de la primera actividad = 0 (o 1; declara la convención y úsala siempre), EF = ES + duración, ES de una actividad = máximo EF de sus predecesoras. Pasada hacia atrás: LF de la última = EF del proyecto, LS = LF − duración, LF de una actividad = mínimo LS de sus sucesoras. Holgura = LS − ES (= LF − EF). Ruta crítica: actividades con holgura 0; el camino más largo de la red. Gantt con `diagramas`; tabla ES/EF/LS/LF/holgura en HTML; diagrama de red también con `diagramas`.

**Estimaciones.** PERT: E = (O + 4M + P) / 6, desviación estándar = (P − O) / 6, varianza = ((P − O) / 6)². Para una ruta, suma las esperanzas y las varianzas (no las desviaciones), y la desviación de la ruta es la raíz de la suma de varianzas. Tabla con actividad, O, M, P, E, σ. Indica la unidad (días, horas, semanas). Otras técnicas válidas: análoga, paramétrica, ascendente.

**Presupuesto y línea base de costos.** Costos por paquete de trabajo (recursos × tarifa × tiempo), costos directos e indirectos, reserva para contingencia (sobre riesgos identificados) y reserva de gestión (fuera de la línea base). Línea base de costos = costos por actividad agregados en el tiempo, sin reserva de gestión; presupuesto = línea base + reserva de gestión. Tabla en HTML o `xlsx`; curva S con gráfico si se pide.

**Valor ganado (EVM).**

| Medida | Fórmula |
|---|---|
| BAC | Presupuesto total en la conclusión |
| PV | % de avance planificado × BAC |
| EV | % de avance real × BAC |
| AC | Costo real acumulado |
| CV | EV − AC |
| SV | EV − PV |
| CPI | EV / AC |
| SPI | EV / PV |
| EAC (tendencia actual) | BAC / CPI |
| EAC (variación atípica) | AC + (BAC − EV) |
| ETC | EAC − AC |
| VAC | BAC − EAC |
| TCPI (sobre BAC) | (BAC − EV) / (BAC − AC) |

Indica cuál fórmula de EAC usas y por qué. Interpreta: CV o SV negativos, y CPI o SPI menores que 1, significan sobrecosto o atraso. Presenta los datos de entrada, la tabla de cálculo y una lectura de una o dos frases.

**Matriz de riesgos.** Registro con id, descripción (causa, evento, efecto), categoría, probabilidad, impacto, puntaje = probabilidad × impacto, estrategia de respuesta, acciones, responsable, disparador y estado. Escalas numéricas definidas antes de usarlas (por ejemplo 1–5). Respuesta a amenazas: evitar, transferir, mitigar, aceptar (y escalar); a oportunidades: explotar, compartir, mejorar, aceptar. Incluye la matriz de calor probabilidad × impacto como tabla HTML con celdas coloreadas.

**Registro de interesados y matriz poder/interés.** Registro: nombre o rol, organización, función en el proyecto, requisitos/expectativas, influencia, interés, actitud actual y deseada, estrategia. Matriz: cuadrantes poder alto/bajo × interés alto/bajo (gestionar de cerca, mantener satisfechos, mantener informados, monitorear). Tabla HTML o gráfico de cuadrantes.

**RACI.** Filas = entregables o actividades, columnas = roles o personas. Cada fila lleva exactamente una A (Accountable) y al menos una R (Responsible); C (consultado) e I (informado) según corresponda. Revisa que no haya filas sin A ni con dos A. Tabla HTML.

**Plan de comunicaciones.** Información a comunicar, emisor, receptor/audiencia, método o canal, frecuencia, responsable, formato y registro. Debe cuadrar con el registro de interesados: todo interesado relevante aparece.

**Lecciones aprendidas.** Qué se planeó, qué ocurrió, causa, impacto, lección y recomendación, por área de conocimiento o fase. Redacta con hechos del proyecto real; sin lecciones genéricas.

**Product backlog e historias de usuario.** Historia: "Como [rol] quiero [necesidad] para [beneficio]". Evalúa con INVEST (independiente, negociable, valiosa, estimable, pequeña, verificable). Criterios de aceptación verificables, en lista o en Dado/Cuando/Entonces. Backlog con id, historia, prioridad (MoSCoW o valor), estimación (puntos de historia o horas), criterios y estado, ordenado por prioridad. Si hay sprints: sprint goal, sprint backlog y una definición de terminado.

## Reglas de cálculo y fechas

- Todo cálculo se muestra con su procedimiento (fórmula, valores sustituidos, resultado) y se **verifica dos veces**: recalcula con otro método o en código (Python) y compara antes de entregar.
- Redondeo uniforme: 2 decimales en índices (CPI, SPI), moneda con 2 decimales, y dilo una vez.
- En el Gantt las fechas tienen que cuadrar: duración = fin − inicio según el calendario laboral declarado (días hábiles, feriados de Panamá si aplican), las predecesoras no empiezan antes de que terminen sus dependencias, y las fechas del cronograma coinciden con las de la tabla CPM, el hito del acta y el presupuesto por periodo.
- La suma de la EDT, el presupuesto y la línea base de costos deben dar la misma cifra total.
- Las cifras del caso o proyecto vienen del enunciado o de supuestos declarados. No inventes datos de una empresa real; si hace falta un supuesto, márcalo como tal.

## Bibliografía base

Obras reales y conocidas. Verifica edición y año contra el sílabo antes de citar, y consulta la fuente antes de poner la referencia (skill `investigacion-apa`).

- Project Management Institute. *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*. PMI. Ediciones 6ª (2017) y 7ª (2021): verificar edición contra el sílabo.
- Schwaber, K. y Sutherland, J. *The Scrum Guide* (2020). Disponible en scrumguides.org: verificar versión y traducción al español.
- Gido, J. y Clements, J. P. *Administración exitosa de proyectos*. Cengage Learning: verificar edición contra el sílabo.
- Si el sílabo lista otros textos, esos mandan.

## Reglas del profesor descubiertas

Se agregan aquí a medida que llegan los enunciados, con la fecha y de dónde salió la regla.

(vacío)

## Formato específico

`[PENDIENTE: confirmar con sílabo/primer enunciado]`

Mientras tanto se hereda el formato de `C:\Cerebrolo\CLAUDE.md` según el tipo de trabajo.
