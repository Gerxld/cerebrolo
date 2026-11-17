# paso16_offline.ps1 - Pasos 16 y 17 del Laboratorio 5 (consulta al modelo local SIN Internet)
# Uso (con el Wi-Fi apagado):  powershell -ExecutionPolicy Bypass -File paso16_offline.ps1
# Guarda todo en evidencia\16_offline.txt. No cambia ninguna configuracion de red.
param([string]$Salida = "16_offline.txt")

$ErrorActionPreference = "Continue"
$carpeta = $PSScriptRoot
$evidencia = Join-Path $carpeta "evidencia"
New-Item -ItemType Directory -Force $evidencia | Out-Null
$ruta = Join-Path $evidencia $Salida
$ollama = Join-Path $env:LOCALAPPDATA "Programs\Ollama\ollama.exe"
$modelo = "qwen2.5-coder:3b"

Start-Transcript -Path $ruta -Force | Out-Null

Write-Output "=== (a) Fecha y hora ==="
Write-Output ("Inicio: " + (Get-Date -Format "yyyy-MM-dd HH:mm:ss"))
Write-Output ("Equipo: " + $env:COMPUTERNAME + " | Script: " + $PSCommandPath)
Write-Output ""

Write-Output "=== (b) Comprobacion de que NO hay Internet ==="
$hayInternet = $false
Write-Output "PS> Test-NetConnection 8.8.8.8 -Port 53"
try {
    $t = Test-NetConnection -ComputerName 8.8.8.8 -Port 53 -WarningAction SilentlyContinue -ErrorAction Stop
    Write-Output ("TcpTestSucceeded: " + $t.TcpTestSucceeded)
    if ($t.TcpTestSucceeded) { $hayInternet = $true }
} catch {
    Write-Output ("Fallo (esperado sin red): " + $_.Exception.Message)
}
Write-Output "PS> Resolve-DnsName ollama.com"
try {
    $d = Resolve-DnsName -Name ollama.com -Type A -DnsOnly -ErrorAction Stop
    Write-Output ("Resolvio: " + (($d | Where-Object { $_.IPAddress } | ForEach-Object { $_.IPAddress }) -join ", "))
    $hayInternet = $true
} catch {
    Write-Output ("Fallo (esperado sin red): " + $_.Exception.Message)
}
if ($hayInternet) {
    Write-Output "ATENCION: hay conexion a Internet. Esta ejecucion NO sirve como prueba offline; apaga el Wi-Fi y repite."
} else {
    Write-Output "Resultado: sin Internet (ni conexion a 8.8.8.8:53 ni resolucion DNS de ollama.com)."
}
Write-Output ""

Write-Output "=== (c) Adaptadores de red ==="
Write-Output "PS> Get-NetAdapter | Select Name,Status"
Get-NetAdapter | Select-Object Name, Status | Format-Table -AutoSize | Out-String -Width 200 | Write-Output
Write-Output ""

Write-Output "=== (d) Consulta al modelo local ==="
Write-Output "Ruta de Ollama: $ollama"
Write-Output "PS> & '$ollama' --version"
& $ollama --version 2>&1 | ForEach-Object { Write-Output ("" + $_) }
Write-Output "PS> & '$ollama' list"
& $ollama list 2>&1 | ForEach-Object { Write-Output ("" + $_) }

$codigo = Get-Content (Join-Path $carpeta "calculadora.py") -Raw -Encoding UTF8
$prompt = "Responde en espanol y en maximo tres lineas: que hace la funcion mediana en este codigo y que pasa si la lista esta vacia?`n`n" + $codigo
$archivoPrompt = Join-Path $env:TEMP "prompt_paso16.txt"
$archivoSalida = Join-Path $env:TEMP "salida_paso16.txt"
$archivoError = Join-Path $env:TEMP "error_paso16.txt"
[System.IO.File]::WriteAllText($archivoPrompt, $prompt, (New-Object System.Text.UTF8Encoding($false)))

Write-Output ""
Write-Output "Comando: & '$ollama' run $modelo   (prompt por entrada estandar)"
Write-Output "PROMPT ENVIADO:"
Write-Output $prompt
Write-Output "------------------------------------------------------------"
$t0 = Get-Date
Write-Output ("Inicio de la consulta: " + $t0.ToString("yyyy-MM-dd HH:mm:ss"))
$p = Start-Process -FilePath $ollama -ArgumentList @("run", $modelo) -NoNewWindow -Wait -PassThru `
    -RedirectStandardInput $archivoPrompt -RedirectStandardOutput $archivoSalida -RedirectStandardError $archivoError
$t1 = Get-Date
$resp = [System.IO.File]::ReadAllText($archivoSalida, [System.Text.Encoding]::UTF8)
$resp = [regex]::Replace($resp, "\x1b\[[0-9;?]*[A-Za-z]", "").Replace("`r", "")
Write-Output "RESPUESTA DEL MODELO:"
Write-Output $resp.Trim()
Write-Output "------------------------------------------------------------"
Write-Output ("Codigo de salida: " + $p.ExitCode)
Write-Output ("Fin de la consulta: " + $t1.ToString("yyyy-MM-dd HH:mm:ss") + " | Tiempo: " + [math]::Round(($t1 - $t0).TotalSeconds, 1) + " s")
Write-Output ("Internet detectado durante la prueba: " + $hayInternet)
Remove-Item $archivoPrompt, $archivoSalida, $archivoError -ErrorAction SilentlyContinue

Stop-Transcript | Out-Null
Write-Host "Listo. Evidencia guardada en: $ruta"
