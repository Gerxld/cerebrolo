# Guía Lab 1: autocompletado con IA en VS Code

Tiempo total estimado: unas 3 horas en una sentada (el bloque de instalación es el que más puede variar).

| Bloque | Pasos del profesor | Tiempo |
|---|---|---|
| A. Instalar y configurar Copilot | 1 | 20 min |
| B. Primeras funciones | 2 a 10 | 50 min |
| C. normalizar_nombre y promedio | 11 a 13 | 25 min |
| D. Pruebas unitarias y error provocado | 14 a 16 | 40 min |
| E. Reto validar_usuario y cierre | 17 y 18 | 25 min |
| F. Reflexión y entrega al cerebro | | 20 min |

Reglas del laboratorio que no puedes saltarte: nada de Chat, Agent ni Composer; ni Ctrl+I (chat dentro del editor). Solo sugerencias inline. Lee la sugerencia completa antes de Tab. Si no entiendes una línea, la rechazas o la corriges. Los commits, si los haces, los haces tú.

Carpeta de trabajo (ábrela como raíz en VS Code):
`C:\Cerebrolo\01-Topicos-Especiales-II\Lab01-autocompletado-ide\laboratorio-autocompletar-ia\`
Ya tiene `funciones.py` y `test_funciones.py` vacíos y `decisiones.md` con la plantilla.

Capturas: Win+Shift+S, selecciona el área, haz clic en la notificación que sale, en la Herramienta de Recortes pulsa Ctrl+S y guarda con el nombre exacto en
`C:\Cerebrolo\01-Topicos-Especiales-II\Lab01-autocompletado-ide\entregables\capturas\`
En cada captura debe verse el editor con el nombre del archivo y, cuando aplique, la sugerencia en gris (el texto fantasma) o la terminal.

---

## A. Instalar y activar Copilot (20 min)

1. Abre VS Code. Ctrl+Shift+X (Extensiones), busca `GitHub Copilot` (publicador GitHub) e instálala. Si te ofrece también "Copilot Chat", puede quedar instalada; solo no la uses.
2. Inicia sesión: ícono de cuentas (abajo a la izquierda) o el ícono de Copilot de la barra de estado, "Sign in with GitHub", con tu cuenta `Gerxld`. Autoriza en el navegador.
3. Revisa el plan en https://github.com/settings/copilot. Si no tienes ninguno, prueba el plan Copilot Free (tiene tope mensual) o activa el beneficio de estudiante de GitHub Education. No tengo forma de confirmar desde aquí cuál te aparece; dime qué viste.
4. Plan B si Copilot no te deja: instala la extensión `CodeGeeX`, crea la cuenta que te pida y úsala solo en modo de sugerencias inline. Avísame antes, porque el informe cambia el nombre de la herramienta.
5. Apaga lo que no se usa. Abre la configuración JSON (Ctrl+Shift+P, "Preferences: Open User Settings (JSON)") y agrega:
   ```json
   "editor.inlineSuggest.enabled": true,
   "github.copilot.enable": { "*": true },
   "chat.commandCenter.enabled": false,
   "github.copilot.nextEditSuggestions.enabled": false
   ```
   Si VS Code subraya alguna de estas claves como desconocida, bórrala; no pasa nada. Además cierra la barra lateral derecha (Ctrl+Alt+B) y no abras el panel de Chat.
6. Terminal integrada (Ctrl+`): `python --version`. Debe salir Python 3.13.x.
   Captura: `paso01_python_version.png` (terminal con la versión y la carpeta abierta a la izquierda).
7. Captura de que Copilot está activo: `paso01b_copilot_activo.png` (barra de estado con el ícono de Copilot, sin tachar, o la pantalla de Extensiones con la extensión instalada).

Atajos de Copilot inline que vas a usar: Tab acepta, Esc rechaza, Alt+\ pide una sugerencia a mano, Alt+] y Alt+[ cambian entre alternativas.

## B. Primeras funciones (paso 2 a 10, 50 min)

Orden de trabajo en `funciones.py`. No pegues nada: escribes tú el comentario o la firma exactamente como dice el profesor, esperas y lees.

**Paso 3. Comprobar que funciona.** Escribe una línea corta (por ejemplo `x = `) y espera unos segundos. Si aparece texto gris, funciona. Esc y borra la línea.
Captura: `paso03_autocompletado_activo.png` (texto gris visible).

**Paso 4. es_par.** Escribe solo `# Devuelve True si un número entero es par y False si es impar`, Enter, espera.
- Captura antes de aceptar: `paso04_es_par_sugerencia.png`.
- Tab solo si puedes explicar la condición. Si trae código de más, Esc y reintenta.
- Captura después: `paso04b_es_par_aceptada.png`.
- Anota la fila 1 en `decisiones.md`.

**Paso 5. Probar.** Al final de `funciones.py` agrega a mano `print(es_par(8))` y `print(es_par(7))`. En la terminal: `python funciones.py`. Esperado: `True` y `False`.
Captura: `paso05_prueba_es_par.png`.

**Paso 6. Rechazar a propósito.** Escribe `# Convierte grados Celsius a Fahrenheit`, espera, y rechaza la primera con Esc aunque se vea bien.
- Captura: `paso06_celsius_rechazo1.png`.
- Cambia el comentario (por ejemplo añade "con un decimal" o reescribe parte del nombre de la función), mira la nueva propuesta.
- Captura: `paso06_celsius_segunda.png`.
- En `decisiones.md` escribe en una línea qué cambió entre ambas (sección "Paso 6") y llena las filas 2 y 3. Si aceptas la segunda, esa función se queda en `funciones.py`.

**Paso 7. aplicar_descuento (firma).** Escribe exactamente `def aplicar_descuento(precio, porcentaje):`, Enter, y espera sin escribir el cuerpo. Comprueba que calcula el descuento sobre el precio y que devuelve el precio final, no solo el descuento.
Captura: `paso07_descuento_primera.png`.

**Paso 8. Docstring si hace falta.** Si la primera no cumple, o aunque cumpla para ver si cambia, escribe dentro de la función `"""Devuelve el precio final después de aplicar el porcentaje de descuento."""` y mira si la sugerencia cambia. Quédate con la versión que puedas defender.
Captura: `paso08_descuento_docstring.png`.

**Paso 9. Validar.** Agrega `print(aplicar_descuento(100, 20))` y `print(aplicar_descuento(250, 10))`. Esperado: `80` y `225` (si te sale `80.0` o `225.0`, anótalo y decide si te parece bien; el profesor escribe 80 y 225).
Captura: `paso09_descuento_salida.png`. Si no coincide, no sigas: corrige código o contexto.

**Paso 10. Decisión.** En `decisiones.md`, responde las 3 preguntas de la sección "Paso 10" y llena las filas 4 y 5.

Tiempos: A 20, B 50. Descansa si Copilot tarda en responder; a veces hay que mover el cursor o pulsar Alt+\.

## C. normalizar_nombre y promedio (paso 11 a 13, 25 min)

**Paso 11.** Escribe el comentario: `# Recibe un nombre con espacios externos y devuelve cada palabra con inicial mayúscula` y deja que proponga `normalizar_nombre`. No abras el chat.
Captura: `paso11_normalizar_sugerencia.png`.

**Paso 12.** Prints: `print(normalizar_nombre("  ana perez  "))` y `print(normalizar_nombre("MARIA LOPEZ"))`. Esperado: `Ana Perez` y `Maria Lopez`. Si falla un caso, cambia comentario, firma o código y deja que sugiera de nuevo.
Captura: `paso12_normalizar_salida.png`.

**Paso 13. promedio.** Escribe la firma `def promedio(notas):` y la docstring `"""Devuelve el promedio de una lista; si está vacía devuelve 0."""`. Espera la sugerencia y comprueba que no divide entre cero. Prints: `print(promedio([90, 80, 70]))` y `print(promedio([]))`. Esperado: `80` y `0` (puede salir `80.0`).
Capturas: `paso13_promedio_sugerencia.png`, `paso13_promedio_salida.png`.
Llena las filas 6 y 7 de `decisiones.md`.

## D. Pruebas unitarias y error provocado (paso 14 a 16, 40 min)

**Paso 14.** Abre `test_funciones.py`. Escribe tú las importaciones (por ahora las cuatro del profesor):
```python
import unittest
from funciones import es_par, aplicar_descuento, normalizar_nombre, promedio
```
Luego el esqueleto con solo los comentarios, y esperas que la IA proponga cada cuerpo:
```python
class TestFunciones(unittest.TestCase):
    def test_es_par(self):
        # Debe aceptar pares y rechazar impares

    def test_aplicar_descuento(self):
        # 100 con 20 por ciento debe devolver 80

    def test_normalizar_nombre(self):
        # Debe quitar espacios externos y capitalizar palabras

    def test_promedio(self):
        # Debe calcular el promedio y manejar una lista vacía
```
Revisa cada `assert` antes de Tab: que el valor esperado sea el correcto y que no sea una prueba que pasa siempre. Si un assert te parece mal, lo rechazas o lo corriges. Nunca cambies una prueba solo para que pase.
Al final deja que sugiera el bloque `if __name__ == "__main__": unittest.main()`; si no sale, lo escribes tú.
Capturas: `paso14_pruebas_sugeridas.png` (una sugerencia en gris) y `paso14b_pruebas_completas.png`. Llena la fila 8.

**Paso 15. Correr todo.** En la terminal, dentro de la carpeta del proyecto:
```
python -m unittest -v
```
Captura de la terminal: `paso15_unittest_ok_inicial.png`. Luego guarda la salida en archivo:
```
cmd /c "python -m unittest -v > ..\entregables\evidencia\pruebas_inicial.txt 2>&1"
```
(Uso `cmd /c` porque el `>` de PowerShell 5 guarda el archivo en UTF-16 y con la salida rota. unittest escribe en stderr, por eso el `2>&1`.) Abre el .txt para confirmar que se lee bien y que todo termina en `ok`. Ojo: si todavía tienes los `print` en funciones.py, saldrán al principio; está bien por ahora.

**Paso 16. Provocar el error.**
1. En `promedio`, quita a mano el manejo de la lista vacía (o acepta una sugerencia que lo olvide).
2. `cmd /c "python -m unittest -v > ..\entregables\evidencia\pruebas_fallo.txt 2>&1"` y también córrelo normal para la captura: `paso16_unittest_fallo.png`.
3. Identifica qué prueba lo delató y escríbelo en `decisiones.md` como una fila nueva (tipo Corregida).
4. Restaura la función (a mano o con una nueva sugerencia) y repite hasta OK. Captura: `paso16b_unittest_restaurado.png`. Guarda `pruebas_restaurado.txt` en `evidencia` con el mismo comando.

## E. Reto final y cierre (paso 17 y 18, 25 min)

**Paso 17. validar_usuario(nombre, edad).** Reglas: True solo si el nombre, sin espacios externos, no está vacío y la edad es 18 o más; False en cualquier otro caso.
- Escribe un comentario o la firma `def validar_usuario(nombre, edad):` y espera.
- Necesitas al menos dos sugerencias distintas: rechaza la primera (Esc) o cambia el contexto (comentario, docstring), o usa Alt+] para ver otra. Captura de cada una: `paso17_validar_sugerencia1.png` y `paso17b_validar_sugerencia2.png`.
- En `decisiones.md` explica por qué elegiste la final (sección "Paso 17") y llena las filas 9 y 10. Ojo con casos raros: nombre `None`, edad como texto. Si la IA los trata distinto, anótalo; no hace falta resolverlo si el profesor no lo pide.

**Paso 18. Tres pruebas.** En `test_funciones.py`:
1. Agrega `validar_usuario` a la línea de importación (la línea original del profesor no la incluye; hay que ampliarla).
2. Con comentarios cortos, deja que la IA proponga estas tres pruebas (revisa cada assert):
   - Caso 1: nombre válido y edad de 18 o más.
   - Caso 2: nombre válido y menor de edad.
   - Caso 3: nombre vacío o solo espacios.
3. Borra todos los `print` temporales de `funciones.py`.
4. `python -m unittest -v` y captura: `paso18_unittest_final.png` (se tienen que ver todas las pruebas con ok y la línea `OK`).
5. Guarda: `cmd /c "python -m unittest -v > ..\entregables\evidencia\pruebas_final.txt 2>&1"`.
6. Abre `pruebas_final.txt` y confirma que termina en `OK`.

## F. Reflexión y entrega (20 min)

1. Abre `entregables\informe\informe.html` solo si quieres ver el esqueleto; no lo edites tú. Lo que necesito de ti está en `CHECKLIST.md`.
2. Contesta las 5 preguntas de reflexión en un archivo `reflexion_notas.md` (en `entregables\`), con tus palabras: qué pasó de verdad, aunque sean frases sueltas. Yo las paso a limpio.
3. Si quieres hacer commit, hazlo tú al final, a mano.
