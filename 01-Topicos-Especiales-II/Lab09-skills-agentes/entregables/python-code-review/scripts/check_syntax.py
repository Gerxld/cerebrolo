import os
import py_compile
import sys
import tempfile

if len(sys.argv) != 2:
    print("Uso: python check_syntax.py <archivo.py>")
    raise SystemExit(2)

archivo = sys.argv[1]

# El bytecode se escribe en una carpeta temporal para no crear __pycache__
# dentro del proyecto revisado (la revisión no debe tocar archivos).
with tempfile.TemporaryDirectory() as tmp:
    try:
        py_compile.compile(archivo, cfile=os.path.join(tmp, "check.pyc"), doraise=True)
        print(f"OK: sintaxis válida en {archivo}")
    except py_compile.PyCompileError as error:
        print(f"ERROR DE SINTAXIS: {error}")
        raise SystemExit(1)
