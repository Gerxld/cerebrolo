# CLAUDE.md — Gerencia de Recursos Tecnológicos e Informáticos

Reglas específicas de esta materia. Lo general (formato UTP, tipos de trabajo, estructura de carpetas, reglas que no se negocian) está en `C:\Cerebrolo\CLAUDE.md` y no se repite aquí. Si algo choca, manda este archivo; sobre ambos manda el enunciado del profesor.

## Identidad de las entregas

| Campo | Valor |
|---|---|
| Asignatura | Gerencia de Recursos Tecnológicos e Informáticos (teoría + laboratorio) |
| Grupo | `[PENDIENTE: confirmar]` |
| Profesor | `[PENDIENTE]` |
| Teoría | Lunes 7:30–9:55 p.m., aula 3-306 · Viernes 7:30–8:15 p.m., aula 3-306 |
| Laboratorio | Viernes 8:20–9:05 p.m., aula 3-306 |
| Estudiante | Ríos, Gerald (8-987-741) |
| Integrantes de grupo | `[PENDIENTE]` |

No inventes compañeros, apellidos ni cédulas. Mientras no estén confirmados, la portada lleva `[PENDIENTE]` en esos campos y se avisa a Gerald. El porcentaje de aporte no se pone salvo que el profesor lo pida.

## Teoría vs. laboratorio

Todo esto es **por defecto, por confirmar contra el sílabo** y el primer enunciado real.

| | Teoría (lunes y viernes) | Laboratorio (viernes) |
|---|---|---|
| Qué se espera | Asignaciones, investigaciones, casos de estudio, parciales, presentaciones | Aplicación práctica: elaborar un artefacto de gestión de TI sobre una organización o caso dado |
| Salida típica | Cuestionario o ensayo en PDF; `.pptx` si hay exposición | Informe PDF con el artefacto (inventario, TCO, matriz, política) más su hoja de cálculo |
| Formato | Asignación = portada + respuestas; investigación e informe = formato completo | Informe de laboratorio completo (portada, índice, introducción, conclusiones) |

Si un entregable de laboratorio incluye una hoja de cálculo, se entrega el `.xlsx` junto al PDF, salvo que el enunciado diga otra cosa.

## Marco de referencia

Base conceptual para redactar y revisar. Si un dato se va a citar, se verifica con la skill `investigacion-apa`; lo de aquí orienta, no sustituye la fuente.

**Gobierno vs. gestión de TI.** El gobierno evalúa, dirige y monitorea: la junta directiva y la alta gerencia fijan objetivos, prioridades y apetito de riesgo. La gestión planifica, construye, ejecuta y controla las actividades para alcanzar esos objetivos. COBIT 2019 los separa explícitamente.

**COBIT 2019 (ISACA).** Marco de gobierno y gestión de TI empresarial. Organiza sus objetivos de gobierno y gestión en cinco dominios:
- EDM (Evaluar, Dirigir y Monitorear): el único dominio de gobierno.
- APO (Alinear, Planificar y Organizar), BAI (Construir, Adquirir e Implementar), DSS (Entregar, Dar Servicio y Soporte) y MEA (Monitorear, Evaluar y Valorar): dominios de gestión.
- Usa factores de diseño para adaptar el sistema de gobierno a la empresa y niveles de capacidad para medir procesos. Citar un objetivo concreto (por ejemplo APO12, gestión del riesgo) solo tras verificarlo en la publicación.

**ITIL 4 (AXELOS/PeopleCert).** Gestión de servicios de TI.
- Sistema de valor del servicio (SVS): oportunidad/demanda, principios rectores, gobierno, cadena de valor del servicio, mejora continua y prácticas, que producen valor.
- Cadena de valor del servicio: planificar, mejorar, involucrar, diseño y transición, obtener/construir, entregar y soporte.
- Prácticas clave para esta materia: gestión de incidentes, de problemas, de cambios (habilitación de cambios), de niveles de servicio, de activos de TI, de configuración, mesa de servicio, gestión de proveedores.

**ISO/IEC 27001 (SGSI).** Requisitos de un sistema de gestión de seguridad de la información: contexto, liderazgo, evaluación y tratamiento de riesgos, controles (Anexo A), auditoría y mejora. Edición vigente: 2022.

**ISO/IEC 20000.** Requisitos de un sistema de gestión de servicios (SMS); es la norma certificable que se alinea con las prácticas de ITIL.

**Conceptos transversales.**
- Alineación estratégica TI-negocio: cada iniciativa de TI se amarra a un objetivo del negocio; si no se puede, se cuestiona.
- Gestión de activos y ciclo de vida: adquisición, operación (mantenimiento, soporte), renovación, disposición (baja, reciclaje de RAEE, borrado seguro de datos).
- TCO (costo total de propiedad): adquisición más operación, soporte, licencias, capacitación, energía y disposición durante el ciclo de vida. ROI: (beneficio - costo) / costo, con el período y los supuestos explícitos.
- Proveedores: criterios de selección, SLA, contratos y licenciamiento (perpetua, suscripción, por usuario, por dispositivo, OEM, de código abierto); cuidar vigencia, penalizaciones y salida del contrato.
- Continuidad: BCP (continuidad del negocio) y DRP (recuperación ante desastres); RTO es el tiempo máximo tolerable para restablecer el servicio y RPO la máxima pérdida de datos tolerable medida en tiempo. Se derivan de un análisis de impacto al negocio (BIA).
- Talento humano en TI: perfiles y roles, brechas de competencias, capacitación, rotación, tercerización.

## Catálogo de entregables típicos

| Entregable | Cómo hacerlo bien | Skill |
|---|---|---|
| Plan estratégico de TI | Situación actual, FODA de TI (con evidencia, no frases genéricas), objetivos medibles alineados al negocio, iniciativas, cartera priorizada con criterio explícito, presupuesto y cronograma | `informe-utp` + `diagramas` (Gantt, mapa de alineación) |
| Inventario de activos | Columnas: ID/etiqueta, tipo, descripción, marca/modelo, serie, ubicación, responsable, estado, fecha de adquisición, proveedor, costo, garantía hasta, vida útil, criticidad, observaciones. Si el inventario es ficticio o de un caso, decirlo | `xlsx` + tabla resumen en `informe-utp` |
| TCO / comparativa de proveedores | Desglose por rubro (adquisición, licencias, implementación, soporte, capacitación, operación, disposición) y horizonte (3 o 5 años). **Cada precio con fuente, URL y fecha de consulta. Nunca precios inventados**; si no hay cotización, `[PENDIENTE: cotizar]` o supuesto marcado como tal. Matriz de criterios ponderados con pesos justificados | `xlsx` (fórmulas vivas) + `informe-utp` |
| Propuesta de SLA | Servicio cubierto, horario, disponibilidad (%), tiempos de respuesta y resolución por prioridad, RTO/RPO, métricas y cómo se miden, exclusiones, penalizaciones o créditos, reportes, revisión periódica | `informe-utp` (tablas) |
| Matriz de riesgos de TI | Riesgo, causa, consecuencia, activo afectado, probabilidad, impacto, nivel (escala declarada), control existente, tratamiento, responsable, riesgo residual. Mapa de calor opcional | `xlsx` + `informe-utp` |
| Plan de continuidad | Alcance, BIA, procesos críticos, RTO/RPO, escenarios, estrategias de recuperación, roles y contactos, procedimientos, pruebas y mantenimiento del plan | `informe-utp` + `diagramas` (flujos) |
| Política de TI | Propósito, alcance, roles, lineamientos (uso aceptable, accesos, respaldos, software autorizado, etc.), cumplimiento y sanciones, vigencia y revisión. Redactada como norma, no como ensayo | `informe-utp` |
| Diagnóstico de madurez | Modelo declarado (por ejemplo niveles de capacidad de COBIT) y criterios por nivel, evaluación por proceso con evidencia, brecha frente al nivel objetivo, plan de cierre de brechas | `xlsx` + `informe-utp` (gráfico de brechas) |

Reglas para todos:
- Los datos de la organización estudiada vienen del enunciado o de Gerald. Lo que falte se pregunta o se marca `[PENDIENTE: …]`.
- Las cifras de la hoja de cálculo y las del informe deben coincidir; el cerebro las recalcula al verificar.
- Si se cita un marco o norma, con la edición y el año que realmente se usó.

## Bibliografía y fuentes base

Marcar todo como **verificar contra el sílabo**: el profesor puede exigir otros textos.

- ISACA. (2018). *COBIT 2019 Framework: Introduction and Methodology* y *Governance and Management Objectives*. ISACA.
- AXELOS / PeopleCert. (2019). *ITIL Foundation: ITIL 4 Edition*. TSO.
- ISO/IEC. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements*.
- ISO/IEC. *ISO/IEC 20000-1* (verificar la edición vigente antes de citar).

Los datos exactos (autor corporativo, año, editorial, URL) se confirman con `investigacion-apa` antes de que entren a una lista de referencias. No se añade ningún libro de texto que no se haya comprobado que existe.

## Reglas del profesor descubiertas

(Vacío. Se llena con lo que Gerald o los enunciados vayan revelando: preferencias de formato, penalizaciones, énfasis de evaluación, política de grupos y de entrega.)

## Formato específico

`[PENDIENTE]`. Mientras tanto se hereda el formato institucional de la raíz (skill `informe-utp`).
