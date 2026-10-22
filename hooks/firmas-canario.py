# Stop: al terminar cada turno, revisa el transcript y controla tres cosas.
#  1. Canario: el primer texto del turno empieza con la palabra Angel. Si no, AVISA A ANGEL (systemMessage)
#     y lo anota con el tamaño de contexto. A Claude no se le avisa: corregirlo refrescaría la regla y mataría
#     la señal. Solo corre en sesiones cuyo CLAUDE.md ya trae la regla (si no, serían falsas alarmas).
#  2. Skills y plugins usados en el turno: su nombre tiene que aparecer en el texto (línea "⚙️ /nombre").
#  3. Notas del vault leídas con Read: su nombre tiene que aparecer en el texto (línea "📓 (nombre)").
#  Si falta 2 o 3, bloquea UNA vez para que Claude agregue la línea (stop_hook_active corta el bucle).
#  4. Reporte para Angel (systemMessage): qué skills, skills leídas como archivo y subagentes o workflows se
#     usaron en el turno. Lo arma el hook, no Claude, así que no depende de que Claude se acuerde.
# Nunca rompe: ante cualquier error sale con 0 y sin salida.
import csv, datetime, json, re, sys, unicodedata
from pathlib import Path

LOG = Path.home() / ".claude" / "hooks" / "logs" / "canario.csv"
MARCA = "Empieza cada respuesta con la palabra Angel"  # frase del CLAUDE.md que activa el canario
OPERATIVAS = {"_claude.md", "index.md", "log.md", "critical_facts.md", "soul.md"}  # no se citan


def nfc(s):
    return unicodedata.normalize("NFC", s).lower()


def es_prompt(r):
    # un mensaje real de Angel (o de la app), no un resultado de herramienta ni una nota meta
    if r.get("type") != "user" or r.get("isMeta") or r.get("isSidechain"):
        return False
    c = r.get("message", {}).get("content")
    return isinstance(c, str) or (isinstance(c, list) and not any(b.get("type") == "tool_result" for b in c))


def leer(path):
    lineas = Path(path).read_text(encoding="utf-8", errors="ignore").splitlines()
    # canario activo si algún adjunto (el CLAUDE.md cargado) trae la frase
    activo = any(MARCA in l and json.loads(l).get("type") == "attachment" for l in lineas if MARCA in l)
    turno = []
    for l in reversed(lineas):  # ponytail: solo se parsea la cola, desde el último prompt
        try:
            r = json.loads(l)
        except ValueError:
            continue
        if es_prompt(r):
            break
        if r.get("type") == "assistant" and not r.get("isSidechain"):
            turno.append(r)
    return activo, list(reversed(turno))


def main():
    data = json.loads(sys.stdin.buffer.read().decode("utf-8"))
    if data.get("stop_hook_active"):
        return  # ya bloqueamos una vez en este turno
    activo, turno = leer(data["transcript_path"])

    textos, skills, notas, leidas, agentes, contexto = [], [], [], [], [], 0
    for r in turno:
        m = r.get("message", {})
        u = m.get("usage") or {}
        if u:
            contexto = u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0) + u.get("cache_read_input_tokens", 0)
        for b in m.get("content") or []:
            if b.get("type") == "text" and b.get("text", "").strip():
                textos.append(b["text"])
            elif b.get("type") == "tool_use":
                n, inp = b.get("name", ""), b.get("input") or {}
                if n == "Skill" and inp.get("skill"):
                    skills.append(inp["skill"].split(":")[-1])
                elif n.startswith("mcp__plugin_"):
                    skills.append(n.split("__")[1].split("_")[1])  # mcp__plugin_<plugin>_<server>__<tool>
                elif n in ("Agent", "Task"):
                    tipo = inp.get("subagent_type") or "general-purpose"
                    agentes.append(f"{tipo} ({inp['description']})" if inp.get("description") else tipo)
                elif n == "Workflow":
                    m_ = re.search(r"name:\s*['\"]([^'\"]+)", str(inp.get("script", "")))
                    agentes.append("workflow " + (inp.get("name") or (m_.group(1) if m_ else "")).strip())
                elif n == "Read":
                    p = str(inp.get("file_path", ""))
                    q = p.replace("\\", "/").lower()
                    if "obsidian vault" in q and q.endswith(".md") and Path(p).name.lower() not in OPERATIVAS:
                        notas.append(Path(p).stem)
                    elif m_ := re.search(r"/\.claude/(?:skills/([^/]+)/skill\.md|commands/([^/]+)\.md)$", q):
                        leidas.append(m_.group(1) or m_.group(2))  # skills ocultas que se usan leyendo su archivo
    # ponytail: las lecturas por Bash (cat, sed) no se detectan; la regla del CLAUDE.md cubre ese caso

    texto = nfc("\n".join(textos))
    out = {}

    if activo:
        estado = "sin-texto" if not textos else ("vivo" if re.match(r"^\W*angel\b", textos[0].strip(), re.I) else "muerto")
        LOG.parent.mkdir(parents=True, exist_ok=True)
        previo = LOG.exists() and any(f"{data.get('session_id')},muerto" in l for l in LOG.read_text(encoding="utf-8").splitlines())
        nuevo = not LOG.exists()
        with LOG.open("a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if nuevo:
                w.writerow(["fecha", "contexto_tokens", "sesion", "estado"])
            w.writerow([datetime.datetime.now().isoformat(timespec="seconds"), contexto, data.get("session_id"), estado])
        if estado == "muerto" and not previo:
            out["systemMessage"] = (f"🐤 Canario muerto (contexto: {contexto:,} tokens): Claude dejó de empezar con «Angel». "
                                    "La sesión se está degradando: pide el traspaso con /obsidian-save y abre una sesión nueva.")

    unicos = lambda xs: list(dict.fromkeys(xs))
    partes = [f"{k}: {v}" for k, v in (("skills", ", ".join("/" + s for s in unicos(skills))),
                                       ("leídas", ", ".join(unicos(leidas))), ("subagentes", ", ".join(unicos(agentes)))) if v]
    if partes:  # sale en la primera pasada, aunque bloquee: la segunda (stop_hook_active) no repite nada
        reporte = "🧰 Este turno usé — " + " · ".join(partes)
        out["systemMessage"] = (out["systemMessage"] + "\n" + reporte) if "systemMessage" in out else reporte

    faltan_s = sorted({s for s in skills if nfc(s) not in texto})
    faltan_n = sorted({n for n in notas if nfc(n) not in texto})
    if faltan_s or faltan_n:
        linea = " ".join(([("⚙️ " + " · ".join("/" + s for s in faltan_s))] if faltan_s else []) +
                         ([("📓 " + " ".join(f"({n})" for n in faltan_n))] if faltan_n else []))
        out["decision"] = "block"
        out["reason"] = ("Faltan las firmas del turno (regla del CLAUDE.md). Escribe solo esta línea final, "
                         f"sin repetir la respuesta: {linea}")

    if out:
        sys.stdout.buffer.write(json.dumps(out, ensure_ascii=False).encode("utf-8"))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass  # ponytail: un hook roto no puede frenar a Angel. Para depurar: correrlo a mano con un JSON por stdin.
    sys.exit(0)
