r"""Revisión manual (paso 23 y verificación de decisiones D3-D11 de la spec).
Se corre desde laboratorio_sdd:  python ..\entregables\evidencia\revision_manual.py
No forma parte del módulo entregado; solo muestra la lista antes y después."""
import copy, sys, os
sys.path.insert(0, os.getcwd())
from prestamos import registrar_prestamo, devolver_prestamo


def caso_negativo(titulo, lista, accion):
    print(f"--- {titulo}")
    antes = copy.deepcopy(lista)
    print("lista antes  :", lista)
    try:
        accion(lista)
        print("resultado    : NO lanzó ValueError  <-- FALLA")
        ok = False
    except ValueError as e:
        print(f"resultado    : ValueError('{e}')")
        ok = True
    except Exception as e:
        print(f"resultado    : {type(e).__name__} (no es ValueError)  <-- FALLA")
        ok = False
    print("lista después:", lista)
    intacta = lista == antes
    print("lista intacta:", intacta)
    print("VEREDICTO    :", "OK" if ok and intacta else "FALLA")
    print()
    return ok and intacta


LIMITE = int(os.environ.get("LIMITE_ACTIVOS", "3"))  # 3 en v1.0, 2 en v1.1


def base_limite():
    p = []
    for libro in "ABCDEFG"[:LIMITE]:
        registrar_prestamo(p, "Ana", libro, "2026-09-01")
    return p


print("=== PASO 23: tres casos negativos obligatorios ===\n")
res = []
p = []
registrar_prestamo(p, "Ana", "Python", "2026-09-01")
res.append(caso_negativo("1. Fecha inválida (2026-02-30)", p,
                         lambda l: registrar_prestamo(l, "Luis", "Redes", "2026-02-30")))
res.append(caso_negativo("2. Libro ya prestado (Python, otro usuario)", p,
                         lambda l: registrar_prestamo(l, "Luis", "Python", "2026-09-02")))
res.append(caso_negativo(f"3. Préstamo activo número {LIMITE + 1} de Ana (límite {LIMITE})", base_limite(),
                         lambda l: registrar_prestamo(l, "Ana", "Z", "2026-09-02")))

print("=== EXTRA: decisiones de la spec sin prueba automatizada ===\n")
extra = []
extra.append(caso_negativo("D3 formato sin ceros (2026-1-5)", [],
                           lambda l: registrar_prestamo(l, "Ana", "X", "2026-1-5")))
extra.append(caso_negativo("D3 formato compacto (20260901)", [],
                           lambda l: registrar_prestamo(l, "Ana", "X", "20260901")))
extra.append(caso_negativo("D3 fecha con espacio inicial", [],
                           lambda l: registrar_prestamo(l, "Ana", "X", " 2026-09-01")))
extra.append(caso_negativo("D3 dígitos de ancho completo", [],
                           lambda l: registrar_prestamo(l, "Ana", "X", "２０２６-09-01")))
extra.append(caso_negativo("D4 desborde (9999-12-31 + 14 días)", [],
                           lambda l: registrar_prestamo(l, "Ana", "X", "9999-12-31")))
extra.append(caso_negativo("D4 usuario no es texto (None)", [],
                           lambda l: registrar_prestamo(l, None, "X", "2026-09-01")))
extra.append(caso_negativo("D4 fecha no es texto (20260901 como int)", [],
                           lambda l: registrar_prestamo(l, "Ana", "X", 20260901)))
q = []
registrar_prestamo(q, "Ana", "Python", "2026-09-01")
extra.append(caso_negativo("D11 devolver libro activo de otro usuario", q,
                           lambda l: devolver_prestamo(l, "Luis", "Python")))
extra.append(caso_negativo("R08 devolver en lista vacía", [],
                           lambda l: devolver_prestamo(l, "Ana", "Python")))

print("=== EXTRA: comportamientos que deben ser aceptados ===\n")
pos = []
l = []
r = registrar_prestamo(l, "  Ana ", " Python  ", "2028-02-29")
c = (r["usuario"], r["libro"]) == ("Ana", "Python") and r["fecha_vencimiento"] == "2028-03-14"
print("D2 recorte + bisiesto: ", r, "->", "OK" if c else "FALLA"); pos.append(c)
c = r is l[-1]
print("D7 registrar devuelve el mismo dict (is):", "OK" if c else "FALLA"); pos.append(c)
d = devolver_prestamo(l, " Ana", "Python ")
c = d is r and d["devuelto"] is True
print("D5 devolver recorta y D7 mismo dict:", "OK" if c else "FALLA"); pos.append(c)
registrar_prestamo(l, "Luis", "Python", "2026-10-01")
c = len(l) == 2
print("D9 libro devuelto vuelve a prestarse a otro usuario:", "OK" if c else "FALLA"); pos.append(c)
registrar_prestamo(l, "ana", "Otro", "2026-10-01")
c = len(l) == 3
print("D6 'ana' distinto de 'Ana' (no cuenta en su límite):", "OK" if c else "FALLA"); pos.append(c)
registrar_prestamo([], "Ana", "X", "9999-12-17")
print("Borde 9999-12-17 aceptado: OK"); pos.append(True)

print()
tot = res + extra + pos
print(f"RESUMEN: {sum(tot)} de {len(tot)} verificaciones correctas")
