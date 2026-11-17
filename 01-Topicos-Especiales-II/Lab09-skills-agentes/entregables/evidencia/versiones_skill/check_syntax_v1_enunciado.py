import py_compile
import sys

if len(sys.argv) != 2:
    print("Uso: python check_syntax.py <archivo.py>")
    raise SystemExit(2)

archivo = sys.argv[1]

try:
    py_compile.compile(archivo, doraise=True)
    print(f"OK: sintaxis válida en {archivo}")
except py_compile.PyCompileError as error:
    print(f"ERROR DE SINTAXIS: {error}")
    raise SystemExit(1)
