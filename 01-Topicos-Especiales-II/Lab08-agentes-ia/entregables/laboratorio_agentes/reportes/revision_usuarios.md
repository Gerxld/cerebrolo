## Análisis de proyecto

1. **Archivo de validación de correo electrónico**
   - Se encuentra en `usuarios.py`
   - Función: `email_valido(email)` que verifica que el correo contenga `@` y un punto en la parte después del `@`.

2. **Casos de prueba para usuarios**
   - `test_email_valido`: Valida correos correctamente formateados (ej. `ana@utp.ac.pa`)
   - `test_email_invalido`: Verifica correos inválidos (ej. `ana@utp`)
   - `test_nombre_obligatorio`: Asegura que el nombre no esté vacío al crear un usuario

**Conclusión**: El proyecto valida el correo electrónico en `usuarios.py` y cubre tres casos clave en las pruebas de usuarios.