---
name: feedback-announce-skill-usage
description: "Firma de skills: antes de usar una skill, comando o plugin, una línea `⚙️ /nombre — para qué`; un hook de Stop la exige"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9d831f4a-8b53-4f09-aa8f-8e904bd71ffe
  modified: 2026-10-18T04:05:03.811Z
---

Antes de usar una skill (tool `Skill`), un comando slash o la herramienta de un plugin (`mcp__plugin_*`, ej. claude-video-vision), escribir una línea `⚙️ /nombre — para qué`. Formato unificado el 2026-10-17 (antes convivían `⚙️ Skill: X` y "nombrar el comando"; quedó uno solo, el del CLAUDE.md global).

**Why:** Angel quiere aprender qué skills existen y ver de un vistazo qué se dispara solo. Notó (2026-10-17) que la regla no se cumplía del todo, así que ahora la exige un hook.

**How to apply:** La regla vive en el CLAUDE.md global ("Firma de skills"). `~/.claude/hooks/firmas-canario.py` (Stop) revisa que el nombre de cada skill/plugin usado en el turno aparezca en el texto y, si falta, bloquea una vez pidiendo la línea. Los hooks 100% automáticos (security-guidance en un commit) no se anuncian, pero si se nota que corrieron, se mencionan. Relacionado: [[Citar nombre de nota del vault al usarla]].
