# Guía Lab 4: Web Builder (Bolt.new)

Tiempo total estimado: unas 3 horas y media en una sentada. Si el plan gratis de la plataforma se queda sin créditos a medio camino, el tiempo sube; revisa eso desde el inicio.

| Bloque | Pasos del profesor | Tiempo |
|---|---|---|
| A. Cuenta, proyecto y objetivo | 1 a 3 | 15 min |
| B. Prompt inicial y primera versión | 4 y 5 | 15 min |
| C. Pruebas como usuario | 6 y 7 | 25 min |
| D. Contador y mejora de UX (con regresión y responsive) | 8 a 11 | 35 min |
| E. Caso límite y corrección | 12 | 20 min |
| F. Revisar el código generado | 13 y 14 | 20 min |
| G. Limpiar terminadas y verificación final | 15 y 16 | 25 min |
| H. Historial, publicar (opcional) y reto | 17 a 19 | 30 min |
| I. Notas de reflexión y entrega | 20 | 20 min |

Reglas: todo dentro del Web Builder. Nada de chat web externo para generar código ni editor local con agente. Tú escribes (o pegas, cuando el profesor da el texto) cada instrucción, miras el resultado y decides.

Archivos de trabajo:
- Capturas: `C:\Cerebrolo\01-Topicos-Especiales-II\Lab04-web-builder\entregables\capturas\` (Win+Shift+S, clic en la notificación, Ctrl+S en la Herramienta de Recortes, con el nombre exacto indicado). Si puedes, que se vea la barra de direcciones o el nombre de la plataforma.
- Notas y tabla de pruebas: `Lab04-web-builder\notas.md` (la llenas mientras trabajas).
- Evidencia que no sea imagen (enlaces, texto copiado): `entregables\evidencia\`.

---

## A. Cuenta y proyecto nuevo (15 min)

1. Entra a https://bolt.new/ y regístrate (puedes usar tu GitHub `Gerxld` o correo). Mira qué plan gratis te dan y cuántos tokens/créditos; anótalo en `notas.md`, va en el informe.
2. Crea un proyecto nuevo vacío. No importes nada.
   Captura: `paso01_proyecto_nuevo.png`.
3. Si Bolt no te deja (cuenta, límites, país): usa Lovable (https://lovable.dev) y, si tampoco, Replit Agent (https://replit.com). Las tres hacen lo mismo para este lab. Si cambias de plataforma, dímelo para ajustar el informe.
4. En `notas.md` escribe la frase del objetivo (paso 2 del profesor):
   “Necesito una aplicación web que permita a un estudiante organizar sus tareas académicas y saber cuáles están pendientes, en progreso o terminadas”.

## B. Prompt inicial y primera versión (15 min)

El profesor da este texto. Cópialo tal cual en la caja de instrucciones de Bolt:

```
Construye una aplicación web llamada “Gestor de tareas de estudio”.

Usuario: estudiante universitario.

Debe permitir: crear, editar y eliminar tareas; asignar título, descripción, prioridad (Alta/Media/Baja), estado (Pendiente/En progreso/Terminada) y fecha límite; buscar por texto y filtrar por estado y prioridad.

Reglas: no permitir guardar una tarea sin título; mostrar mensajes claros cuando falten datos; conservar las tareas en el navegador mediante almacenamiento local; no usar servicios externos ni autenticación.

Interfaz: sencilla, responsive, con una lista o tablero claro y un formulario fácil de usar.

Genera una primera versión funcional. No agregues funciones distintas a las solicitadas.
```

Mientras genera, no interrumpas. Cuando termine abre la vista previa y no pidas cambios todavía.
- Captura de la vista previa de la primera versión: `paso05_v1_vista_previa.png`.
- Captura del panel izquierdo con los pasos que hizo Bolt: `paso05b_v1_proceso.png`.
- Guarda también esa captura como línea base para comparar luego.

## C. Pruebas como usuario (25 min)

Panel izquierdo: trabajo de Bolt y caja de instrucciones. Panel derecho: la app.

Haz las pruebas de la tabla de `notas.md` (sección 3) y anota resultado real, aunque sea "falló". Resumen:

| ID | Prueba |
|---|---|
| P01 | Crear al menos 3 tareas con prioridades y estados distintos |
| P02 | Editar una tarea |
| P03 | Eliminar una tarea |
| P04 | (Prueba A) Intentar guardar una tarea sin título |
| P05 | (Prueba B) Crear una tarea, recargar la página y ver si permanece |
| P06 | (Prueba C) Buscar una palabra que exista en una tarea |
| P07 | (Prueba D) Combinar filtro de estado con filtro de prioridad |

Capturas:
- `paso06_tres_tareas.png` (lista con 3 o más tareas)
- `paso06_pruebaA_sin_titulo.png` (el mensaje de error o lo que pase)
- `paso06_pruebaB_recarga.png` (después de recargar)
- `paso06_pruebaC_busqueda.png`
- `paso06_pruebaD_filtros.png`

Paso 7: escribe en `notas.md` máximo 3 observaciones o mejoras (sección 4) antes de pedir nada. No pidas diez cambios de golpe. Honestidad: si la primera versión salió bien, di que salió bien y anota solo lo que de verdad notes.

## D. Refinamientos 1 y 2 (35 min)

**Instrucción de refinamiento 1 (paso 8, contador).** Cópiala tal cual:

```
Añade un contador visible con el total de tareas y cuántas están Pendientes, En progreso y Terminadas.
No cambies el modelo de datos, los filtros ni el funcionamiento del formulario actual.
Después del cambio, verifica que crear, editar y eliminar tareas siga funcionando.
```

Captura: `paso08_contador.png`.

**Paso 9. Regresión.** No lo des por bueno solo porque el contador aparece. Repite crear, editar, eliminar, buscar y filtrar, y comprueba que los números del contador cambian bien (P08 y P09 en la tabla). Captura: `paso09_regresion.png`.

**Instrucción de refinamiento 2 (paso 10, UX).** Tal cual:

```
Mejora únicamente la presentación y usabilidad.
Haz que el formulario sea más compacto y que la prioridad se distinga claramente en cada tarea.
Mantén exactamente las mismas funciones y datos.
No agregues autenticación, backend, base de datos externa ni nuevas pantallas.
```

Captura: `paso10_ux.png`. Repite la regresión rápida (crear, editar, eliminar, buscar, filtrar).

**Paso 11. Responsive.** Revisa un ancho de escritorio y uno de teléfono (unos 375 px). Usa el selector de dispositivo de la vista previa de Bolt si lo tiene; si no, abre la vista previa en una pestaña nueva y usa F12, modo dispositivo, o simplemente reduce la ventana. Los controles no deben superponerse, salirse ni quedar muy pequeños.
Capturas: `paso11_responsive_escritorio.png` y `paso11_responsive_movil.png`.

## E. Caso límite (20 min)

1. Crea una tarea con un título muy largo (unos 150 caracteres sin espacios o con pocos) y luego varias con fechas y prioridades distintas.
   Captura: `paso12_titulo_largo.png`.
2. Esta es la instrucción de refinamiento 3. Si ves un defecto, descríbelo con tus palabras a Bolt, sin decirle cómo arreglarlo. Plantilla del profesor:

```
Encontré este comportamiento al probar la aplicación: [DESCRIBE AQUÍ EL PROBLEMA].
Reproduce el problema, identifica la causa y corrígelo.
No modifiques funciones que no estén relacionadas con este error.
Al finalizar, dime brevemente qué cambiaste y qué debo volver a probar.
```

   Ejemplos del tipo de descripción (úsalos solo si es lo que de verdad viste): "el título largo se sale de la tarjeta y no se ve el botón de eliminar", "las tareas no quedan ordenadas por fecha límite".
3. Captura después de la corrección: `paso12b_corregido.png`, y repite las pruebas que Bolt te indique.
4. Si no encuentras ningún defecto después de probar de verdad (título largo, fecha pasada, descripción larga, solo espacios en el título), dilo así en `notas.md`; no inventes un bug. Dime y ajustamos esa sección.

Este es también tu ejemplo para la pregunta de reflexión sobre instrucciones demasiado generales (si te pasó, anótalo).

## F. Revisar el código generado (20 min)

1. Abre la vista de código/archivos (ícono `</>` de la barra superior del panel derecho). No modifiques nada.
2. Anota en `notas.md` (sección 5) los nombres reales de los archivos para: archivo de entrada, componentes principales, dónde se define la estructura de una tarea (tipo o interfaz), dónde se usa el almacenamiento local. En proyectos que genera Bolt es común ver algo como `index.html`, `src/main.tsx`, `src/App.tsx`, `package.json` y archivos de componentes y tipos, pero confirma con lo que veas; no copies mi lista. Mínimo 3 archivos o componentes.
3. Captura de la lista de archivos: `paso13_codigo_archivos.png`. Captura del lugar donde se usa `localStorage`: `paso13_localstorage.png`.
4. Paso 14: elige una función visible (crear tarea o filtrar por estado), localiza qué componente o función la implementa y apúntalo. Captura: `paso14_funcion_codigo.png`. Tienes que poder explicar en dos frases qué hace.

## G. Limpiar terminadas y verificación final (25 min)

**Instrucción de refinamiento 4 (paso 15).** Tal cual:

```
Agrega un botón “Limpiar tareas terminadas”.
Debe eliminar únicamente las tareas cuyo estado sea Terminada y pedir confirmación antes de hacerlo.
Reutiliza la estructura y componentes actuales del proyecto.
No cambies los filtros, el formulario ni el almacenamiento local existente.
```

Prueba: con tareas en varios estados, pulsa el botón, cancela la confirmación (no debe borrar), pulsa de nuevo y acepta (solo debe desaparecer lo Terminada) y verifica que el contador se actualiza.
Capturas: `paso15_limpiar_confirmacion.png` y `paso15b_limpiar_resultado.png`.

Con esto ya tienes 4 refinamientos reales (contador, UX, corrección del caso límite si hubo, limpiar terminadas); el profesor pide al menos tres.

**Paso 16. Lista de verificación.** Márcala en `notas.md` (sección 6) y corrige lo que falle antes de seguir:
- Función: crear/editar/eliminar; filtrar y buscar; persistencia.
- Calidad: validaciones; mensajes claros; sin errores visibles.
- Responsive: escritorio; tableta; móvil.
- Código: archivos identificables; cambios comprensibles; sin secretos expuestos.
Captura de la app en esta verificación: `paso16_verificacion_final.png`.

## H. Historial, publicar (opcional) y reto (30 min)

**Paso 17.** Abre el historial (ícono del reloj a la izquierda de la barra superior). Captura: `paso17_historial.png`. En `notas.md` (sección 7) escribe: una mejora que salió bien a la primera, una que necesitó corrección y una decisión que tomaste tú en vez de dejársela a la IA.

**Paso 18. Publicar: es opcional.** Si lo haces, solo datos ficticios, ninguna clave ni dato personal. Copia el enlace a `entregables\evidencia\enlace_publicacion.txt` y captura `paso18_publicado.png`. Si no publicas, no pasa nada; escribe "no se publicó" en `notas.md`.

**Paso 19. Reto final (con tu propia redacción, sin copiar el prompt del profesor).** Elige una: ordenar por fecha límite, mostrar tareas vencidas, vista Kanban simple o exportar tareas a un archivo. Mi sugerencia: tareas vencidas (es corto y fácil de probar con una fecha pasada). Escribe tú la instrucción con la estructura de 6 partes (objetivo, usuario, funciones, reglas, presentación, límites) e incluye qué NO debe cambiar. Guarda el texto exacto en `notas.md` (sección 8).
Después: prueba el reto y repite una regresión rápida. Anota por qué mejora el producto.
Capturas: `paso19_reto.png` y `paso20_version_final.png` (la app completa en su versión final).

## I. Cierre (20 min)

1. Pasa a `notas.md` (sección 9) tus respuestas crudas a las 5 preguntas de reflexión, con ejemplos de lo que te pasó en este lab.
2. Revisa `CHECKLIST.md` y avísame cuando esté todo.
3. Subida a Teams y commit: los haces tú.
