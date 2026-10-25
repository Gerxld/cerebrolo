---
name: nuevo-trabajo
description: Recibe un trabajo universitario nuevo (laboratorio, asignación, investigación, presentación, caso, proyecto) y lo monta en Cerebrolo — ubica la materia, lee el enunciado, clasifica, crea la carpeta, lo registra en ENTREGAS.md y planifica el reparto entre subagentes. Úsala cada vez que Gerald pase un enunciado, un PDF del profesor o diga "tengo que entregar…".
---

# Nuevo trabajo

## 1. Ubicar la materia

Identifica la materia por el enunciado (nombre de la asignatura, profesor, código de grupo) o por lo que diga Gerald. Si hay duda entre dos, pregunta. Lee el `CLAUDE.md` de esa materia completo antes de seguir.

## 2. Leer el enunciado entero

- PDF: usa la skill `pdf` o PyMuPDF (`py -3.14`). Word: la skill `docx`. Imagen: léela directamente.
- Anota: título exacto, fecha y hora de entrega, si es individual o grupal, extensión pedida, formato de salida (PDF, Word, pptx, plataforma), rúbrica si viene.
- La lista de entregables manda. Si el enunciado contradice al `CLAUDE.md` de la materia, gana el enunciado; anota la diferencia en el `CLAUDE.md` de la materia si parece una regla fija del profesor.

## 3. Clasificar

| Si el enunciado… | Tipo | Prefijo de carpeta |
|---|---|---|
| pide realizar un proceso y documentarlo con evidencias | Laboratorio | `Lab` |
| hace preguntas concretas a responder | Asignación | `Asig` |
| pide investigar un tema con fuentes | Investigación | `Inv` |
| pide exponer o diapositivas | Presentación | `Pres` |
| plantea una empresa o situación a analizar | Caso de estudio | `Caso` |
| es el proyecto de la materia o una fase de él | Proyecto | `Proy` |
| es taller o parcial para resolver | Taller | `Taller` |

Un trabajo puede combinar tipos (investigación + presentación). Crea una sola carpeta y lista todos los entregables.

## 4. Crear la carpeta

```
NN-Materia/<Prefijo><NN>-<tema-corto>/
  tmp/            enunciado original (copia, no se edita)
  entregables/
```

Numera con dos dígitos según los existentes de ese tipo en la materia (`Lab01`, `Lab02`…). Tema corto en kebab-case sin tildes.

## 5. Registrar

Agrega la fila en `C:\Cerebrolo\ENTREGAS.md` con estado `en curso` y la fecha en `DD/MM/AAAA`.

## 6. Datos que faltan

Antes de producir, confirma lo que no puedes deducir y que cambia el resultado: integrantes del grupo y cédulas (si no están en el `CLAUDE.md` de la materia), profesor, grupo, tema elegido cuando el enunciado deja escoger. Pregunta todo junto, una sola vez.

## 7. Planificar y repartir

Escribe un plan corto: entregables → quién los hace → en qué orden. Reglas:

- Divide por entregable (investigación de fuentes / diagramas / redacción / presentación), no por paso.
- Delega en el agente de la materia (Sonnet). En el encargo incluye: ruta de la carpeta, tipo de trabajo, extracto de las reglas aplicables del `CLAUDE.md` de la materia, hechos ya verificados y la **lista cerrada de archivos que puede escribir**.
- Lo que no depende de nada corre en paralelo. Solo un agente a la vez con navegador.
- Fuentes primero, redacción después: el texto se escribe sobre fuentes ya verificadas (skill `investigacion-apa`).

## 8. Verificar y cerrar

- Revisa cifras, citas y afirmaciones de lo que devuelvan los agentes.
- Pasa el texto por `redaccion-humana`.
- Genera y revisa el PDF con `informe-utp` (portada, índice contra paginación real, figuras legibles).
- Cumple cada punto de la lista de entregables, uno por uno.
- Actualiza `ENTREGAS.md` a `listo para revisar` y dile a Gerald qué le queda a él.
