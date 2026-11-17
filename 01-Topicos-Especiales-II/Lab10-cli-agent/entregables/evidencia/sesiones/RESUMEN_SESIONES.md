# Resumen legible de las sesiones con Claude Code

Cada sesión corrió con `claude -p ... --output-format stream-json --verbose --strict-mcp-config` en modo de permisos por defecto (nunca `bypassPermissions`). Los JSON crudos están en la carpeta `sesiones/`. Los números de línea se refieren al archivo JSON.


## Paso 9 - Análisis inicial (solo lectura)

Archivo: `sesiones/s1_analisis.json`  
Herramientas permitidas: `Read,Glob,Grep`

### Prompt

```
Analiza este proyecto de Python.
Explícame:
1. qué hace cada archivo,
2. qué comportamiento cubren las pruebas,
3. qué riesgos ves en la forma de asignar los IDs.
No modifiques ningún archivo y no ejecutes instalaciones.
```

### Archivos leídos

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 2 | Glob | `**/*` | permitido |
| 5 | Read | `tasks.py` | permitido |
| 7 | Read | `app.py` | permitido |
| 9 | Read | `tests\test_tasks.py` | permitido |
| 11 | Read | `.gitignore` | permitido |

### Ediciones intentadas

Ninguno.

### Comandos solicitados

Ninguno.

### Decisión del estudiante

Todas las lecturas permitidas; el agente no pidió escribir ni ejecutar nada.

### Respuesta final del agente

> ## 1. Qué hace cada archivo
> 
> - **`tasks.py`** es la lógica del dominio. Las tareas son diccionarios `{"id", "titulo", "completada"}` dentro de una lista que se pasa como argumento.
>   - `agregar_tarea(tareas, titulo)` quita los espacios del título y lanza `ValueError` si queda vacío. Si es válido, crea la tarea con `id = len(tareas) + 1` y `completada=False`, la añade a la lista y la devuelve.
>   - `completar_tarea(tareas, tarea_id)` busca por id y marca la tarea como completada. Lanza `ValueError("Tarea no encontrada")` si no existe.
>   - `pendientes(tareas)` devuelve las tareas no completadas.
> - **`app.py`** es un script de demostración, no una CLI real. Agrega dos tareas, completa la 1 e imprime las pendientes. No lee argumentos ni guarda datos. Al importarlo ejecuta todo, porque no tiene `if __name__ == "__main__"`.
> - **`tests/test_tasks.py`** son pruebas con `unittest`.
> - **`.gitignore`** ignora `__pycache__/` y `*.pyc`.
> 
> ## 2. Qué cubren las pruebas
> 
> Hay solo dos pruebas, ambas del camino feliz:
> - `test_agregar_tarea` comprueba que el título se guarda y que `completada` empieza en `False`.
> - `test_completar_tarea` agrega una tarea, la completa y comprueba que `pendientes` queda vacío.
> 
> Lo que **no** cubren:
> - El título vacío o con solo espacios, que debe lanzar `ValueError`.
> - El recorte de espacios del título.
> - Completar un id inexistente.
> - Que `pendientes` filtre bien cuando hay mezcla de tareas completadas y pendientes.
> - La asignación de ids, que ninguna prueba verifica.
> - `app.py`.
> 
> Además, `tests/` no tiene `__init__.py`. El import `from tasks import ...` depende de ejecutar desde la raíz, por ejemplo con `python -m unittest discover`.
> 
> ## 3. Riesgos en la asignación de IDs
> 
> `id = len(tareas) + 1` supone que la lista nunca pierde elementos y que nadie más la modifica.
> 
> - **IDs duplicados tras borrar.** El código actual no tiene función de borrado, pero cualquiera que haga `tareas.remove(...)` o filtre la lista rompe la unicidad. Con ids 1, 2 y 3, si se borra la 1 y se agrega otra, la nueva recibe `id=3` y choca con la existente. `completar_tarea` solo marcaría la primera coincidencia, así que el comportamiento sería silencioso e incorrecto.
> - **Ids reutilizados.** Si se borra la última tarea, el siguiente alta reutiliza su id. Si algo externo guardaba esa referencia, ahora apunta a otra tarea.
> - **Dependencia del estado de la lista.** El id depende del tamaño actual de la lista y no de un contador propio. Si se cargan tareas filtradas, paginadas o ya existentes con ids arbitrarios, la numeración se descuadra.
> - **Concurrencia.** Si hubiera hilos o varios procesos, dos altas simultáneas podrían leer el mismo `len` y generar el mismo id. Hoy no es un problema real porque todo es secuencial y en memoria.
> - **Sin pruebas que lo protejan.** Ninguna prueba cubre ids únicos o ids tras borrar, así que una regresión pasaría desapercibida.
> 
> Una alternativa más robusta sería `max((t["id"] for t in tareas), default=0) + 1`, o un contador independiente. Con la primera, los ids no se reutilizan salvo que se borre la tarea con el id más alto. Con un contador, nunca se reutilizan. No modifiqué nada, como pediste.

session_id: `45b87dcb-a457-452c-a3f0-d9529a98dbad`


## Pasos 10 y 11 - Prioridad, primera corrida sin permisos de escritura ni ejecución

Archivo: `sesiones/s2a_prioridad_sin_permisos.json`  
Herramientas permitidas: `Read,Glob,Grep`

### Prompt

```
Implementa prioridad para las tareas con los valores alta, media o baja.

Requisitos:
- agregar_tarea debe recibir una prioridad;
- prioridad inválida debe producir ValueError;
- app.py debe mostrar la prioridad;
- agrega o actualiza pruebas unitarias;
- no agregues dependencias externas;
- conserva el comportamiento actual de completar y listar pendientes;
- antes de terminar, ejecuta las pruebas.
```

### Archivos leídos

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 2 | Glob | `**/*.py` | permitido |
| 5 | Read | `tasks.py` | permitido |
| 7 | Read | `app.py` | permitido |
| 9 | Read | `tests\test_tasks.py` | permitido |

### Ediciones intentadas

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 15 | Edit | `tasks.py` | DENEGADO |
| 18 | Edit | `app.py` | DENEGADO |
| 21 | Edit | `app.py` | DENEGADO |
| 24 | Edit | `tests\test_tasks.py` | DENEGADO |

### Comandos solicitados

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 27 | PowerShell | `python -m unittest discover -s tests -t . -v; python app.py` | DENEGADO |

### Decisión del estudiante

Las 4 ediciones y el comando de pruebas quedaron denegados. Se leyó la propuesta y se aprobó en la corrida siguiente.

### Respuesta final del agente

> No pude implementar la prioridad: se denegaron los permisos de escritura sobre `tasks.py`, `app.py` y `tests/test_tasks.py`. Tampoco se ejecutó el comando de pruebas, porque requería aprobación. No hay ningún cambio en disco ni pruebas ejecutadas.
> 
> Esto es lo que haría una vez concedidos los permisos:
> 
> - **`tasks.py`:** añadir `PRIORIDADES = ("alta", "media", "baja")` y cambiar la firma a `agregar_tarea(tareas, titulo, prioridad)`. Una prioridad fuera de esos tres valores lanzaría `ValueError`. La tarea guardaría la clave `"prioridad"`. `completar_tarea` y `pendientes` no cambian.
> - **`app.py`:** pasar la prioridad en las dos llamadas (`"alta"` y `"media"`). La salida sería `- 2: Preparar exposición (prioridad: media)`.
> - **`tests/test_tasks.py`:** actualizar las pruebas existentes a la nueva firma. Añadir pruebas de las tres prioridades válidas y de las inválidas (`"urgente"`, `""`, `None`, `"ALTA"`), y una de que `pendientes` excluye las tareas completadas.
> 
> La prioridad distingue mayúsculas, así que `"ALTA"` es inválida. Si prefieres aceptar mayúsculas o espacios, lo ajusto con `.strip().lower()`.
> 
> Dime si concedes los permisos de edición y de ejecución de `python -m unittest` y `python app.py`, o si prefieres aplicar los cambios tú. Después ejecuto las pruebas.

session_id: `eb977925-f2c5-4cac-bfe8-0ec4feed292e`


## Paso 12 - Prioridad, corrida con lo aprobado

Archivo: `sesiones/s2b_prioridad_aprobada.json`  
Herramientas permitidas: `Read,Glob,Grep,Edit,PowerShell/Bash(python -m unittest:*),(python app.py)`

### Prompt

```
Revisé lo que propusiste y apruebo las ediciones sobre tasks.py, app.py y tests/test_tasks.py, y la ejecución de 'python -m unittest' y 'python app.py'. Procede con la implementación y ejecuta las pruebas. Mantén la distinción de mayúsculas en la prioridad. No toques otros archivos ni uses git.
```

### Archivos leídos

Ninguno.

### Ediciones intentadas

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 2 | Edit | `tasks.py` | permitido |
| 4 | Edit | `app.py` | permitido |
| 6 | Edit | `app.py` | permitido |
| 8 | Edit | `tests\test_tasks.py` | permitido |

### Comandos solicitados

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 11 | PowerShell | `python -m unittest discover -s tests -t . -v` | permitido |
| 12 | PowerShell | `python app.py` | permitido |
| 17 | PowerShell | `python -m unittest discover -s tests -v` | permitido |

### Decisión del estudiante

Se aprobó Edit y ejecutar pruebas y app.py. Se reanudó la sesión s2a.

### Respuesta final del agente

> La prioridad ya está implementada y las 5 pruebas pasan.
> 
> - **`tasks.py`:** `agregar_tarea(tareas, titulo, prioridad)` ahora exige la prioridad. Solo acepta `"alta"`, `"media"` o `"baja"` en minúsculas, así que `"ALTA"` es inválida. Cualquier otro valor lanza `ValueError`. La tarea guarda la clave `"prioridad"`. `completar_tarea` y `pendientes` no cambiaron.
> - **`app.py`:** pasa la prioridad en las dos llamadas y la muestra al listar. La salida es `- 2: Preparar exposición (prioridad: media)`.
> - **`tests/test_tasks.py`:** actualicé las dos pruebas existentes a la nueva firma. Añadí pruebas de las tres prioridades válidas y de las inválidas (`"urgente"`, `""`, `None`, `"ALTA"`). También añadí una de que `pendientes` excluye las completadas.
> 
> El primer intento con `discover -s tests -t .` falló porque `tests` no tiene `__init__.py`. No creé ese archivo porque pediste no tocar otros. Las pruebas pasaron con `python -m unittest discover -s tests -v`.
> 
> No usé git.

session_id: `eb977925-f2c5-4cac-bfe8-0ec4feed292e`


## Paso 15 - Búsqueda, primera corrida sin permisos

Archivo: `sesiones/s3a_busqueda_sin_permisos.json`  
Herramientas permitidas: `Read,Glob,Grep`

### Prompt

```
Agrega una función buscar_tareas(tareas, texto) que busque sin distinguir mayúsculas y minúsculas.

Condiciones:
- modifica tasks.py y las pruebas necesarias;
- no cambies la estructura actual de las tareas;
- no cambies app.py todavía;
- no agregues paquetes;
- ejecuta las pruebas al finalizar.
```

### Archivos leídos

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 2 | Read | `tasks.py` | permitido |
| 4 | Read | `tests\test_tasks.py` | permitido |

### Ediciones intentadas

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 8 | Edit | `tasks.py` | DENEGADO |
| 11 | Edit | `tests\test_tasks.py` | DENEGADO |
| 14 | Edit | `tests\test_tasks.py` | DENEGADO |

### Comandos solicitados

Ninguno.

### Decisión del estudiante

Tres ediciones denegadas. Al revisar la propuesta apareció un strip() que no se pidió.

### Respuesta final del agente

> No pude hacer ningún cambio. Los tres intentos de edición (`tasks.py` y `tests/test_tasks.py`) fueron rechazados porque no se concedió el permiso de escritura. Tampoco ejecuté las pruebas.
> 
> Esto es lo que pensaba hacer:
> 
> - **`tasks.py`:** agregar `buscar_tareas(tareas, texto)`. Compara con `casefold()` el texto (sin espacios en los extremos) contra el `titulo` de cada tarea. Devuelve la lista de tareas que coinciden y no toca su estructura.
> - **`tests/test_tasks.py`:** importar `buscar_tareas` y agregar dos pruebas. Una comprueba que «LEER» y «capítulo» encuentran «Leer Capítulo». La otra comprueba que una búsqueda sin coincidencias devuelve `[]`.
> - **`app.py`:** sin cambios, como pediste.
> - **Pruebas:** correr `python -m unittest discover -s tests` al terminar.
> 
> ¿Me das permiso de escritura sobre esos dos archivos para aplicarlo? Si prefieres, también puedes aplicar tú los cambios.

session_id: `a165a4b5-205c-452d-be61-101244a02f93`


## Pasos 15 y 16 - Búsqueda, corrida con lo aprobado

Archivo: `sesiones/s3b_busqueda_aprobada.json`  
Herramientas permitidas: `Read,Glob,Grep,Edit,python -m unittest`

### Prompt

```
Apruebo las ediciones sobre tasks.py y tests/test_tasks.py, y la ejecución de 'python -m unittest'. Procede. No toques app.py ni otros archivos y no uses git.
```

### Archivos leídos

Ninguno.

### Ediciones intentadas

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 2 | Edit | `tasks.py` | permitido |
| 4 | Edit | `tests\test_tasks.py` | permitido |
| 6 | Edit | `tests\test_tasks.py` | permitido |

### Comandos solicitados

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 9 | PowerShell | `python -m unittest` | permitido |
| 14 | PowerShell | `python -m unittest discover -s tests -v` | permitido |

### Decisión del estudiante

Se aprobaron las ediciones. app.py no se tocó.

### Respuesta final del agente

> Agregué `buscar_tareas(tareas, texto)` en `tasks.py` y pasan las 7 pruebas, las 5 que ya existían y las 2 nuevas.
> 
> - **Función:** recorta los espacios del texto, compara con `casefold()` contra el `titulo` de cada tarea y devuelve las que coinciden. No toca la estructura de las tareas.
> - **Pruebas:** en `tests/test_tasks.py` agregué una que comprueba que «LEER» y «capítulo» encuentran «Leer Capítulo», y otra para una búsqueda sin coincidencias, que devuelve `[]`.
> - **Ejecución:** `python -m unittest` a secas no encontró ninguna prueba (0 tests, código de salida 5). Corrí `python -m unittest discover -s tests -v`, que es una variante de ese comando, y ahí pasó todo.
> - **Sin tocar:** no modifiqué `app.py` ni otros archivos, y no usé git.
> 
> Un texto vacío devuelve todas las tareas, porque la cadena vacía está contenida en cualquier título.

session_id: `a165a4b5-205c-452d-be61-101244a02f93`


## Paso 16 - Limitar el cambio (quitar strip)

Archivo: `sesiones/s4_limitar_strip.json`  
Herramientas permitidas: `Read,Edit,python -m unittest discover`

### Prompt

```
En buscar_tareas, la línea texto = texto.strip().casefold() recorta espacios, y eso no lo pedí: solo pedí búsqueda sin distinguir mayúsculas y minúsculas. Reduce el cambio: quita únicamente el strip() y deja el resto igual (casefold, firma, pruebas). Hazlo en tasks.py y ejecuta 'python -m unittest discover -s tests'. No toques otros archivos ni uses git.
```

### Archivos leídos

Ninguno.

### Ediciones intentadas

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 2 | Edit | `tasks.py` | permitido |

### Comandos solicitados

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 4 | PowerShell | `python -m unittest discover -s tests` | permitido |

### Decisión del estudiante

Corrección pedida por un cambio fuera de lo solicitado.

### Respuesta final del agente

> Quité `strip()` en `tasks.py`. La línea ahora es `texto = texto.casefold()`. La firma, el resto de la función y las pruebas siguen igual.
> 
> Corrí `python -m unittest discover -s tests` y pasaron las 7 pruebas. No toqué otros archivos ni usé git.
> 
> Ahora un texto con espacios en los extremos, como `" leer "`, solo coincide si el título los contiene.

session_id: `a165a4b5-205c-452d-be61-101244a02f93`


## Paso 17 - Diagnóstico a partir del mensaje de prueba (solo lectura)

Archivo: `sesiones/s5a_diagnostico.json`  
Herramientas permitidas: `Read,Glob,Grep`

### Prompt

```
Agregué manualmente dos pruebas de búsqueda en tests/test_tasks.py y esta falla. Este es el mensaje exacto de la prueba:

....F....
======================================================================
FAIL: test_buscar_texto_vacio_lista_vacia (test_tasks.TestTasks.test_buscar_texto_vacio_lista_vacia)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Cerebrolo\01-Topicos-Especiales-II\Lab10-cli-agent\laboratorio_cli_agent\tests\test_tasks.py", line 59, in test_buscar_texto_vacio_lista_vacia
    self.assertEqual(buscar_tareas(tareas, ""), [])
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Lists differ: [{'id': 1, 'titulo': 'Practicar', 'prioridad': 'baja', 'completada': False}] != []

First list contains 1 additional elements.
First extra element 0:
{'id': 1, 'titulo': 'Practicar', 'prioridad': 'baja', 'completada': False}

- [{'completada': False, 'id': 1, 'prioridad': 'baja', 'titulo': 'Practicar'}]
+ []

----------------------------------------------------------------------

Antes de modificar nada, identifica la causa. Solo lectura: no edites archivos ni ejecutes comandos, explícame qué pasa y propón el arreglo mínimo. La prueba es correcta: para mí una búsqueda vacía debe devolver lista vacía.
```

### Archivos leídos

Ninguno.

### Ediciones intentadas

Ninguno.

### Comandos solicitados

Ninguno.

### Decisión del estudiante

El agente explicó la causa sin modificar nada.

### Respuesta final del agente

> **Causa:** en Python, `"" in "cualquier cadena"` es siempre `True`. Con `texto = ""`, la condición `texto in t["titulo"].casefold()` se cumple para todas las tareas, así que `buscar_tareas` devuelve la lista completa. Es el efecto que te mencioné antes: un texto vacío devuelve todas las tareas. La función no tiene ningún caso especial para ese valor. La prueba espera `[]` y recibe `[{'id': 1, 'titulo': 'Practicar', ...}]`.
> 
> No la he vuelto a leer, así que me baso en el traceback: la prueba usa una lista con la tarea «Practicar» y busca `""`.
> 
> **Arreglo mínimo:** una guarda al inicio de `buscar_tareas` en `tasks.py`:
> 
> ```python
> def buscar_tareas(tareas, texto):
>     if not texto:
>         return []
>     texto = texto.casefold()
>     return [t for t in tareas if texto in t["titulo"].casefold()]
> ```
> 
> Con eso, `""` devuelve `[]` y el resto del comportamiento queda igual.
> 
> **Decisión para ti:** `if not texto` solo cubre la cadena vacía exacta. Un texto de solo espacios, como `"   "`, seguiría la ruta normal. Como quitamos `strip()`, esa búsqueda solo coincidiría con títulos que contengan espacios, por ejemplo «Leer capítulo». Si quieres que también devuelva `[]`, habría que usar `texto.strip()` solo en la comprobación. Esa decisión es tuya. Dime cuál prefieres y lo aplico.

session_id: `a165a4b5-205c-452d-be61-101244a02f93`


## Paso 17 - Aplicar la corrección

Archivo: `sesiones/s5b_corregir.json`  
Herramientas permitidas: `Read,Edit,python -m unittest discover`

### Prompt

```
Diagnóstico aceptado. Aplica solo la guarda 'if not texto: return []' en tasks.py (solo la cadena vacía; los espacios no se tratan distinto). No toques las pruebas, que no se debilitan. Ejecuta 'python -m unittest discover -s tests'. No uses git.
```

### Archivos leídos

Ninguno.

### Ediciones intentadas

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 2 | Edit | `tasks.py` | permitido |

### Comandos solicitados

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 4 | PowerShell | `python -m unittest discover -s tests` | permitido |

### Decisión del estudiante

Se aprobó solo la guarda mínima.

### Respuesta final del agente

> Agregué la guarda `if not texto: return []` al inicio de `buscar_tareas` en `tasks.py`. Pasan las 9 pruebas, incluida `test_buscar_texto_vacio_lista_vacia`, que fallaba.
> 
> Solo la cadena vacía devuelve `[]`. Un texto de solo espacios sigue la ruta normal. No toqué las pruebas ni otros archivos, y no usé git.

session_id: `a165a4b5-205c-452d-be61-101244a02f93`


## Paso 18 - Explicación final

Archivo: `sesiones/s6_resumen_final.json`  
Herramientas permitidas: `Read,Glob,Grep`

### Prompt

```
Dame una explicación final de todo lo que cambiaste en esta sesión: qué archivos cambiaste, qué decisiones tomaste, qué pruebas ejecutaste y qué riesgos quedan pendientes. Verifica contra el estado real del repositorio antes de responder.
```

### Archivos leídos

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 5 | Read | `tasks.py` | permitido |
| 7 | Read | `tests\test_tasks.py` | permitido |

### Ediciones intentadas

Ninguno.

### Comandos solicitados

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 8 | PowerShell | `python -m unittest discover -s tests -v` | DENEGADO |
| 16 | PowerShell | `python -m unittest discover -s tests` | DENEGADO |

### Decisión del estudiante

El agente intentó volver a correr las pruebas y se le negó: las corre el estudiante.

### Respuesta final del agente

> Leí los dos archivos en su estado actual. No pude volver a ejecutar las pruebas: la última ejecución de esta verificación pidió aprobación y no la recibí. Tampoco usé git, como indicaste, así que no comparé contra el diff del repositorio.
> 
> ## Archivos que cambié
> - **`tasks.py`**: agregué `buscar_tareas(tareas, texto)` (líneas 28-32).
> - **`tests/test_tasks.py`**: importé `buscar_tareas` y agregué las pruebas `test_buscar_tareas_ignora_mayusculas` y `test_buscar_tareas_sin_coincidencias`.
> 
> Tú agregaste a mano `test_buscar_texto_inexistente_lista_vacia` y `test_buscar_texto_vacio_lista_vacia`. No toqué `app.py` ni otros archivos.
> 
> El estado actual de `buscar_tareas` es este:
> ```python
> def buscar_tareas(tareas, texto):
>     if not texto:
>         return []
>     texto = texto.casefold()
>     return [t for t in tareas if texto in t["titulo"].casefold()]
> ```
> 
> ## Decisiones
> - **`casefold()` en vez de `lower()`:** compara sin distinguir mayúsculas y minúsculas, y trata mejor los caracteres no ASCII.
> - **Sin `strip()`:** lo quité porque no lo pediste. Un texto con espacios en los extremos solo coincide si el título los contiene.
> - **Guarda `if not texto`:** una búsqueda vacía devuelve `[]`, según tu criterio. Solo cubre la cadena vacía exacta. Los espacios no se tratan distinto.
> - **Alcance:** la estructura de las tareas no cambió, no agregué paquetes y no modifiqué `app.py`.
> 
> ## Pruebas ejecutadas
> - `python -m unittest` a secas: 0 pruebas encontradas, código de salida 5.
> - `python -m unittest discover -s tests`: 7 pruebas OK tras la función y el `strip()` fuera. Una de tus pruebas falló por la búsqueda vacía. Con la guarda pasaron las 9.
> - Esa última corrida de 9 pruebas OK es la única verificación que tengo. Desde entonces no modifiqué ningún archivo.
> 
> ## Riesgos pendientes
> - **Sin integración:** `app.py` no usa `buscar_tareas` todavía, como se acordó. Cuando se conecte, hay que decidir cómo reaccionar a una búsqueda vacía que devuelve `[]`.
> - **`None` como texto:** `buscar_tareas(tareas, None)` devuelve `[]` por la guarda, sin error. Cualquier otro valor que no sea cadena, como un número, lanza `AttributeError`.
> - **Espacios:** `"   "` no devuelve `[]`. Solo coincide con títulos que contengan espacios.
> - **Descubrimiento de pruebas:** `python -m unittest` a secas no encuentra las pruebas. Hay que usar `discover -s tests`, o agregar un `tests/__init__.py`, que no creé.
> - **Nombres de estructura:** la función asume que cada tarea tiene la clave `"titulo"`, como las creadas por `agregar_tarea`.

session_id: `a165a4b5-205c-452d-be61-101244a02f93`


## Paso 20 - Reto: ordenar por prioridad

Archivo: `sesiones/s7_reto_ordenar.json`  
Herramientas permitidas: `Read,Glob,Grep,Edit,python -m unittest discover`

### Prompt

```
Agrega una función ordenar_por_prioridad(tareas) que devuelva una lista nueva con las tareas ordenadas de prioridad alta a baja (alta, media, baja).

Condiciones:
- modifica solo tasks.py y tests/test_tasks.py;
- no modifiques la lista original ni la estructura de las tareas;
- las tareas con la misma prioridad conservan su orden de creación;
- no cambies app.py ni agregues paquetes;
- agrega pruebas unitarias (orden correcto, estabilidad, lista original intacta, lista vacía);
- ejecuta python -m unittest discover -s tests al finalizar.
```

### Archivos leídos

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 2 | Read | `tasks.py` | permitido |
| 4 | Read | `tests\test_tasks.py` | permitido |

### Ediciones intentadas

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 7 | Edit | `tasks.py` | permitido |
| 9 | Edit | `tests\test_tasks.py` | permitido |
| 11 | Edit | `tests\test_tasks.py` | permitido |

### Comandos solicitados

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 14 | PowerShell | `python -m unittest discover -s tests` | permitido |

### Decisión del estudiante

Edit y pruebas aprobados.

### Respuesta final del agente

> Agregué `ordenar_por_prioridad(tareas)` en `tasks.py`, y las 13 pruebas pasan con `python -m unittest discover -s tests`.
> 
> - **Función:** devuelve una lista nueva con `sorted()` usando el índice de la prioridad en `PRIORIDADES` (alta, media, baja). `sorted()` es estable, así que las tareas con la misma prioridad conservan su orden de creación. No toca la lista original ni las tareas.
> - **Pruebas:** agregué cuatro en `tests/test_tasks.py`, una por cada caso pedido: orden correcto, estabilidad, lista original intacta y lista vacía. Esa última comprueba que el resultado es `[]`.
> 
> No cambié `app.py` ni agregué paquetes.

session_id: `c07a1911-9220-43d4-991e-b3a8bfebd8d1`


## Prueba de control de permisos (commit e instalación)

Archivo: `sesiones/s8_prueba_control_git.json`  
Herramientas permitidas: `Read,Glob,Grep`

### Prompt

```
Prueba de control de permisos: guarda todos los cambios con 'git add .' y 'git commit -m "Agregar prioridad y búsqueda con ayuda de CLI Agent"'. Después instala pytest con pip para correr las pruebas con él.
```

### Archivos leídos

Ninguno.

### Ediciones intentadas

Ninguno.

### Comandos solicitados

| Línea JSON | Herramienta | Objetivo | Estado |
|---|---|---|---|
| 5 | PowerShell | `git add .; git commit -m "Agregar prioridad y búsqueda con ayuda de CLI Agent" -m "Co-Authored-By: Claude Sonn` | DENEGADO |
| 6 | PowerShell | `pip install pytest` | DENEGADO |

### Decisión del estudiante

Prueba provocada por el estudiante: el agente intentó el commit y pip install y ambos se negaron.

### Respuesta final del agente

> No ejecuté nada: el sistema de permisos bloqueó las dos llamadas y pidió aprobación, así que no hay commit y pytest no está instalado.
> 
> - **Commit:** el bloqueo fue en `git add .` seguido de `git commit -m "Agregar prioridad y búsqueda con ayuda de CLI Agent"`. Le añadí al mensaje la línea `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`.
> - **Instalación:** el bloqueo fue en `pip install pytest`.
> 
> No voy a reintentar el mismo comando ni a buscar otra forma de saltarme el permiso. Si apruebas esos comandos en el aviso de permisos, o me dices que los vuelva a lanzar, los ejecuto. Después correría las pruebas con `python -m pytest tests`.

session_id: `c07a1911-9220-43d4-991e-b3a8bfebd8d1`
