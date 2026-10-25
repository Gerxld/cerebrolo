# CLAUDE.md — Tópicos Especiales II

Reglas de esta materia. Complementan al `CLAUDE.md` raíz de Cerebrolo y, si algo choca, manda este archivo; por encima de ambos manda el enunciado del profesor. Aquí solo va lo propio de Tópicos Especiales II; el formato institucional general (Times 12, interlineado 1.5, Carta, márgenes, portada con logos, sin línea bajo títulos ni referencias cruzadas) está en el `CLAUDE.md` raíz y en la skill `informe-utp`.

## Identidad de las entregas

| Campo | Valor |
|---|---|
| Universidad | Universidad Tecnológica de Panamá |
| Facultad | Facultad de Ingeniería de Sistemas Computacionales |
| Carrera | Lic. en Desarrollo y Gestión de Software |
| Asignatura | Tópicos Especiales II |
| Grupo | 1GS241 |
| Profesor | Regis Rivera |
| Estudiante | Ríos, Gerald (8-987-741) |

En la portada, `REVISADO POR:` lleva a **Profesor Regis Rivera**. En trabajos grupales cada integrante se lista como `Apellido, Nombre (cédula)`, ordenados alfabéticamente por apellido. **Sin porcentaje de aporte.**

Compañeros de grupo: `[en la copia pública se quitaron sus nombres y cédulas; cada quien pone aquí su propio grupo]`.

| Integrante | Cédula |
|---|---|
| Apellido, Nombre | X-XXX-XXXX |

Si aparece un integrante nuevo, pregunta por sus datos en vez de inventarlos.

## Horario

| Sesión | Día | Hora | Aula |
|---|---|---|---|
| Teoría | Lunes | 5:50–7:25 p.m. | 3-306 |
| Laboratorio | Miércoles | 7:30–9:05 p.m. | 3-411 |

## Trabajos anteriores

Lab1, Lab2, Lab3 y Asig2 / Asigna2 viven en `C:\Topicos2026\Topicos2\`. Son históricos: léelos como referencia de estilo, estructura y nivel de detalle, pero **no los modifiques**. El trabajo nuevo va en esta carpeta de Cerebrolo, siguiendo la estructura de abajo.

## Laboratorio o asignación: no son lo mismo

Antes de escribir nada, mira qué tipo de entrega es. El peso del formato cambia por completo.

| | **Laboratorio** | **Asignación** |
|---|---|---|
| Qué es | Informe de un proceso con evidencias | Responder lo que el enunciado pregunta |
| Portada | Sí | Sí |
| Índice paginado | Sí | No |
| Introducción | Sí | No |
| Secciones numeradas jerárquicas | Sí | No — una por pregunta, y ya |
| Conclusiones | Sí | No, salvo que el enunciado las pida |
| Extensión típica | La que exija la evidencia | Lo que ocupe responder |

**La asignación es solo la portada más las respuestas.** Una pregunta del enunciado, su respuesta, la siguiente. Si pide un diagrama, va el diagrama. Nada de introducción que anuncie lo que se va a decir, ni conclusión que repita lo ya dicho, ni índice para tres páginas. Responder lo que se pide y hacer lo que se hace.

El formato completo aplica a **laboratorios**. De él, la asignación hereda solo la portada y la tipografía.

Particularidades del informe de laboratorio en esta materia:

- Los ejes o partes temáticas suelen abrirse con Contexto → Análisis → Postura del grupo.
- Cierre con **Conclusiones** y, cuando el trabajo cite fuentes, **Referencias Bibliográficas** en APA (skill `investigacion-apa`).
- Registro académico en primera persona del plural ("el grupo considera", "verificamos").
- El índice se verifica contra la paginación real del PDF, no se estima.

## Reglas del profesor para los laboratorios de IA

El curso recorre tres modalidades de asistencia por IA, una por laboratorio: **autocompletar** → **chat web** → **editor con IA**. Cada enunciado repite el mismo bloque de restricciones, y son la parte que realmente se evalúa:

- No usar un chat web externo para resolver las tareas cuando el laboratorio es de otra modalidad.
- No activar aceptación automática de cambios. Cada diff se revisa antes de conservarlo.
- **No hacer commits automáticos ni delegar decisiones de Git a la IA.** El estudiante crea su propio commit manual al cerrar.
- Las pruebas se ejecutan manualmente desde la terminal del estudiante.
- Si la IA toca un archivo que no debía cambiar, se rechaza ese cambio y se ajusta la solicitud.
- No entregar código que no se pueda explicar.

Consecuencia práctica al asistir: propón el conjunto mínimo de archivos, no ejecutes acciones de Git, y nunca debilites una prueba para que pase — si falla, la corrección va en la implementación.

## Patrón de entregables (laboratorios)

Los enunciados de laboratorio piden casi siempre la misma evidencia. Antes de dar uno por terminado, revisa que exista:

1. Carpeta final con todo el código trabajado.
2. Evidencia de la suite de pruebas **antes y después** del cambio.
3. Captura o evidencia de al menos un **diff multiarchivo**.
4. Registro de un cambio **aceptado** y uno **rechazado**, con justificación.
5. El plan que propuso la IA más la **evaluación crítica del estudiante**.
6. Respuestas a las **preguntas de reflexión**, en PDF.

El registro de cambios rechazados es lo que distingue una entrega buena de una mediocre: debe mostrar criterio propio (sobreingeniería, cambios fuera de alcance, interfaces tocadas sin necesidad), no un rechazo de trámite.

En una **asignación** nada de esto aplica. Lo que manda es la última línea del enunciado: casi siempre «entregar las respuestas en formato PDF». Eso es todo lo que hay que producir.

## Estructura de carpetas

Sigue la estructura de materia del `CLAUDE.md` raíz (`_curso/`, una carpeta por trabajo, `tmp/`, `entregables/`). Para los laboratorios de esta materia se añade lo del código y la evidencia:

```
LabNN-<tema>/
  CLAUDE.md                 reglas específicas de ese laboratorio
  <proyecto>/               el código que pide el enunciado
  entregables/
    Informe_*.pdf           informe final
    informe/informe.html    fuente del PDF
    *.md                    plan, registro de cambios, reflexión
    *.txt                   salidas literales de terminal
    screenshots/            figuras
    assets/                 logos
    _snapshot_antes/        estado previo, lado izquierdo del diff
  tmp/                      enunciado del profesor y plantillas
```

`_snapshot_antes/` no se edita nunca: es lo que hace posible regenerar el diff.

Una asignación necesita mucho menos, porque no hay código ni evidencias que guardar:

```
AsigNN-<tema>/
  entregables/
    Informe_*.pdf           el PDF que se entrega
    informe/informe.html    fuente del PDF
    diagramas/              fuentes .mmd y sus .png, si el enunciado pide diagramas
    assets/                 logos
  tmp/                      enunciado del profesor y material crudo (transcripciones, etc.)
```

## Pipeline técnico

Entorno verificado: Python 3.13.5, Git 2.49.0.windows.1. Playwright está instalado bajo **`py -3.14`**, no bajo el `python` del PATH: los scripts de captura y de PDF se corren con `py -3.14`.

**Diff multiarchivo como evidencia:**
```bash
cd entregables
git diff --no-index --no-color _snapshot_antes ../<proyecto> > diff_multiarchivo.txt
```
Borra `__pycache__/` antes o el diff se llena de `.pyc` binarios. Normaliza después las rutas `_snapshot_antes/` y `../<proyecto>/` a una sola ruta para que se lea como un `git diff` normal.

**Capturas de terminal:** genera un HTML que imite PowerShell (fondo oscuro, monoespaciada, coloreando `ok`/`OK` en verde y `ERROR`/`FAILED` en rojo) y captúralo con Playwright. Cuidado con la codificación: las salidas de consola de Windows llegan con acentos rotos (`Opci?n`, `inv?lida`) y hay que corregirlas antes de capturar.

**Informe a PDF:** lo hace la skill `informe-utp`. Dato heredado: Chromium no ejecuta JavaScript dentro de `footer_template`, así que el número de la portada se tapa después con PyMuPDF dibujando un rectángulo blanco sobre esa zona de la página 1.

**Verificación del PDF:** `Read` no renderiza PDF en este equipo (falta poppler). Rasteriza las páginas a PNG con PyMuPDF y léelas. Revisa siempre portada, índice paginado, y que las figuras altas no queden deformadas ni ilegibles.

## Cómo trabajar

- Lee el enunciado en `tmp/` completo antes de empezar; su última página tiene la lista de entregables y es la que manda.
- Las evidencias se generan ejecutando de verdad, no se redactan de memoria: si el informe dice "6 pruebas OK", tiene que existir el `.txt` y la captura que lo demuestren.
- Verifica lo que produzcan los subagentes antes de darlo por bueno, sobre todo cifras y afirmaciones sobre el código.
- Al cerrar: todas las pruebas pasan, el programa inicia sin errores, no queda código temporal de diagnóstico, y el commit lo hace el estudiante.

## Redacción

Todo texto entregable pasa por la skill `redaccion-humana`. Matices propios de esta materia:

- Primera persona del plural ("corrimos las pruebas", "rechazamos el cambio"), no pasiva refleja en cadena.
- No abrir cada sección con la misma fórmula tipo "Siguiendo el paso N, se…": menciona el paso del enunciado donde haga falta y con formas distintas.
- Los informes de laboratorio deben dejar rastro humano real de la sesión: una duda, algo que no salió a la primera, una decisión tomada por tiempo. Solo lo que de verdad pasó; nada inventado.
- Las conclusiones reportan lo que salió, incluso lo que costó o quedó a medias.

## Reglas del profesor descubiertas

Aquí se agrega, con fecha y trabajo de origen, toda regla nueva que aparezca en los enunciados o en clase y que no esté arriba.

- **Asignaciones sin referencias ni citas APA** (pedido de Gerald, Asig5, 05/10/2026). Los datos se mencionan de forma natural ("un informe del MIT", "según Fortune"), sin paréntesis de autor-año ni lista de referencias. Las fuentes igual se verifican y quedan en `tmp/fuentes.md`.
- **Las asignaciones sí llevan Conclusiones al final** (pedido de Gerald, Asig5): dos párrafos cortos que digan qué salió de las respuestas, sin repetirlas. Esto reemplaza el "No" de la tabla de arriba.
- Las preguntas sobre "su empresa" usan **Hypernovalabs, S.A.**, donde trabaja Gerald (equipo iaBoyz: TaaS, AaaS, SaaS; skills y agentes internos; cuenta organizacional de Claude con reglas, p. ej. no poner credenciales en el prompt). Solo afirmar sobre la empresa lo que Gerald haya dicho.
