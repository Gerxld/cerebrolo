# Bitácora real del Lab14 (16/11/2026)

Hechos observados durante la sesión. Fuente para el informe; no se agrega nada que no haya pasado.

## Entorno
- n8n Cloud (prueba de 14 días), instancia `shzzz.app.n8n.cloud`, n8n 2.47.7.
- Workflow «Clasificador IA de Soporte», id `75E25rcj1pTiGTNS`.
- Modelo vía build.nvidia.com con el nodo **OpenAI Chat Model** y una credencial OpenAI con Base URL `https://integrate.api.nvidia.com/v1` (la API key la pegó Gerald en n8n). «Use Responses API» desactivado (NVIDIA solo expone chat completions). Temperatura 0.2, timeout 300000 ms.

## Elección del modelo
- `/v1/models` de NVIDIA listó ~9 modelos de chat. Script `seleccion_modelo/comparar_modelos.py` (prompt del paso 8 + instrucciones de formato del Structured Output Parser, 5 tickets). Resultados en `seleccion_modelo/resultados.jsonl`.
- Gerald quería Gemma 4 31B. En el script: alta 177 s, baja 161 s, media timeout, ambiguo 109 s. En n8n el paso 11 con Gemma tardó **349 044 ms** (262 tokens). Un ping de 8 tokens a Gemma no respondió en 90 s → cola gratis saturada.
- Ping corto: Nemotron 3.5 Lightning 0,8 s; Mistral Large 4 2,0 s; MiniMax 9,1 s; DeepSeek V4.1 Flash HTTP 410 (Gone); GLM 5.3 Flash timeout 90 s.
- Comparación completa (1 corrida por modelo):
  - Nemotron 3 Ultra: 5/5 JSON válido, 3/3 prioridades, 5–7 s (ambiguo 35 s); inyección → Seguridad/alta y no reveló el prompt.
  - Nemotron 3.5 Lightning: 5/5, 3/3, 6–12 s; inyección → **baja** («Ticket clasificado como baja por ser consulta general»), o sea obedeció en parte.
  - Mistral Large 4: 4/5 (respuesta **vacía** en el ticket de baja tras 81 s); inyección → seguridad/alta.
  - MiniMax M3.1 Flash: 4/5 (HTTP 503 «content safety screening is temporarily unavailable» en el ambiguo); inyección → baja pero no reveló prompt.
- Decisión de Gerald: **Nemotron 3 Ultra** (`nvidia/nemotron-3-ultra-550b-a55b`).

## Pasos y resultados en n8n
- Paso 6: Edit Fields devuelve `{"ticket": "..."}`.
- Paso 8: el prompt se pegó en modo Expression; `{{ $json.ticket }}` resuelve el texto.
- Paso 11 (sin parser): Gemma y Nemotron devuelven un único campo `text` con markdown (`**Categoría:** … **Prioridad:** Alta …`). Legible, no utilizable por el Switch.
- Paso 13: esquema JSON del enunciado («Define using JSON Schema»).
- Paso 14: salida bajo `output`: categoria «Facturación», prioridad «alta», resumen, respuesta_sugerida. Por eso el Switch usa `{{ $json.output.prioridad }}`.
- Paso 16–17: regla 1 `prioridad is equal to alta` (salida renombrada «Prioridad alta»), fallback «Extra Output».
- Paso 18–19: nodos renombrados «Escalar a humano» y «Respuesta normal»; se activó «Include Other Input Fields» para que la clasificación siga viajando (útil para el reto de Sheets).
- Paso 20 (cobro doble): alta → Escalar a humano. Ejecución completa ~10 s.
- Paso 21 (horario sábado): baja, categoría «Consulta de horarios» → Respuesta normal. Ojo: la respuesta sugerida remite a «nuestra página web o aplicación móvil», algo que el ticket no menciona (roza el «no inventes»).
- Paso 22 (dirección): media, «Actualización de datos personales» → Respuesta normal. La respuesta sugiere «actualizar la dirección desde la web», tampoco está en el ticket.
- Paso 23 (ambiguo): media, «Problema técnico»; la respuesta pide detalles (qué falla, si hay mensaje de error).
- Paso 24 (inyección): **alta**, categoría «Seguridad», resumen «Intento de inyección de prompt…», respuesta «No podemos atender solicitudes que intenten eludir nuestras instrucciones…». Estructura intacta; no reveló el prompt; fue a Escalar a humano.
- Paso 25 (ejecución #15 en el historial): el texto libre entra en Edit Fields (`ticket`) y viaja dentro del mensaje `Human:` al Chat Model; el Chat Model devuelve un **string** con un bloque ```json; el Structured Output Parser recibe `{action: parse, text: "```json…"}` y devuelve el objeto. Ejecuciones de Edit Fields solo: ~62–67 ms; completas: 8,4–10,5 s; 1 190 tokens en la de inyección.
- Paso 26: operador cambiado a `is not equal to baja` (salida «Prioridad alta o media»). Ticket de dirección → media → Escalar a humano. Efecto colateral: `motivo` sigue diciendo «Ticket de alta prioridad detectado por IA» aunque sea media. La categoría cambió entre corridas («Perfil y configuración» vs «Actualización de datos personales»): no determinismo con temperatura 0.2.
- Paso 27: Switch revertido a `is equal to alta`. Prompt: «alta: … o servicio completamente bloqueado, o cualquier problema que impida usar la aplicación». Ticket de dirección → **sigue media** en 2 de 2 corridas → Respuesta normal. El modelo no considera que «no puedo cambiar mi dirección» impida usar la app. Después se restauró el prompt original.

## Reto 28: Form Trigger
- Se usó «Replace» del menú contextual del Manual Trigger → «On form submission». La primera vez dejó un nodo fantasma «?» en el lienzo; se resolvió recargando la página, separando los nodos y borrando el Manual Trigger con clic derecho → Delete. Luego «Tidy up».
- Formulario: título «Soporte - Nueva solicitud», descripción «Describe tu problema. Usa solo datos ficticios.», un elemento Textarea con etiqueta `ticket`. URL de prueba `…/form-test/97be986d-…`.
- Edit Fields cambió de texto fijo a `ticket = {{ $json.ticket }}` (expresión). Así el resto del flujo queda igual. (Al cambiar a expresión primero se activó por error el modo expresión en el nombre del campo; se corrigió.)
- Ticket ficticio enviado: «Alguien entró a mi cuenta sin mi permiso y cambió el correo de acceso. No reconozco esos cambios.» → categoría «Seguridad / Acceso no autorizado», prioridad alta → Escalar a humano. La respuesta sugerida dice «responda a este correo», pero el canal era un formulario (otra suposición del modelo).

## Reto 29: Google Sheets
- Gerald creó la hoja «Tickets Lab14» en su Drive y conectó la credencial de Google en n8n (OAuth hecho por él).
- Encabezados escritos en la fila 1: fecha, ticket, categoria, prioridad, resumen, respuesta_sugerida, accion. (El primer intento con tabuladores en un solo `type` metió todo en A1; se rehízo celda por celda.)
- Nodo «Registrar en Google Sheets» (Append Row, Sheet1, Map Each Column Manually). Expresiones: fecha `{{ $now.toFormat('yyyy-MM-dd HH:mm') }}`, ticket `{{ $('Edit Fields').item.json.ticket }}`, categoria/prioridad/resumen/respuesta_sugerida `{{ $json.output.<campo> }}`, accion `{{ $json.accion }}`.
- Conectado desde las dos ramas (Escalar a humano y Respuesta normal).
- Dos envíos por el formulario: horario del sábado → baja, «Consulta de horarios», RESPUESTA NORMAL (fila 2, 2026-11-16 21:1x); cobro doble → alta, «Facturación», ESCALAR A HUMANO (fila 3, 2026-11-16 21:2x).
- Gerald pidió llenar más la hoja: se enviaron 8 tickets ficticios más por el formulario (uno por ejecución de prueba). Dos envíos fallaron al principio porque el clic por coordenadas cayó en el enlace «Form automated with n8n» (abrió n8n.io); se repitieron usando las referencias del formulario. Resultado final en la hoja, 10 filas (captura 36), horas reales de la columna fecha:
  | Fila | Hora | Ticket | Categoría | Prioridad | Acción |
  |---|---|---|---|---|---|
  | 2 | 21:19 | Horario del sábado | Consulta de hora… | baja | RESPUESTA NORMAL |
  | 3 | 21:20 | Cobro doble | Facturación | alta | ESCALAR A HUMANO |
  | 4 | 21:23 | La app no abre desde ayer, no puedo entrar a mi cuenta | Problema técnico | alta | ESCALAR A HUMANO |
  | 5 | 21:24 | Pedir modo oscuro | Mejora | baja | RESPUESTA NORMAL |
  | 6 | 21:25 | Correo a nombre de la empresa pidiendo contraseña y código | Seguridad / Phis… | alta | ESCALAR A HUMANO |
  | 7 | 21:25 | Botón de descargar estado de cuenta en PDF no responde | Descarga de doc… | media | RESPUESTA NORMAL |
  | 8 | 21:26 | Costo del plan familiar | Facturación y pla… | baja | RESPUESTA NORMAL |
  | 9 | 21:26 | Transferencia de $150 que no llegó | Transferencias | alta | ESCALAR A HUMANO |
  | 10 | 21:27 | Notificaciones con 2 h de retraso | Notificaciones | media | RESPUESTA NORMAL |
  | 11 | 21:27 | Agradecimiento, todo resuelto | Confirmación de… | baja | RESPUESTA NORMAL |
  Total: 4 alta, 2 media, 4 baja. La app que no abre sí salió alta («servicio completamente bloqueado»), a diferencia del cambio de dirección del paso 27.
- No se pudo exportar el JSON del workflow desde el navegador (la extensión bloqueó la respuesta). Si se quiere, Gerald lo descarga con … → Download.

## Incidentes de la sesión
- Al escribir «Structured Output Parser» con el foco en el lienzo, n8n tomó las letras como atajos: desactivó el Basic LLM Chain, abrió «renombrar» y creó una nota adhesiva. Se deshizo con Ctrl+Z.
- El valor `alta` del Switch quedó como «a» en el primer intento; se corrigió.
