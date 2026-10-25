# Cerebrolo

Montaje de Claude Code que usamos para organizar los trabajos del último semestre de la Lic. en Desarrollo y Gestión de Software (UTP, FISC, II semestre 2026). Una sesión principal (el «cerebro») recibe cada enunciado, decide qué es, lo reparte entre subagentes por materia y revisa lo que devuelven antes de darlo por bueno.

El repo trae las reglas, los agentes, las skills, las herramientas y, como ejemplo, el trabajo de **Sistemas de Información Gerencial** (Prof. Ivan Clarence) ya hecho: los 7 laboratorios, 3 investigaciones y 3 cuestionarios.

> Los trabajos de ejemplo son de Gerald Ríos. Sirven para ver el formato y el nivel de detalle que pide el profe, no para entregarlos copiados.

## Qué hay

```
CLAUDE.md                      reglas generales: tipos de trabajo, formato, reglas que no se negocian
ENTREGAS.md                    registro de entregas (ejemplo con SIG)
.claude/
  agents/                      un agente por materia (corren en Sonnet)
  skills/                      nuevo-trabajo, informe-utp, redaccion-humana, investigacion-apa, diagramas
0N-Materia/CLAUDE.md           reglas de cada materia
03-Sistemas-Informacion-Gerencial/
  _curso/LABS_BRIEF.md         reglas comunes de los labs de Clarence (paso a paso, evidencia real)
  _curso/TEORIA_BRIEF.md       reglas de las investigaciones y cuestionarios (fuentes, formato)
  _curso/plantilla/build_lab.py   spec.json → .docx + .pdf con la plantilla del profe
  _curso/herramientas/captura.ps1 captura de ventanas de escritorio (DIA, Excel) para las evidencias
  Lab01 … Lab07/entregables/   PDF, DOCX, spec.json y evidencias de cada lab
  Inv01 … Inv03/entregables/   investigaciones (la #2 es la original de Gerald, calificada 10/10)
  Cuest01 … Cuest03/entregables/  cuestionarios de los capítulos I, II y III
```

| Lab | Tema | Herramienta |
|---|---|---|
| 1 | Ludificación | purposegames.com |
| 2 | Checksum SHA-256 | defuse.ca, Bloc de notas, PowerShell |
| 3 | Equivalencia decimal y ASCII | Excel |
| 4 | Oracle APEX (taller SQL) | oracleapex.com (SQL Scripts y SQL Commands) |
| 5 | Power Query | Excel |
| 6 | Modelado de la organización (UML) | DIA |
| 7 | Modelaje de datos (E-R de Northwind) | DIA |

| Trabajo | Tema | Base |
|---|---|---|
| Investigación 1 | Datos, información y conocimiento (y qué los une) | Material 1.2 + fuentes verificadas |
| Investigación 2 | Señales digitales y analógicas | Hecha por Gerald (10/10), sirve de modelo de formato |
| Investigación 3 | Técnicas de análisis y modelado de datos | Material 3.2–3.4 + IBM, Microsoft, Rueda et al. (2020) |
| Cuestionario 1 | Cap. I, 18 preguntas | Presentaciones del capítulo I |
| Cuestionario 2 | Cap. II, 24 preguntas | Presentaciones del capítulo II |
| Cuestionario 3 | Cap. III, 30 preguntas | Presentaciones del capítulo III |

Los cuestionarios se responden con las presentaciones del profe porque él pregunta lo que dio en clase. Las investigaciones y los cuestionarios 2 y 3 se entregan por correo: en Moodle las investigaciones 1 y 3 ya cerraron y los cuestionarios 2 y 3 no tienen preguntas cargadas.

En el Lab 4, cada captura de APEX muestra el pie con el usuario y el workspace (constancia de que es tu cuenta). Cada quien hace el lab en su propio workspace.

## Lo que no viene (y dónde conseguirlo)

El material del profesor no se publica: enunciados, presentaciones, `Northwind.xlsx` y la plantilla `PlantillaPresentaciones.docx`. Todo está en Virtual-UTP, en el curso de SIG, carpeta **Documentos → Laboratorios**. Pon cada enunciado en `LabNN-*/tmp/` y la plantilla en `03-Sistemas-Informacion-Gerencial/_curso/plantilla/`.

## Cómo usarlo

1. Clona el repo y ábrelo con Claude Code desde la raíz.
2. Cambia tus datos:
   - `CLAUDE.md` (tabla «Estudiante») y el `CLAUDE.md` de cada materia.
   - En cada `spec.json`, agrega `"integrantes": ["Apellido, Nombre (cédula)"]`; si no lo pones, `build_lab.py` usa el valor de `INTEGRANTE`.
   - `"tipo"` cambia el rótulo de la portada (`"INVESTIGACIÓN"`, `"CUESTIONARIO"`; por defecto `"LABORATORIO"`) y `"conclusion": []` omite esa sección.
3. Pásale el enunciado al cerebro («tengo que entregar…»); la skill `nuevo-trabajo` crea la carpeta, lo registra y reparte.
4. Para generar un lab de SIG a mano:

   ```
   py -3.13 03-Sistemas-Informacion-Gerencial\_curso\plantilla\build_lab.py LabNN-tema\entregables\spec.json
   ```

## Requisitos (Windows)

- Microsoft Word y Excel (el generador exporta el PDF con Word por COM).
- Python 3.13 con `python-docx`, `pywin32` y `pymupdf`.
- DIA 0.97.2 para los labs 6 y 7: http://dia-installer.de
- Node.js si se usan diagramas Mermaid (skill `diagramas`).

## Reglas que más pesan

- **No se inventa nada**: fuentes, datos, resultados ni capturas. Lo que no se sabe se marca `[PENDIENTE: …]`.
- **La evidencia se genera, no se redacta**: si el informe dice que algo corrió, existe la captura que lo prueba. Nada de imágenes de relleno.
- Si una parte se automatizó (por script o COM) en vez de hacerse con clics, el informe lo dice.
- Todo texto entregable pasa por la skill `redaccion-humana`.
