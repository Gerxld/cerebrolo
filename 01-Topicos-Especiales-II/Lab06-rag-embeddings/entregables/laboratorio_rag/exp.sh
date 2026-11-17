#!/bin/bash
# Uso: exp.sh <archivo_salida> <pregunta> <tamano> <k>
export PYTHONIOENCODING=utf-8
out="evidencia/$1"
{
  echo "Comando: python -u experimentos.py \"$2\" $3 $4"
  echo "Hora de inicio: $(date '+%Y-%m-%d %H:%M:%S')"
  echo "----------------------------------------"
  timeout 300 python -u experimentos.py "$2" "$3" "$4" < /dev/null
  echo "----------------------------------------"
  echo "Hora de fin: $(date '+%Y-%m-%d %H:%M:%S')"
} > "$out" 2>&1
