"""Validación manual (paso 13) de los requisitos mínimos del estándar Agent Skills."""
import re, sys, pathlib
for ruta in sys.argv[1:]:
    d = pathlib.Path(ruta); sk = d / "SKILL.md"
    texto = sk.read_text(encoding="utf-8")
    fm = re.match(r"---\n(.*?)\n---\n", texto, re.S).group(1)
    campos = dict(l.split(": ", 1) for l in fm.splitlines())
    name, desc = campos["name"], campos["description"]
    print(f"[{d.name}]")
    print(" carpeta se llama igual que name:", name == d.name)
    print(" archivo SKILL.md existe:", sk.exists())
    print(" name valido (a-z, 0-9, guiones, <=64):", bool(re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name)) and len(name) <= 64)
    print(f" description no vacia y <=1024 ({len(desc)} caracteres):", 0 < len(desc) <= 1024)
    rutas = set(re.findall(r"`((?:references|assets|scripts)/[\w./-]+)`", texto)) | set(re.findall(r"\b((?:references|assets|scripts)/[\w./-]+\.\w+)", texto))
    for r in sorted(rutas):
        print(f" ruta relativa {r} existe:", (d / r).exists())
