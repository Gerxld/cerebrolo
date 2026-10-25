---
name: informe-utp
description: Produce informes en PDF con el formato institucional de la UTP/FISC (portada con logos, índice, secciones numeradas, Times 12, Carta, número de página salvo en portada) a partir de una plantilla HTML, y verifica el PDF página por página. Úsala para cualquier entregable en PDF de las materias de Cerebrolo — laboratorio, asignación, investigación, caso o proyecto.
---

# Informe UTP

Archivos de la skill (ruta base `C:\Cerebrolo\.claude\skills\informe-utp\`):

- `template.html` — portada, índice, estilos de tablas, figuras y referencias APA.
- `assets/utp.png`, `assets/fisc.png` — logos de la plantilla oficial.
- `scripts/informe_a_pdf.py` — HTML → PDF (Carta, márgenes 2.5 cm, número en el pie) y tapa el número de la portada.
- `scripts/verificar_pdf.py` — rasteriza páginas a PNG e imprime la primera línea de cada una.

## Pasos

1. **Preparar** dentro de `<trabajo>/entregables/`:
   ```powershell
   $s = 'C:\Cerebrolo\.claude\skills\informe-utp'
   New-Item -ItemType Directory -Force informe, assets | Out-Null
   Copy-Item "$s\assets\*" assets\
   Copy-Item "$s\template.html" informe\informe.html
   ```
2. **Llenar la portada** con los datos del `CLAUDE.md` de la materia: asignatura, título exacto del enunciado, grupo, profesor (como lo pida la materia, p. ej. "Profesor Regis Rivera"), integrantes en orden alfabético, fecha `DD / MM / AAAA`. Si un dato falta, no lo inventes: pregunta.
3. **Ajustar la estructura al tipo de trabajo** (tabla en el `CLAUDE.md` raíz):
   - Asignación: borra el bloque `.indice`, la introducción y las conclusiones. Cada pregunta como `<h2>` con su número y enunciado, y debajo la respuesta.
   - Laboratorio / investigación / proyecto: deja índice, introducción, secciones numeradas, conclusiones y referencias.
4. **Contenido.** Tablas con título arriba ("Tabla 1. …") y figuras con `<figcaption>` ("Figura 1. …"), estilo APA. A las figuras se las nombra por su número, sin decir en qué sección están. Nada de líneas bajo los títulos.
5. **Generar el PDF:**
   ```powershell
   py -3.14 "$s\scripts\informe_a_pdf.py" informe\informe.html <Nombre>.pdf
   ```
6. **Verificar:**
   ```powershell
   py -3.14 "$s\scripts\verificar_pdf.py" <Nombre>.pdf
   ```
   Lee con Read al menos la portada, el índice y cada página con figura o tabla grande. Comprueba:
   - La portada no tiene número y los logos se ven.
   - Los números del índice coinciden con la paginación real (la salida del script muestra la primera línea de cada página). Si no coinciden, corrige el HTML y regenera.
   - No hay títulos huérfanos al final de una página ni tablas cortadas feo.
   - Las figuras altas no salen deformadas ni ilegibles.
7. Borra `_preview/` al terminar; no se entrega.

## Si el profesor pide Word

Usa la skill `docx` respetando el mismo formato (Times 12, 1.5, márgenes 2.5 cm, misma portada con los logos de `assets/`).
