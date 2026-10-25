# CLAUDE.md — Sistemas de Información Gerencial

Reglas de la materia. Hereda todo lo del `CLAUDE.md` raíz (formato institucional, tipos de trabajo, reglas que no se negocian, estructura de carpetas, skills). Aquí va solo lo específico de SIG. Si algo choca, manda este archivo; por encima manda el enunciado del profesor.

## Identidad de las entregas

| Campo | Valor |
|---|---|
| Universidad | Universidad Tecnológica de Panamá |
| Facultad | Facultad de Ingeniería de Sistemas Computacionales |
| Carrera | Lic. en Desarrollo y Gestión de Software |
| Asignatura | Sistemas de Información Gerencial |
| Grupo | 1GS241 (curso Moodle 7709, código 1494) |
| Profesor | Ivan Clarence |
| Teoría | Jueves 5:50–8:15 p.m., aula 3-306 |
| Laboratorio | Martes 8:20–9:55 p.m., aula 3-411 |
| Estudiante | Ríos, Gerald (8-987-741) |
| Integrantes de grupo | `[PENDIENTE]` |

En trabajos grupales, `Apellido, Nombre (cédula)` en orden alfabético por apellido. No se inventan compañeros, cédulas ni variantes de apellido: si falta un dato, se pregunta.

## Teoría vs. laboratorio (por defecto; confirmar con el sílabo)

| | Teoría | Laboratorio |
|---|---|---|
| Qué se espera | Conceptos, casos y análisis escrito | Práctica con herramientas y evidencia |
| Entregables probables | Asignaciones, análisis de caso, investigaciones, presentaciones, parciales | Informe con capturas: dashboards en Excel o Power BI, consultas SQL, modelado de procesos, demos de ERP/CRM |
| Tipo (según raíz) | Asignación, caso de estudio, investigación, presentación | Laboratorio |

Nada de esto está confirmado. Cuando llegue el sílabo a `_curso/`, se corrige esta tabla. Mientras tanto, el tipo de cada trabajo lo decide el enunciado.

En laboratorio la regla de la raíz pesa más: si el informe dice que una consulta o un dashboard funciona, existe la captura o la salida que lo prueba. Los archivos de trabajo (`.xlsx`, `.pbix`, `.sql`) se guardan junto al informe.

## Marco conceptual de referencia

Es base para que el agente no se equivoque en definiciones. No se copia a los entregables: se usa para analizar, y lo que se cite se respalda con la bibliografía.

- **Dato, información, conocimiento.** Dato: hecho en bruto sin contexto. Información: datos procesados con significado para quien decide. Conocimiento: información interpretada y aplicada a la experiencia.
- **Componentes de un SI.** Personas, procesos, datos, hardware, software y redes. Funciones: entrada, procesamiento, salida, retroalimentación y control.
- **Tipos de SI por nivel.**
  - TPS: procesa transacciones operativas (ventas, planilla, inventario).
  - MIS: resume datos de los TPS en informes periódicos para la gerencia media.
  - DSS: apoya decisiones semiestructuradas con modelos y análisis.
  - ESS/EIS: indicadores de alto nivel para la gerencia estratégica.
  - KMS: captura, almacena y comparte conocimiento de la organización.
- **Sistemas empresariales.** ERP (integra los procesos de toda la empresa en una base de datos común), CRM (relación con el cliente), SCM (cadena de suministro).
- **Procesos de negocio.** Conjunto de actividades coordinadas que producen un resultado para un cliente. Se modelan, se miden y se rediseñan (BPM, reingeniería).
- **Ventaja competitiva (Porter).** Cinco fuerzas: rivalidad entre competidores, amenaza de nuevos entrantes, de sustitutos, poder de proveedores y poder de clientes. Cadena de valor: actividades primarias (logística de entrada, operaciones, logística de salida, marketing y ventas, servicio) y de apoyo (infraestructura, recursos humanos, tecnología, abastecimiento). Un SI da ventaja si reduce costos, diferencia el producto, o ata al cliente o al proveedor.
- **BI, data warehouse, KPI.** BI: herramientas y prácticas para convertir datos en decisiones. Data warehouse: repositorio histórico e integrado, orientado a análisis (proceso ETL: extraer, transformar, cargar). KPI: indicador clave ligado a un objetivo del negocio.
- **Ética, seguridad y aspectos legales.** Privacidad, propiedad intelectual, exactitud y acceso a la información; confidencialidad, integridad y disponibilidad. En Panamá aplica la Ley 81 de 2019 sobre protección de datos personales (con su reglamentación por decreto ejecutivo). `[VERIFICAR: número y fecha del decreto reglamentario antes de citarlo; citar la Gaceta Oficial como fuente]`.

## Catálogo de entregables típicos

### Análisis de caso empresarial
Estructura: **Contexto** (empresa, sector, situación) → **Problema** (una frase concreta, no un tema) → **SI involucrados** (qué sistemas usa o le faltan, a qué nivel operan) → **Análisis** (causas, impacto en procesos, aplicación de un marco como Porter o cadena de valor) → **Recomendaciones** (accionables, priorizadas, con costo o riesgo aproximado). Las recomendaciones responden al problema planteado, no a cualquier mejora posible.

### Cuadro comparativo
Criterios definidos antes de llenar la tabla y los mismos para todos los elementos. Cada celda con contenido real, no «sí/no» sueltos. Cierra con una frase de qué opción conviene y para quién.

### Diagramas
Skill `diagramas` (Mermaid a PNG). DFD (niveles 0 y 1, con entidades externas, procesos, almacenes y flujos rotulados; el balanceo entre niveles debe cuadrar), ER (entidades, atributos clave, cardinalidades) y procesos (inicio y fin claros, decisiones con salidas rotuladas). Cada diagrama lleva número y título, y el texto lo introduce brevemente.

### Propuesta de SI para una empresa
Diagnóstico breve → objetivos medibles → requerimientos funcionales y no funcionales → solución propuesta (tipo de SI, módulos, quién lo usa) → arquitectura o diagrama → plan de implantación y capacitación → costo-beneficio y riesgos. Si hay cifras de costos, se marcan como estimado y con su base.

### Dashboard y KPI
Cada KPI se define en una tabla con: **nombre, objetivo de negocio que mide, fórmula, fuente de datos, frecuencia de actualización, meta y responsable**. Pocos KPI y bien definidos valen más que muchos. Skill `dataviz` para elegir el gráfico (barras para comparar, líneas para tendencia; sin gráficos de pastel con muchas categorías). Títulos que digan qué muestra el gráfico, ejes rotulados, colores consistentes.

### Informe de laboratorio con capturas
Formato de laboratorio de la raíz. Cada paso lleva su captura y se ve la herramienta, la versión y los datos usados (la captura debe mostrar la ventana, no un recorte sin contexto). Las consultas SQL y las fórmulas van como texto, además de la captura. Si algo falló y se corrigió, se cuenta.

## Casos sobre empresas reales

Cuando el caso trate de una empresa real (de Panamá, cuando sea posible): solo hechos verificados y con fuente (informe anual, sitio oficial, prensa reconocida, Gaceta Oficial), citados en APA con la skill `investigacion-apa`. No se inventan cifras, cargos, sistemas que «usa» la empresa ni declaraciones. Lo que no se pueda verificar se presenta como supuesto del análisis, rotulado como tal, o se omite.

## Bibliografía base

Obras conocidas de la materia. Las ediciones y años exactos se verifican contra el sílabo antes de citar: `[verificar edición contra el sílabo]`.

- Laudon, K. C. y Laudon, J. P. *Sistemas de información gerencial*. Pearson. `[verificar edición contra el sílabo]`
- O'Brien, J. A. y Marakas, G. M. *Sistemas de información gerencial*. McGraw-Hill. `[verificar edición contra el sílabo]`

Para cualquier otra fuente, skill `investigacion-apa`: se busca, se verifica y recién entonces se cita.

## Reglas del profesor descubiertas

- **Paso a paso detallado** en los laboratorios: cada paso con su captura, su pie de figura y el desarrollo (Gerald, 24/10/2026).
- **Plantilla del profesor** para documentar (`_curso/plantilla/PlantillaPresentaciones.docx`; el Lab 1 la pide de forma explícita): portada → INDICE → CONTENIDO → CONCLUSION → REFERENCIA. La plantilla trae «Técnico en Informática / Sistemas de Información Empresarial» porque el profe la reutiliza de otro curso; se corrige a la carrera y asignatura de Gerald (24/10/2026).
- Fecha de portada en formato `AAAA.MM.DD`, como en la plantilla.
- Los enunciados y el material de cada lab están en la carpeta «Documentos / Laboratorios» del Moodle y adjuntos en cada tarea.
- Moodle cierra la tarea en la fecha de cierre: después ya no aparece «Agregar entrega».
- **Oracle APEX:** en cada captura tiene que verse el pie inferior izquierdo de APEX con el usuario (`gerald.rios@utp.ac.pa`), el workspace (`shzzzz`) y el idioma. Es la constancia de que el trabajo es de su workspace (Gerald, 25/10/2026).

## Formato específico

Laboratorios e investigaciones: **plantilla del profesor**, no `informe-utp`. Se generan con `_curso/plantilla/build_lab.py` (spec JSON → docx + pdf con Word). El brief común de los labs está en `_curso/LABS_BRIEF.md`.

## Cómo trabajar

- Lee el enunciado completo; la lista de entregables (casi siempre al final) manda.
- Revisa `_curso/` (sílabo, rúbricas) antes de empezar: ahí está lo que se evalúa.
- Todo texto entregable pasa por `redaccion-humana`. Las cifras y fuentes las verifica el cerebro antes de cerrar.
- No hacer commits ni push; eso lo maneja Gerald.
