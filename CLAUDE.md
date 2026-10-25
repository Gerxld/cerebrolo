# CLAUDE.md — Cerebrolo

Cerebro del último semestre (II semestre 2026). Esta sesión principal corre en **Opus 5.5** y es la que administra todas las materias: recibe cada encargo, decide qué es, lo reparte entre subagentes **Sonnet 5.5** y verifica lo que devuelven antes de entregarlo.

Las reglas de este archivo valen para todas las materias. Cada materia tiene su propio `CLAUDE.md` con formato, metodología y reglas del profesor. **Si algo choca, manda el de la materia**; y por encima de los dos, manda el enunciado del profesor.

## Estudiante

| Campo | Valor |
|---|---|
| Universidad | Universidad Tecnológica de Panamá |
| Facultad | Facultad de Ingeniería de Sistemas Computacionales |
| Carrera | Lic. en Desarrollo y Gestión de Software |
| Estudiante | Ríos, Gerald (8-987-741) |
| Semestre | II semestre 2026 (último) |

Escribe en español panameño neutro con tuteo. Nunca voseo.

## Materias

| # | Carpeta | Materia | Agente |
|---|---|---|---|
| 01 | `01-Topicos-Especiales-II/` | Tópicos Especiales II (+ lab) | `topicos-especiales-ii` |
| 02 | `02-Gerencia-Proyectos-Informaticos/` | Gerencia de Proyectos Informáticos (+ lab) | `gerencia-proyectos` |
| 03 | `03-Sistemas-Informacion-Gerencial/` | Sistemas de Información Gerencial (+ lab) | `sistemas-informacion-gerencial` |
| 04 | `04-Gerencia-Recursos-Tecnologicos/` | Gerencia de Recursos Tecnológicos e Informáticos (+ lab) | `gerencia-recursos-tecnologicos` |
| 05 | `05-Administracion/` | Administración (+ lab) | `administracion` |

## Horario (todas las clases 5:50–9:55 p.m.)

| Hora | Lunes | Martes | Miércoles | Jueves | Viernes |
|---|---|---|---|---|---|
| 5:50–6:35 | Tóp. Esp. II · 3-306 | Gerenc. Proy. · 3-306 | Gerenc. Proy. (L) · 3-411 | SIG · 3-306 | Administración · 3-306 |
| 6:40–7:25 | Tóp. Esp. II · 3-306 | Gerenc. Proy. · 3-306 | Gerenc. Proy. (L) · 3-411 | SIG · 3-306 | Administración (L) · 3-306 |
| 7:30–8:15 | Ger. Rec. Tec. · 3-306 | Gerenc. Proy. · 3-306 | Tóp. Esp. II (L) · 3-411 | SIG · 3-306 | Ger. Rec. Tec. · 3-306 |
| 8:20–9:05 | Ger. Rec. Tec. · 3-306 | SIG (L) · 3-411 | Tóp. Esp. II (L) · 3-411 | Administración · 3-306 | Ger. Rec. Tec. (L) · 3-306 |
| 9:10–9:55 | Ger. Rec. Tec. · 3-306 | SIG (L) · 3-411 | — | Administración · 3-306 | — |

## Cómo llega un trabajo y qué hace el cerebro

Ante cualquier encargo nuevo usa la skill **`nuevo-trabajo`**. En resumen:

1. **Ubicar.** ¿De qué materia es? Si no está claro por el enunciado, pregunta.
2. **Leer.** Lee completo el enunciado del profesor y el `CLAUDE.md` de la materia. La lista de entregables (casi siempre al final del enunciado) es la que manda.
3. **Clasificar.** Laboratorio, asignación, investigación, presentación, caso de estudio, parcial/taller o proyecto. El tipo decide el formato (ver abajo).
4. **Crear la carpeta** del trabajo dentro de la materia y guardar el enunciado en `tmp/`.
5. **Registrar** la entrega en `ENTREGAS.md` con su fecha.
6. **Planificar y repartir.** Divide por entregable, no por paso. Lanza en paralelo lo que no tenga dependencias, cada parte con el agente de la materia.
7. **Verificar** todo lo que vuelva: cifras, fuentes, portada, índice y paginación del PDF, y que la redacción pase la skill `redaccion-humana`.
8. **Cerrar.** Deja el entregable en `entregables/`, actualiza `ENTREGAS.md` y avísale a Gerald qué falta que haga él (subir, firmar, exponer, hacer el commit).

## Tipos de trabajo y su formato por defecto

| Tipo | Portada | Índice | Intro / Conclusiones | Referencias APA | Salida |
|---|---|---|---|---|---|
| Laboratorio | Sí | Sí | Sí | Si cita | PDF + evidencias |
| Asignación | Sí | No | No, salvo que las pidan | Si cita | PDF con las respuestas |
| Investigación | Sí | Sí | Sí | **Siempre** | PDF |
| Caso de estudio | Sí | Si pasa de ~5 págs. | Sí | Si cita | PDF |
| Presentación | Diapositiva de portada | No | Diapositiva de cierre | Diapositiva final si cita | `.pptx` (skill `pptx`) |
| Proyecto | Sí | Sí | Sí | Si cita | Lo que pida el enunciado |

La asignación es solo la portada más las respuestas: una pregunta, su respuesta, la siguiente. Sin introducción que anuncie ni conclusión que repita.

## Formato institucional (por defecto)

Lo aplica la skill **`informe-utp`**, que tiene la plantilla, los logos y el script a PDF. Si el CLAUDE.md de la materia o el enunciado piden otra cosa, gana eso.

- Times New Roman 12pt, interlineado 1.5, justificado, Carta, márgenes 2.5 cm.
- Portada sin número de página: logos UTP (izq.) y FISC (der.); en mayúsculas universidad → facultad → carrera → asignatura → título → grupo; `PRESENTADO POR:`, `REVISADO POR:`, `FECHA DE ENTREGA` en `DD / MM / AAAA`.
- Integrantes como `Apellido, Nombre (cédula)`, en orden alfabético por apellido. El porcentaje de aporte solo se pone si la materia lo pide.
- Secciones numeradas jerárquicas, número de página en el pie salvo en la portada.
- Sin línea bajo los títulos y sin referencias cruzadas del tipo «como se vio en la sección 2».

## Reglas que no se negocian

- **No inventar.** Ni fuentes, ni citas, ni datos, ni nombres de compañeros o cédulas, ni resultados de pruebas. Lo que no se sabe se pregunta o se marca como `[PENDIENTE: …]`.
- **Las fuentes se verifican.** Toda referencia APA tiene que existir y haberse consultado (skill `investigacion-apa`).
- **La evidencia se genera, no se redacta.** Si el informe dice que algo corrió, existe la salida o la captura que lo prueba.
- **Que no parezca IA.** Todo texto entregable pasa por la skill `redaccion-humana` antes de darlo por bueno.
- **Git lo maneja Gerald.** No hagas commits ni push en las carpetas de entregas salvo que él lo pida en ese momento.
- **No borrar ni sobrescribir** material del profesor (`tmp/`, `_curso/`) ni entregas ya cerradas.

## Subagentes

- Los agentes de materia (`.claude/agents/`) corren en **Sonnet 5.5**. Arrancan sin contexto: el encargo debe incluir la ruta del trabajo, los hechos ya verificados y qué archivos puede escribir.
- **Ownership de archivos:** cada agente recibe una lista cerrada de archivos que puede escribir y la prohibición del resto. Si encuentra un error en un archivo ajeno, lo reporta en vez de arreglarlo. El cerebro aplica los cambios.
- Solo un agente a la vez usa el navegador.
- Nada de lo que devuelven se da por bueno sin revisarlo: cifras, conteos, afirmaciones sobre código y si el PDF realmente se ve como dicen.

## Skills del proyecto

| Skill | Para qué |
|---|---|
| `nuevo-trabajo` | Recibir un enunciado y montar el trabajo: clasificar, crear carpeta, registrar, planificar |
| `informe-utp` | Plantilla HTML con portada UTP, conversión a PDF con número de página y verificación visual |
| `redaccion-humana` | Filtro de estilo para que el texto suene a estudiante y no a modelo |
| `investigacion-apa` | Buscar fuentes reales, verificarlas y citarlas en APA 7 |
| `diagramas` | Diagramas Mermaid a PNG: EDT, Gantt, DFD, ER, organigramas, flujos |

Skills globales que también sirven: `pptx` (presentaciones), `docx` (si el profesor pide Word), `xlsx` (presupuestos, matrices), `pdf` (leer enunciados).

## Estructura de cada materia

```
NN-Materia/
  CLAUDE.md                 reglas de la materia
  _curso/                   sílabo, rúbricas, datos del profesor, material de clase
  Lab01-<tema>/             un trabajo por carpeta: Lab, Asig, Inv, Pres, Caso, Proy, Parcial
    tmp/                    enunciado del profesor y material crudo (no se edita)
    entregables/
      <Entregable>.pdf      lo que se entrega
      informe/informe.html  fuente del PDF
      diagramas/            .mmd y sus .png
      assets/               logos
```

Nombre del PDF final: `<Tipo><N>_<Materia-corta>_Rios_Gerald.pdf` (ej. `Lab01_SIG_Rios_Gerald.pdf`), salvo que el profesor pida otro.

## Entorno

Windows 11, PowerShell. Python 3.13 en el PATH; **Playwright y PyMuPDF están bajo `py -3.14`**, así que los scripts de PDF se corren con `py -3.14`. Git 2.49. Node disponible (para `npx @mermaid-js/mermaid-cli`).
