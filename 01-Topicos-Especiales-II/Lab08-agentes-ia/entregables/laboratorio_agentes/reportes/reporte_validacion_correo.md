## Reporte de Análisis

### 1. ¿En qué archivo se valida el correo electrónico?
El archivo que contiene la validación de correo electrónico es **usuarios.py**. Se define la función `email_valido` que verifica la estructura del correo.

### 2. ¿Qué casos cubren las pruebas de usuarios?
Las pruebas de usuarios incluyen:
- `test_email_valido`: Valida correos válidos (ej: "ana@utp.ac.pa")
- `test_email_invalido`: Valida correos inválidos (ej: "ana@utp")

**Evidencia relevante**:
- `usuarios.py`: Implementación de `email_valido`
- `test_usuarios.py`: Casos de prueba para validación de email