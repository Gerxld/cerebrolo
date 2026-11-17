#!/bin/bash
# Uso: ./ejecutar_paso.sh NN_descripcion "objetivo en una sola linea" [script.py]
# Corre el script pasando el objetivo por stdin y guarda comando, hora y salida completa.
cd "$(dirname "$0")"
script="${3:-agente_proyecto.py}"
out="evidencia/$1.txt"
{
  echo "Fecha y hora de inicio: $(date '+%Y-%m-%d %H:%M:%S')"
  echo "Directorio: $(pwd -W)"
  echo "Comando: echo \"$2\" | python $script"
  echo "------------------------------------------------------------"
  printf '%s\n' "$2" | PYTHONIOENCODING=utf-8 python -u -X utf8 "$script" 2>&1
  echo "------------------------------------------------------------"
  echo "Código de salida: $?"
  echo "Fecha y hora de fin: $(date '+%Y-%m-%d %H:%M:%S')"
} > "$out"
