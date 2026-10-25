# Brief común: investigaciones y cuestionarios de SIG (Prof. Ivan Clarence, 1GS241)

Lo leen los subagentes que hagan investigaciones o cuestionarios de esta materia. El cerebro revisa todo antes de dárselo a Gerald. Las investigaciones 1 y 3 ya cerraron en Moodle y los cuestionarios no tienen preguntas cargadas en Moodle: **todo se entrega por correo y lo envía Gerald**. Tú no envías nada.

## Formato

- Plantilla del profesor con el generador (el mismo de los labs):
  `py -3.13 C:\Cerebrolo\03-Sistemas-Informacion-Gerencial\_curso\plantilla\build_lab.py <ruta>\spec.json`
  (pon `PYTHONIOENCODING=utf-8` si imprime acentos). La documentación de los bloques está al inicio de `build_lab.py`.
- Campos de la raíz del spec:
  - `"tipo"`: `"INVESTIGACIÓN"` o `"CUESTIONARIO"`.
  - `"lab"`: el número.
  - `"titulo"`: el tema tal como lo escribe el profesor.
  - `"fecha"`: `"2026.10.27"`.
  - `"salida"`: `"Inv01_SIG_Rios_Gerald"`, `"Cuest02_SIG_Rios_Gerald"`, etc.
- Modelo real: `C:\Cerebrolo\03-Sistemas-Informacion-Gerencial\Inv02-senales\entregables\Investigacion 2.pdf`. Es la investigación de Gerald y el profe le puso 10/10. Sigue su estructura: portada → INDICE → contenido en prosa, con subtítulos y viñetas donde ayudan → CONCLUSION de 1 párrafo → REFERENCIA en APA con fecha de consulta y URL.
- **Investigación:** texto propio y bien organizado, con 2 a 4 subtítulos (`h2`), alguna tabla comparativa si sirve y citas en el texto (Autor, año). La conclusión va en un párrafo y lleva referencias. Extensión orientativa: de 4 a 8 páginas de contenido. Sin «Objetivo».
- **Cuestionario:** sin «Objetivo», sin introducción y sin conclusión (deja `"conclusion": []`). Cada pregunta va como `h2` con su número y el texto del profesor, con la ortografía corregida (tildes y signos de apertura). Debajo va la respuesta: de 1 a 3 párrafos o una lista cuando la pregunta pide «cuáles son…». Las respuestas son concretas y sin relleno. Al final va REFERENCIA con lo que se usó.

## Fuentes (lo más importante)

- **Los cuestionarios se responden con el material del profesor**, que está en `_curso\capitulos\` (PDF de cada tema). El profe pregunta lo que dio en clase, así que la respuesta tiene que coincidir con su presentación: sus listas, sus nombres y sus clasificaciones. Lee los PDF del capítulo con `py -3.14 -I` + `pymupdf` (`page.get_text()`). Si una pregunta no está en el material, complétala con una fuente web real y verificada, y no inventes.
- Para citar el material del curso: `Clarence, I. (2026). <título del PDF> [Material del curso]. Universidad Tecnológica de Panamá, Virtual-UTP.`
- **Las investigaciones** usan el material del capítulo como base y, además, de 3 a 5 fuentes web reales que hayas abierto con WebFetch. Prefiere universidades, libros, revistas, IBM, Microsoft, Oracle y similares, y evita blogs de tareas. Cada referencia en APA 7 lleva «Recuperado el 25 de octubre de 2026, de <URL>». Antes de citar, sigue `C:\Cerebrolo\.claude\skills\investigacion-apa\SKILL.md`.
- No se inventan autores, años, URL ni citas. Si una página no carga, no se cita.
- No copies párrafos de las fuentes: redacta con tus palabras. Las citas textuales, si hacen falta, van entre comillas, son cortas y son pocas.

## Redacción

- Español panameño neutro. Impersonal o en tercera persona; nada de «en este trabajo exploraremos».
- Antes de generar el PDF final, aplica `C:\Cerebrolo\.claude\skills\redaccion-humana\SKILL.md` a todo el texto.
- Ortografía cuidada. Las preguntas del profe vienen sin tildes: en el informe corrígelas, sin cambiar lo que preguntan.

## Cierre

- Escribe solo dentro de la carpeta asignada (`tmp\` no se toca).
- Genera el PDF, renderiza las páginas a PNG con `py -3.14 -I` + pymupdf y míralas. El índice tiene que cuadrar con la paginación y la portada tiene que decir «INVESTIGACIÓN #N» o «CUESTIONARIO #N».
- Nada de commits, nada de Moodle, nada de correo. No uses Chrome: la investigación web va con WebSearch y WebFetch.
- Al terminar, reporta: páginas, fuentes usadas (con URL), qué preguntas salieron del material y cuáles de la web, y cualquier duda.
