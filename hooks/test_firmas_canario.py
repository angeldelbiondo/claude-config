# Chequeo de firmas-canario.py con transcripts sintéticos. Correr: python test_firmas_canario.py
import importlib.util, io, json, sys, tempfile
from pathlib import Path

spec = importlib.util.spec_from_file_location("fc", Path(__file__).with_name("firmas-canario.py"))
fc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fc)
tmp = Path(tempfile.mkdtemp())
fc.LOG = tmp / "canario.csv"

V = r"C:\Users\angel\Documents\Obsidian Vault"
REGLA = {"type": "attachment", "attachment": {"type": "files", "files": [{"content": "## Canario\n- " + fc.MARCA + " ..."}]}}


def prompt(t):
    return {"type": "user", "message": {"role": "user", "content": t}}


def asis(*bloques, ctx=1000):
    return {"type": "assistant", "message": {"content": list(bloques), "usage": {"input_tokens": ctx}}}


def txt(t):
    return {"type": "text", "text": t}


def tool(name, **inp):
    return {"type": "tool_use", "name": name, "input": inp}


def run(filas, sid="s1", activo=False):
    p = tmp / f"{sid}.jsonl"
    p.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in filas), encoding="utf-8")
    sys.stdin = io.TextIOWrapper(io.BytesIO(json.dumps({"transcript_path": str(p), "session_id": sid,
                                                        "stop_hook_active": activo}).encode()), encoding="utf-8")
    buf, real = io.BytesIO(), sys.stdout
    sys.stdout = io.TextIOWrapper(buf, encoding="utf-8")
    try:
        fc.main()
    finally:
        sys.stdout.flush()
        sys.stdout.detach()  # sin esto, el wrapper cierra buf al soltarlo
        sys.stdout = real
    return json.loads(buf.getvalue() or b"{}")


# turno viejo con nota sin citar: no cuenta, solo se revisa el último turno
viejo = [prompt("antes"), asis(tool("Read", file_path=V + r"\wiki\Vieja.md"), txt("Angel, ok"))]

# 1. todo en regla: canario vivo, nota citada, skill nombrada
r = run([REGLA] + viejo + [prompt("hola"), asis(txt("Angel, voy.")), asis(tool("Skill", skill="obsidian-save")),
        asis(tool("Read", file_path=V + r"\wiki\concepts\Nota Uno.md")), asis(txt("Listo. ⚙️ /obsidian-save 📓 (Nota Uno)"))])
assert r == {"systemMessage": "🧰 Este turno usé — skills: /obsidian-save"}, r

# 2. faltan firmas y el canario murió: bloquea con la línea exacta y avisa a Angel
r = run([REGLA, prompt("hola"), asis(txt("Listo, ya está.")),
         asis(tool("mcp__plugin_claude-video-vision_claude-video-vision__video_watch", path="x")),
         asis(tool("Skill", skill="ponytail:ponytail-review")),
         asis(tool("Read", file_path=V + r"\raw\videos\2026-10-17 — Lote.md")),
         asis(tool("Read", file_path=V + r"\_CLAUDE.md")),  # operativa: no se exige
         asis(txt("Fin."), ctx=50000)], sid="s2")
assert r["decision"] == "block", r
assert "⚙️ /claude-video-vision · /ponytail-review 📓 (2026-10-17 — Lote)" in r["reason"], r["reason"]
assert "Canario muerto (contexto: 50,000 tokens)" in r["systemMessage"], r
assert r["systemMessage"].endswith("🧰 Este turno usé — skills: /claude-video-vision, /ponytail-review"), r  # sale aunque bloquee

# 3. segunda muerte en la misma sesión: ya no repite el aviso (pero sí lo anota)
r = run([REGLA, prompt("otra"), asis(txt("Sin nombre."))], sid="s2")
assert r == {}, r
assert fc.LOG.read_text(encoding="utf-8").count("s2,muerto") == 2

# 4. sesión sin la regla cargada: no hay canario aunque no empiece con Angel
r = run([prompt("hola"), asis(txt("Listo."))], sid="s3")
assert r == {} and "s3" not in fc.LOG.read_text(encoding="utf-8"), r

# 5. continuación después de bloquear: no vuelve a bloquear
r = run([REGLA, prompt("hola"), asis(tool("Skill", skill="obsidian-save")), asis(txt("x"))], sid="s4", activo=True)
assert r == {}, r

# 6. subagente, workflow y skill oculta leída como archivo: van al reporte; la leída no exige firma
r = run([prompt("hola"), asis(tool("Agent", subagent_type="Explore", description="buscar hooks")),
         asis(tool("Agent", description="sin tipo")),
         asis(tool("Workflow", script="export const meta = {\n  name: 'review-changes', description: 'x' }")),
         asis(tool("Read", file_path=r"C:\Users\angel\.claude\skills\design-dna\SKILL.md")),
         asis(tool("Read", file_path=r"C:\Users\angel\.claude\commands\design-research.md")),
         asis(txt("Listo."))], sid="s6")
assert r == {"systemMessage": "🧰 Este turno usé — leídas: design-dna, design-research · subagentes: "
             "Explore (buscar hooks), general-purpose (sin tipo), workflow review-changes"}, r

print("ok: 6 casos")
