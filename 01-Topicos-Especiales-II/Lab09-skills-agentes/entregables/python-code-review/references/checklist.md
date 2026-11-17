# Checklist de revisión Python

## 1. Corrección funcional
- Divisiones por cero.
- Índices fuera de rango.
- Colecciones vacías.
- Valores None no controlados.
- Excepciones demasiado amplias.

## 2. Diseño y mantenibilidad
- Parámetros mutables por defecto.
- Funciones con demasiadas responsabilidades.
- Nombres poco claros.
- Código duplicado.

## 3. Seguridad
- Credenciales o secretos en el código.
- Archivos, claves o tokens secretos embebidos en el código (variables como API_KEY, TOKEN, PASSWORD, SECRET o cadenas con aspecto de clave). Todo secreto embebido se clasifica como CRÍTICO; en el informe se muestra la línea pero enmascarando el valor (por ejemplo, 'de***'), y la corrección propone leerlo de una variable de entorno.
- Uso inseguro de eval o exec.
- Construcción insegura de comandos o consultas.
- Validación insuficiente de entradas.

## 4. Calidad
- Manejo explícito de errores.
- Pruebas para casos límite.
- Mensajes de error comprensibles.
- Tipos o documentación cuando aporten claridad.

Clasifica cada hallazgo como:
CRÍTICO, ALTO, MEDIO o BAJO.
