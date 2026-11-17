#!/bin/bash
# Uso: sin_rag.sh <archivo_salida> <pregunta>  -- ollama run sin documentos (stdin cerrado, timeout 300 s)
export PYTHONIOENCODING=utf-8
OL="/c/Users/HOME/AppData/Local/Programs/Ollama/ollama.exe"
raw=$(mktemp)
ini=$(date '+%Y-%m-%d %H:%M:%S')
timeout 300 "$OL" run qwen2.5:3b "$2" < /dev/null > "$raw" 2>&1
fin=$(date '+%Y-%m-%d %H:%M:%S')
python -I limpiar_sin_rag.py "$raw" "evidencia/$1" "$2" "$ini" "$fin"
rm -f "$raw"
python -I -c "print(open('evidencia/$1',encoding='utf-8').read())"
