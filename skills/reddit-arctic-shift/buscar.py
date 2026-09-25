"""Buscar en Reddit via Arctic Shift. Reddit directo esta bloqueado por politica.

Uso:
    python buscar.py posts <subreddit> [consulta] [limite]
    python buscar.py hilo <id_del_post> [limite_comentarios]
"""

import json
import sys

# La consola de Windows es cp1252 y los comentarios de Reddit traen unicode
# raro (espacios de ancho cero, emojis). Sin esto el script muere a mitad de
# lectura — paso tres veces en este proyecto.
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import urllib.parse
import urllib.error
import urllib.request

BASE = "https://arctic-shift.photon-reddit.com/api"


def pedir(ruta: str, **params) -> list:
    """Arctic Shift a veces responde HTTP 422 CON datos validos en el cuerpo.
    urllib trata 4xx como excepcion, asi que hay que leer el cuerpo igual."""
    url = f"{BASE}/{ruta}?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "research/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            cuerpo = r.read()
    except urllib.error.HTTPError as e:
        cuerpo = e.read()
    try:
        return json.loads(cuerpo).get("data") or []
    except json.JSONDecodeError:
        return []


def posts(sub: str, consulta: str = "", limite: int = 20) -> None:
    p = {"subreddit": sub, "limit": limite}
    if consulta:
        p["query"] = consulta
    for x in pedir("posts/search", **p):
        print(f"[{x.get('score',0):>5}pts {x.get('num_comments',0):>3}c] {x.get('id')}  "
              f"{(x.get('title') or '')[:95]}")


def hilo(post_id: str, limite: int = 60) -> None:
    """Comentarios ordenados por puntaje: lo votado suele ser lo util."""
    cs = pedir("comments/search", link_id=post_id, limit=limite)
    cs.sort(key=lambda c: c.get("score", 0), reverse=True)
    for c in cs:
        cuerpo = " ".join((c.get("body") or "").split())
        if len(cuerpo) < 40 or cuerpo in ("[removed]", "[deleted]"):
            continue   # ruido: saludos, borrados
        print(f"\n[{c.get('score',0):>4}pts] u/{c.get('author')}\n  {cuerpo[:700]}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
    elif sys.argv[1] == "posts":
        posts(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "",
              int(sys.argv[4]) if len(sys.argv) > 4 else 20)
    elif sys.argv[1] == "hilo":
        hilo(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 60)
