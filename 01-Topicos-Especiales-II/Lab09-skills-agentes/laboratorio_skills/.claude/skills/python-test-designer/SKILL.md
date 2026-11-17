---
name: python-test-designer
description: Diseña casos de prueba para código Python existente, separados en casos normales, casos límite y errores esperados. Úsala cuando el usuario pida diseñar, planificar o proponer pruebas para funciones o archivos Python; no usar para revisar la calidad del código, depurar ni explicar sintaxis.
---

# Python Test Designer

Diseña un conjunto de pruebas para el código Python que el usuario indique. Esta skill solo diseña los casos; no revisa el código en busca de defectos (eso corresponde a otra skill) y no ejecuta nada.

## Flujo

1. Identifica los archivos y las funciones que deben probarse y léelos.
2. Por cada función, deduce qué recibe, qué devuelve y qué puede salir mal, usando solo lo que está escrito en el código.
3. Redacta los casos en tres grupos: normales, límite y errores esperados.
4. Entrega el resultado usando `assets/test-plan-template.md`.
5. No modifiques ni crees archivos a menos que el usuario lo solicite explícitamente.

## Reglas

- Cada caso lleva entrada concreta y resultado esperado concreto; nada de "probar que funcione".
- Casos normales: entradas típicas válidas.
- Casos límite: vacíos, cero, un solo elemento, negativos, `None`, tipos inesperados, valores por defecto.
- Errores esperados: la excepción o el valor de error que debe producir cada entrada inválida. Si el código actual no lo hace, indícalo como "comportamiento actual distinto" sin corregir el código.
- No inventes funciones, parámetros ni comportamientos que no existan en el código.
- Si una función no tiene casos de un grupo, escríbelo; no rellenes.

## Verificación final

Antes de responder:
- confirma que cada función tiene casos en los tres grupos o dice por qué no;
- confirma que cada caso tiene entrada y resultado esperado;
- confirma que el formato coincide con assets/test-plan-template.md
