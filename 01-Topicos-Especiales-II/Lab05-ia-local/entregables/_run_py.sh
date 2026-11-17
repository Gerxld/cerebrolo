#!/bin/bash
# Uso: _run_py.sh NN_nombre script.py  (corre dentro de laboratorio_local_privado y guarda evidencia con hora y tiempo)
cd "$(dirname "$0")/laboratorio_local_privado"
out="evidencia/$1.txt"
t0=$(date +%s.%N)
{
  echo "Fecha y hora de inicio: $(date '+%Y-%m-%d %H:%M:%S')"
  echo "Directorio: $(pwd -W)"
  echo "Comando: python $2"
  echo "------------------------------------------------------------"
  PYTHONIOENCODING=utf-8 python -X utf8 "$2" 2>&1
  rc=$?
  echo "------------------------------------------------------------"
  echo "Código de salida: $rc"
  echo "Fecha y hora de fin: $(date '+%Y-%m-%d %H:%M:%S')"
  echo "Tiempo transcurrido: $(python -c "import time;print(round(time.time()-$t0,1))") s"
} > "$out"
cat "$out"
