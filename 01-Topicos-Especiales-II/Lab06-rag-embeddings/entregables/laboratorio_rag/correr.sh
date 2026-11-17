#!/bin/bash
# Uso: correr.sh <archivo_salida> <pregunta> [VAR=valor ...]   -- alimenta rag_universidad.py por stdin y guarda la salida completa
out="evidencia/$1"; preg="$2"; shift 2
export PYTHONIOENCODING=utf-8
{
  echo "Comando: printf '%s\nsalir\n' \"$preg\" | python -u rag_universidad.py   $*"
  echo "Hora de inicio: $(date '+%Y-%m-%d %H:%M:%S')"
  echo "----------------------------------------"
  printf '%s\nsalir\n' "$preg" | env "$@" python -u rag_universidad.py
  echo "----------------------------------------"
  echo "Hora de fin: $(date '+%Y-%m-%d %H:%M:%S')"
} > "$out" 2>&1
cat "$out"
