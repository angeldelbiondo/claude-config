import importlib.util, sys
spec = importlib.util.spec_from_file_location("h", r"C:\Users\angel\.claude\hooks\vault-autoconsulta.py")
h = importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
# chequeo del parser de aliases (formato inline, en lista, y sin frontmatter)
assert "Animaciones con scroll" in h.alias("---\ndate: x\naliases: [Animaciones con scroll, animación]\ntype: concept\n---\nbody")
assert "desplazamiento" in h.alias("---\naliases:\n  - Animaciones\n  - desplazamiento\ntags: [a]\n---\n")
assert "tags" not in h.alias("---\naliases:\n  - Animaciones\ntags: [a]\n---\n")
assert h.alias("sin frontmatter") == ""
# punta a punta: nota en inglés con aliases en español, buscada con un mensaje en español
import tempfile, pathlib
with tempfile.TemporaryDirectory() as d:
    real, h.VAULT = h.VAULT, pathlib.Path(d)
    (h.VAULT / "Scroll animations.md").write_text("---\naliases: [Animaciones con desplazamiento]\n---\nHow to animate on scroll.", encoding="utf-8")
    for i in range(5):  # relleno: con 2 notas cualquier palabra está en el 50% y el filtro de comunes (40%) la descarta
        (h.VAULT / f"Otra nota {i}.md").write_text("Nada que ver.", encoding="utf-8")
    assert [x[1].name for x in h.buscar("cómo hago animaciones con desplazamiento")] == ["Scroll animations.md"]
    h.VAULT = real
print("aliases: ok")
# (mensaje, subcadenas que marcan una nota relevante — juicio mío)
SET = [
 ("cómo hago animaciones con scroll en GSAP", ["GSAP", "Kimi K3"]),
 ("qué pasó con el funding de Maria y el backtest del carry", ["carry", "funding", "Carry", "Funding"]),
 ("cómo configuro supabase con RLS para los inversionistas", ["Supabase RLS"]),
 ("sí, mueve la carpeta de marketing-research y analiza si vamos por buen camino con la narrativa que he comentado y las acciones que tomaste", ["ADR-2026-09-23", "Stack de skills"]),
 ("quiero que el second brain crezca, que sea una base de conocimientos de todo lo que aprendo, cursos, especializado en IA para agentes de código", ["AI second brain", "ADR-2026-09-23", "Second Brain/"]),  # "Second Brain/" existe desde el 2026-09-25
 ("sí, hazlo", []),
 ("que mas hace falta", []),  # 2026-09-25: traía una nota por "falta" en el título
 ("te paso un video de tiktok para guardarlo", []),
 ("cómo hago el deploy de VendingHub con supabase cloud", ["VendingHubPTY", "Supabase"]),
 ("qué retornos son realistas para un bot de trading", ["Realidad de los retornos", "El norte"]),
]
ok = ruido = falt = 0
for msg, rel in SET:
    r = [x[1].as_posix() for x in h.buscar(msg)]
    buenos = [p for p in r if any(s in p for s in rel)]
    ok += len(buenos); ruido += len(r) - len(buenos); falt += (1 if rel and not buenos else 0)
    print(f"   {len(buenos)}/{len(r)}  {msg[:55]}")
print(f"relevantes={ok}  ruido={ruido}  mensajes sin ninguna relevante={falt}")
