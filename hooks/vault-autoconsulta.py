# UserPromptSubmit: busca en el vault notas relacionadas con el mensaje de Angel y le pasa a Claude
# las candidatas ("déjame ver si tengo apuntes de esto"). Solo punteros, no contenido: Claude decide qué abrir.
# Nunca bloquea el mensaje: ante cualquier error sale con 0 y sin salida.
import json, math, re, sys, unicodedata
from pathlib import Path

VAULT = Path(r"C:\Users\angel\Documents\Obsidian Vault")
EXCLUIR = {"_trash", ".obsidian", ".git", "templates"}
MAX_NOTAS = 5
UMBRAL = 5.0  # puntaje mínimo; ver puntuar()

STOP = set("""
para pero como este esta esto estos estas porque cuando donde entonces tambien tiene tienen tengo tenemos
hacer hace hazlo haces quiero quieres puedes puede podemos vamos sobre entre desde hasta todo toda todos
todas cosa cosas bueno whatever digamos basicamente mismo misma solo algo aqui ahora creo siento verdad
favor decir dice estar esta estan tener sido otro otra otros cada sino nada mucho poco bien igual hola
gracias dale listo osea tipo seria sera esos esas aquel ella ellos nosotros usted ustedes cual cuales
quien sabes saber mira veamos luego despues antes mejor peor manera forma parte hecho hice hizo
paso pasa pasar pasame
that this with from have what your about there would could should which their them then than
""".split())


def norm(s):
    return unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode()


def palabras(s):
    return {w for w in re.findall(r"[a-z0-9]{4,}", norm(s)) if w not in STOP}


def descripciones():
    # index.md: "- [[ruta/nota]] — descripción" → {ruta/nota: descripción}
    out = {}
    idx = VAULT / "index.md"
    if idx.exists():
        for m in re.finditer(r"^- \[\[([^\]|]+)[^\]]*\]\]\s*[—-]\s*(.+)$", idx.read_text(encoding="utf-8"), re.M):
            out[m.group(1).strip()] = m.group(2).strip()
    return out


def alias(texto):
    # "aliases:" del frontmatter (inline o en lista). Las notas nuevas van en inglés con aliases en español
    # (regla del 2026-09-25 en _CLAUDE.md): cuentan como título para que Angel las encuentre escribiendo en español.
    fm = re.match(r"---\r?\n(.*?)\r?\n---", texto, re.S)
    a = fm and re.search(r"^aliases:(.*(?:\r?\n[ \t]+-.*)*)", fm.group(1), re.M)
    return a.group(1) if a else ""


def buscar(prompt):
    claves = palabras(prompt)
    if not claves:
        return []

    desc = descripciones()
    notas = []
    for p in VAULT.rglob("*.md"):
        rel = p.relative_to(VAULT)
        if EXCLUIR & set(rel.parts) or p.name in ("index.md", "log.md"):
            continue
        clave = rel.with_suffix("").as_posix()
        d = desc.get(clave, "")
        texto = p.read_text(encoding="utf-8", errors="ignore")
        notas.append((rel, d, palabras(p.stem + " " + alias(texto)), palabras(d), palabras(texto)))

    # IDF: una palabra que aparece en casi todas las notas (angel, proyecto, claude) casi no suma.
    n = len(notas)
    df = {k: sum(k in cuerpo for *_, cuerpo in notas) for k in claves}

    def puntuar(titulo, dsc, cuerpo):
        # título pesa 3, descripción del índice 2, cuerpo 1; cada una multiplicada por lo rara que es la palabra
        s, hits = 0.0, []
        for k in claves:
            if not df[k] or df[k] > 0.4 * n:
                continue
            w = 3 if k in titulo else 2 if k in dsc else 1 if k in cuerpo else 0
            if w:
                s += w * math.log(n / df[k])
                hits.append(k)
        return s, hits

    ranking = []
    for rel, d, t, dd, c in notas:
        s, hits = puntuar(t, dd, c)
        # una palabra del mensaje en el título alcanza aunque el puntaje no llegue: con 52% de notas de Maria,
        # "retornos" no llegaba al umbral y "Realidad de los retornos" no aparecía (eval 2026-09-23).
        # Pero solo si la palabra pasó el filtro de comunes: sin eso, "qué más hace falta" traía una nota
        # por tener "falta" en el título (48% de las notas, eval 2026-09-25).
        if s >= UMBRAL or any(k in t for k in hits):
            ranking.append((s, rel, d, hits))
    ranking.sort(key=lambda x: -x[0])
    return ranking[:MAX_NOTAS]


def main():
    ranking = buscar(json.loads(sys.stdin.buffer.read().decode("utf-8")).get("prompt", ""))
    if not ranking:
        return

    lineas = ["[autoconsulta del vault] Notas que podrían tener apuntes sobre este mensaje "
              "(búsqueda por palabras). Abrir las que apliquen antes de responder; ignorar el resto."]
    for s, rel, d, hits in ranking:
        d = re.sub(r"\[\[([^\]|]+)(\|[^\]]*)?\]\]", r"\1", d)
        d = (d[:160] + "…") if len(d) > 160 else d
        lineas.append(f"- {rel.as_posix()}" + (f" — {d}" if d else "") + f" (coincide: {', '.join(sorted(hits)[:5])})")
    sys.stdout.buffer.write("\n".join(lineas).encode("utf-8"))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass  # ponytail: silencioso a propósito; un hook roto no puede frenar a Angel. Para depurar, correrlo a mano.
    sys.exit(0)
