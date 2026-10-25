---
name: diagramas
description: Crea diagramas para trabajos universitarios en Mermaid y los renderiza a PNG listos para el informe — EDT/WBS, Gantt, diagramas de red, DFD, entidad-relación, casos de uso, flujos de proceso BPMN simplificados, organigramas, mapas conceptuales, matrices. Úsala cuando un enunciado pida un diagrama o cuando una figura explique mejor que un párrafo.
---

# Diagramas

Fuente en `.mmd`, imagen en `.png`, ambos en `<trabajo>/entregables/diagramas/`. El `.mmd` se guarda siempre: es lo que permite corregir después.

## Renderizar

```powershell
py -3.14 C:\Cerebrolo\.claude\skills\diagramas\scripts\mermaid_a_png.py entregables\diagramas
```

Usa Playwright y Mermaid 11 desde CDN (requiere internet). Después **mira el PNG con Read**: textos cortados, cajas encimadas o un diagrama demasiado ancho para una página Carta se corrigen en el `.mmd` (abreviar etiquetas, cambiar `LR` por `TB`, partir en dos figuras).

## Qué tipo de Mermaid para cada cosa

| Necesidad | Mermaid | Notas |
|---|---|---|
| EDT / WBS | `flowchart TB` | Códigos en cada nodo: `1.1 Análisis`. Paquetes de trabajo como sustantivos, no verbos |
| Cronograma | `gantt` | `dateFormat YYYY-MM-DD`, secciones por fase, hitos con `milestone` |
| Red / ruta crítica | `flowchart LR` | Ruta crítica con `classDef critica stroke:#000,stroke-width:3px` |
| DFD | `flowchart LR` | Entidades externas `[ ]`, procesos `(( ))`, almacenes `[( )]`, flujos etiquetados |
| Entidad-relación | `erDiagram` | Atributos con tipo; PK/FK marcadas |
| Casos de uso | `flowchart LR` | Mermaid no tiene casos de uso nativos: actores como nodos, casos `([ ])`, sistema en `subgraph` |
| Proceso de negocio | `flowchart TB` con `subgraph` por área | Simula carriles (swimlanes) |
| Organigrama | `flowchart TB` | Un nivel jerárquico por fila |
| Mapa conceptual | `flowchart TB` o `mindmap` | Conectores con verbo en la flecha |
| Clases | `classDiagram` | |
| Secuencia | `sequenceDiagram` | |

## Estilo

- Tema `neutral` en blanco y negro con grises: se imprime bien y se ve académico. Nada de colores chillones.
- Etiquetas en español, cortas. Sin emojis.
- En el informe: `<figure><img src="../diagramas/x.png"><figcaption>Figura N. Descripción. Elaboración propia.</figcaption></figure>`. Si el diagrama se basa en una fuente: "Adaptado de Autor (Año)".

## Cuando Mermaid no alcanza

Matrices (RACI, riesgos probabilidad × impacto, FODA, BCG) se hacen como **tabla HTML** en el informe, no como diagrama. Para un Gantt que el profesor pida en MS Project o Excel, usa la skill `xlsx` y avísale a Gerald que esa herramienta específica la tiene que abrir él.
