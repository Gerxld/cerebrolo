# Brief común — Laboratorios de SIG (Prof. Ivan Clarence, 1GS241)

Lo leen todos los que produzcan un laboratorio de esta materia (sesión Ayudas, subagentes Sonnet). El cerebro (sesión REMONTADA) revisa todo antes de dárselo a Gerald.

## Lo que pide el profesor

- **Paso a paso detallado.** A Clarence le gusta ver cada paso: qué se hizo, dónde se hizo clic, qué se escribió y qué salió. Cada paso lleva una captura real (de la ventana completa o con contexto suficiente) y su pie de figura.
- **Plantilla del profesor** (`_curso/plantilla/PlantillaPresentaciones.docx`): portada → INDICE → CONTENIDO (objetivo + pasos) → CONCLUSION → REFERENCIA. No se arma a mano: se usa el generador.
- Modelo de cómo le gusta: `Lab03-decimal-ascii/entregables/version-gerald/Lab3_Paso_a_Paso_Gerald_Rios.pdf` (léelo antes de empezar). Ahí se ven el objetivo, los «Paso N: …», las figuras numeradas, el desarrollo de cada cálculo, una tabla resumen al final del contenido, la conclusión en 2 párrafos y las referencias APA.

## Generador

```
py -3.13 C:\Cerebrolo\03-Sistemas-Informacion-Gerencial\_curso\plantilla\build_lab.py <ruta>\spec.json
```

Produce `.docx` y `.pdf` (Word actualiza el índice). El formato del `spec.json` está documentado al inicio de `build_lab.py`. Campos fijos:

- `"lab"`: número · `"titulo"`: título del lab tal como lo escribe el profesor · `"fecha"`: `"2026.10.27"` · `"salida"`: `"Lab0N_SIG_Rios_Gerald"`, con la ruta relativa al spec.
- La portada (universidad, facultad, Lic. en Desarrollo y Gestión de Software, Sistemas de Información Gerencial, profesor, «Gerald Ríos, 8-987-741») la pone el generador.

Para revisar el PDF, renderiza las páginas a PNG con `py -3.14 -I` + `pymupdf` y míralas. El índice tiene que cuadrar con la paginación y ninguna figura puede quedar cortada ni ilegible.

## Estructura de carpeta (por lab)

```
LabNN-tema/
  tmp/                      enunciado del profesor (no se edita)
  entregables/
    spec.json               fuente del informe
    evidencias/             capturas PNG numeradas (01_..., 02_...) y archivos de trabajo
    Lab0N_SIG_Rios_Gerald.docx / .pdf
```

## Reglas que no se negocian

- **Evidencia real.** Toda captura sale de haber hecho el paso de verdad. No se inventan resultados, puntajes, hashes, salidas ni capturas. Si algo falló, se cuenta y se muestra cómo se corrigió.
- **Nada de imágenes de relleno.** Nunca se copia una imagen (por ejemplo, el PNG exportado) con nombre de captura, ni siquiera «para probar el generador». Si una captura falta, la figura no va. Antes de entregar, comprueba con SHA-256 que no haya dos evidencias iguales (24/10/2026: pasó en el Lab 6 y hubo que rehacerlo).
- **No crear cuentas ni escribir contraseñas.** Si un sitio exige registro o login, se detiene y se le avisa al cerebro.
- **No entregar en Moodle ni enviar nada.** El que sube es Gerald.
- **Referencias:** solo fuentes que existan y se hayan consultado. Material del curso: `Clarence, I. (2026). <título> [Material del curso]. Universidad Tecnológica de Panamá, Virtual-UTP.`. Las páginas web, con su URL.
- **Redacción:** español panameño neutro, tercera persona impersonal («se abrió», «se escribió»), como en el Lab 3. Nada de frases de relleno ni tono de IA. Antes de cerrar, aplica la skill `redaccion-humana` (`C:\Cerebrolo\.claude\skills\redaccion-humana\SKILL.md`).
- **Ownership:** cada quien escribe solo dentro de la carpeta de su lab. Si algo de `_curso/` hay que cambiar (por ejemplo, el generador), se le avisa al cerebro.
- **Navegador:** solo una sesión a la vez usa Chrome. Cuando termines, cierra tus pestañas y avisa.
- **Git:** nada de commits.

## Estado y reparto

| Lab | Tema | Quién | Notas |
|---|---|---|---|
| 1 | Ludificación (purposegames.com) | Ayudas | Navegador |
| 2 | Checksum SHA-256 (defuse.ca) | Ayudas | Navegador + archivo local |
| 3 | Decimal y ASCII | Cerebro | Ya hecho por Gerald; solo se corrige la portada |
| 4 | Oracle APEX | pendiente | Necesita que Gerald inicie sesión en su workspace |
| 5 | Power Query | subagente | Excel local + Northwind.xlsx |
| 6 | Modelado de la organización | subagente | DIA 0.97.2 instalado |
| 7 | Modelaje de datos | subagente | DIA; **prioridad: cierra el 27/10 a las 23:59** |

DIA: `C:\Program Files (x86)\Dia\bin\diaw.exe` (interfaz) y `dia.exe` (línea de comandos: `dia.exe --export=x.png --filter=png archivo.dia`). Interfaz en español.

## Capturas de aplicaciones de escritorio (DIA, Excel, Bloc de notas)

Herramienta: `_curso/herramientas/captura.ps1` (lee la ayuda al inicio del archivo).

```
powershell -ExecutionPolicy Bypass -File C:\Cerebrolo\03-Sistemas-Informacion-Gerencial\_curso\herramientas\captura.ps1 -Listar
powershell -ExecutionPolicy Bypass -File ...\captura.ps1 -Titulo "Northwind.dia" -Salida <evidencias>\05_tabla.png
powershell -ExecutionPolicy Bypass -File ...\captura.ps1 -Titulo "Northwind.dia" -Escritorio -Salida <evidencias>\01_dia.png
```

- Por defecto captura solo la ventana (PrintWindow), aunque esté tapada por otra.
- `-Escritorio` trae la ventana al frente y captura la pantalla completa. Sirve, por ejemplo, para que se vean el diagrama de DIA y su caja de herramientas, que es una ventana aparte.
- Pantalla 1920×1080 al 150 %.

**Turno de escritorio.** El escritorio es uno solo y hay varios agentes trabajando. Antes de mover, abrir o traer al frente ventanas, o de usar `-Escritorio` o `SendKeys`, toma el turno:

```
New-Item -ItemType File C:\Cerebrolo\03-Sistemas-Informacion-Gerencial\_curso\.escritorio.lock -Value "<tu lab>"
```

(sin `-Force`: si ya existe, falla; espera y vuelve a intentar con un bucle de 15 s). Haz tus capturas en ráfaga y bórralo enseguida (`Remove-Item ...\.escritorio.lock`). No lo tengas tomado más de 5 minutos seguidos. Las capturas de solo ventana (sin `-Escritorio`) de una ventana que ya está abierta no necesitan turno.

Cierra las ventanas que abriste cuando termines. Gerald está usando la PC: no toques ventanas que no son tuyas (Chrome, terminales).

**Honestidad de los pasos.** El texto describe cómo se hace cada paso en la herramienta (menú, hoja de formas, diálogo). Las capturas tienen que ser de la herramienta de verdad, mostrando el estado que el texto describe. Si una parte del diagrama se armó editando el archivo `.dia` y después se abrió en DIA, el resultado que se ve es igual de real. Aun así, al menos un diálogo de propiedades (por ejemplo, el de atributos de una tabla) tiene que aparecer abierto en una captura, y para eso se abre de verdad con la interfaz (UIAutomation o SendKeys de PowerShell). No se instalan paquetes nuevos sin preguntarle al cerebro.

Python disponible: `py -3.13` tiene python-docx, pandas, PIL, pymupdf y pywin32 (Excel y Word por COM). openpyxl no está: los `.xlsx` se leen con pandas (si falla, con Excel por COM).
