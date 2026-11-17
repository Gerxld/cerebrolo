Revisé `ejemplo/calculadora.py` (15 líneas) y no lo modifiqué.

## Errores funcionales

1. **Línea 15: el script falla al importarlo o ejecutarlo.** `print(dividir(10, 0))` corre en el nivel superior y lanza `ZeroDivisionError` sin capturarlo. Como no hay un `if __name__ == "__main__":`, el error también salta si otro módulo hace `import calculadora`.
2. **Línea 4: `dividir` no valida `b == 0`.** Tampoco valida el tipo de los argumentos. Con `b = 0` lanza `ZeroDivisionError`. Con una cadena lanza `TypeError`.
3. **Línea 7: `promedio` falla con una lista vacía.** Si `valores` está vacío, `len(valores)` es 0 y lanza `ZeroDivisionError`. Eso pasa siempre que se llame sin argumentos, porque el valor por defecto es `[]`.
4. **Línea 6: el valor por defecto de `promedio` es mutable (`valores=[]`).** Hoy no se muta, así que no causa un bug visible. Pero es un antipatrón y se vuelve una trampa si alguien añade un `append`. Además, no tiene sentido como valor por defecto, porque con él la función siempre falla.
5. **Líneas 9–13: `procesar` devuelve `0` ante cualquier error.** Mezcla "el dato era inválido" con "el dato era realmente 0". Un `"abc"` y un `"0"` dan el mismo resultado, y quien llama no puede distinguirlos.
6. **Línea 11: `int(numero)` trunca y rechaza decimales.** `int("3.5")` lanza `ValueError`, que el `except` convierte en `0`. `int(3.9)` da `3` sin avisar. Para una calculadora esto probablemente no es lo esperado.
7. **`procesar` no se usa.** Ni `procesar` ni `promedio` se invocan en el archivo, así que no hay forma de ver si funcionan.

## Riesgos de mantenimiento

- **Línea 12: `except:` desnudo.** Captura todo, incluidos `KeyboardInterrupt` y `SystemExit`, y oculta bugs reales. Debería ser `except (ValueError, TypeError):`.
- **Errores silenciados.** No hay logging ni mensaje cuando `procesar` falla, así que depurar un `0` inesperado es difícil.
- **No hay docstrings, anotaciones de tipo ni pruebas.** No se sabe qué contrato tienen las funciones (qué reciben, qué devuelven, qué excepciones lanzan).
- **Efectos secundarios al importar.** El `print` de la línea 15 hace que el módulo no se pueda reutilizar ni probar con `pytest` sin que se dispare el error.
- **El nombre `procesar` es vago.** Lo que hace es convertir a entero. Algo como `a_entero` lo diría mejor.
- **Inconsistencia en el manejo de errores.** `dividir` y `promedio` propagan excepciones, y `procesar` las traga. No hay una política única.

## Seguridad

No hay vulnerabilidades graves, porque el archivo no usa `eval`, `exec`, archivos, red ni subprocesos. Hay dos riesgos menores:

- **Datos inválidos que pasan sin que nadie lo note.** El `except:` de `procesar` convierte entradas maliciosas o corruptas en `0`. Si ese valor alimenta una cantidad, un precio o un divisor, el programa sigue con un dato falso en lugar de rechazarlo.
- **Denegación de servicio por excepción no controlada.** Si estas funciones se expusieran en un servicio, un `b = 0` o una lista vacía enviados por el usuario tumbarían la petición. Con el `except:` desnudo ocurre algo parecido en sentido contrario: se oculta el fallo y se pierde la trazabilidad.

## Prioridad sugerida

1. Mover el `print` a un bloque `if __name__ == "__main__":`.
2. Validar `b == 0` en `dividir` y la lista vacía en `promedio`. Elige entre lanzar una excepción clara y devolver `None`.
3. Reemplazar `except:` por excepciones específicas.
4. Cambiar `valores=[]` por un parámetro obligatorio.
5. Añadir pruebas, docstrings y anotaciones de tipo.

Si quieres, te propongo el código corregido como texto, sin tocar el archivo.
