# Paso 16 y 17: consulta al modelo sin Internet

Este paso hay que hacerlo con el equipo realmente desconectado. El script no toca la red: solo comprueba que no hay conexión y consulta al modelo local.

1. Abre PowerShell en esta carpeta (`laboratorio_local_privado`).
2. Apaga el Wi-Fi (y desconecta cable de red si usas uno). Confirma que el navegador no abre ninguna página.
3. Ejecuta:

   ```
   powershell -ExecutionPolicy Bypass -File paso16_offline.ps1
   ```

4. Espera a que termine (unos 10 a 40 segundos). Debe decir `Listo. Evidencia guardada en: ...\evidencia\16_offline.txt`.
5. Vuelve a encender el Wi-Fi.
6. Revisa que en `evidencia\16_offline.txt` aparezca «Resultado: sin Internet» y que `Get-NetAdapter` muestre el Wi-Fi como `Disconnected`. Si dice «ATENCION: hay conexion», la prueba no vale: repite con el Wi-Fi apagado.
7. Avísale al cerebro para regenerar el informe (captura, PDF y ZIP).

Durante este paso no uses modelos con nombre `cloud` ni páginas web (paso 17).
