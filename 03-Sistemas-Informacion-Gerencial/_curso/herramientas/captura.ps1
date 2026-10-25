<#
Captura una ventana de escritorio a PNG con PrintWindow (funciona aunque esté tapada).

Uso:
  powershell -ExecutionPolicy Bypass -File captura.ps1 -Titulo "Dia" -Salida C:\ruta\01_dia.png
  powershell -ExecutionPolicy Bypass -File captura.ps1 -Proceso EXCEL -Salida C:\ruta\02_excel.png
  powershell -ExecutionPolicy Bypass -File captura.ps1 -Listar      # muestra ventanas visibles

-Titulo   texto que debe contener el título de la ventana (sin distinguir mayúsculas)
-Proceso  nombre del proceso (sin .exe); toma su ventana principal
-Maximizar  maximiza la ventana antes de capturar
-Pantalla   captura la zona de la ventana desde la pantalla (si PrintWindow la deja en negro)
-Escritorio trae la ventana al frente y captura el escritorio completo (p. ej. DIA con su caja de herramientas)
#>
param(
  [string]$Titulo,
  [string]$Proceso,
  [string]$Salida,
  [switch]$Maximizar,
  [switch]$Pantalla,
  [switch]$Escritorio,
  [switch]$Listar
)

Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName System.Windows.Forms
Add-Type @"
using System;
using System.Text;
using System.Runtime.InteropServices;
public class W {
  public delegate bool EnumProc(IntPtr h, IntPtr p);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc cb, IntPtr p);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int GetWindowText(IntPtr h, StringBuilder s, int n);
  [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
  [DllImport("user32.dll")] public static extern bool PrintWindow(IntPtr h, IntPtr hdc, uint f);
  [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr h, int c);
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int L, T, R, B; }
}
"@
[W]::SetProcessDPIAware() | Out-Null

function Get-Ventanas {
  $lista = New-Object System.Collections.ArrayList
  $cb = [W+EnumProc]{
    param($h, $p)
    if ([W]::IsWindowVisible($h)) {
      $sb = New-Object System.Text.StringBuilder 512
      [W]::GetWindowText($h, $sb, 512) | Out-Null
      $t = $sb.ToString()
      if ($t) {
        $procId = 0; [W]::GetWindowThreadProcessId($h, [ref]$procId) | Out-Null
        $pn = (Get-Process -Id $procId -ErrorAction SilentlyContinue).ProcessName
        [void]$lista.Add([pscustomobject]@{ Handle = $h; Titulo = $t; Proceso = $pn })
      }
    }
    return $true
  }
  [W]::EnumWindows($cb, [IntPtr]::Zero) | Out-Null
  return $lista
}

$ventanas = Get-Ventanas
if ($Listar) { $ventanas | Format-Table Proceso, Titulo -AutoSize; exit 0 }
if (-not $Salida) { throw "Falta -Salida" }

$v = $null
if ($Titulo) { $v = $ventanas | Where-Object { $_.Titulo -like "*$Titulo*" } | Select-Object -First 1 }
elseif ($Proceso) { $v = $ventanas | Where-Object { $_.Proceso -eq $Proceso } | Select-Object -First 1 }
if (-not $v) { throw "No se encontró la ventana (Titulo='$Titulo' Proceso='$Proceso'). Usa -Listar." }

$h = $v.Handle
if ($Maximizar) { [W]::ShowWindow($h, 3) | Out-Null; Start-Sleep -Milliseconds 800 }
$r = New-Object W+RECT
[W]::GetWindowRect($h, [ref]$r) | Out-Null
$w = $r.R - $r.L; $hh = $r.B - $r.T
if ($w -le 0 -or $hh -le 0) { throw "Ventana minimizada o sin tamaño" }

if ($Escritorio) {
  [W]::SetForegroundWindow($h) | Out-Null; Start-Sleep -Milliseconds 700
  $vs = [System.Windows.Forms.SystemInformation]::VirtualScreen
  $bmp = New-Object System.Drawing.Bitmap $vs.Width, $vs.Height
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.CopyFromScreen($vs.Left, $vs.Top, 0, 0, $bmp.Size)
  $g.Dispose()
} else {
$bmp = New-Object System.Drawing.Bitmap $w, $hh, ([System.Drawing.Imaging.PixelFormat]::Format32bppArgb)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.Clear([System.Drawing.Color]::Transparent)
if ($Pantalla) {
  [W]::SetForegroundWindow($h) | Out-Null; Start-Sleep -Milliseconds 600
  $g.CopyFromScreen($r.L, $r.T, 0, 0, $bmp.Size)
} else {
  $hdc = $g.GetHdc()
  [W]::PrintWindow($h, $hdc, 2) | Out-Null   # PW_RENDERFULLCONTENT
  $g.ReleaseHdc($hdc)
}
$g.Dispose()
# Apps sin soporte DPI dibujan solo una parte del bitmap: recorta lo no dibujado
$maxX = 0; $maxY = 0
for ($x = $w - 1; $x -ge 0; $x -= 2) { if ($bmp.GetPixel($x, [int]($hh / 3)).A -ne 0 -or $bmp.GetPixel($x, 20).A -ne 0) { $maxX = $x + 2; break } }
for ($y = $hh - 1; $y -ge 0; $y -= 2) { if ($bmp.GetPixel([int]($maxX / 2), $y).A -ne 0 -or $bmp.GetPixel(20, $y).A -ne 0) { $maxY = $y + 2; break } }
$maxX = [Math]::Min($w, [Math]::Max($maxX, 50)); $maxY = [Math]::Min($hh, [Math]::Max($maxY, 50))
if ($maxX -lt $w -or $maxY -lt $hh) {
  $crop = $bmp.Clone((New-Object System.Drawing.Rectangle 0, 0, $maxX, $maxY), [System.Drawing.Imaging.PixelFormat]::Format24bppRgb)
  $bmp.Dispose(); $bmp = $crop
}
}
$dir = Split-Path -Parent $Salida
if ($dir -and -not (Test-Path $dir)) { New-Item -ItemType Directory -Force $dir | Out-Null }
$bmp.Save($Salida, [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()
"OK $Salida ($w x $hh) <- [$($v.Proceso)] $($v.Titulo)"
