---
name: Citar nombre de nota del vault al usarla
description: Firma del vault — toda nota leída en el turno se cita al final con `📓 (nombre-del-archivo)`; un hook de Stop la exige
type: feedback
originSessionId: 0d1eda05-a97f-4a2a-b289-c2746b3cb39e
modified: 2026-10-18T04:05:08.182Z
---
Toda nota del vault que lea en el turno se cita al final de la respuesta, en una línea `📓 (nombre-del-archivo)` (sin `.md`). Formato unificado el 2026-10-17 con la regla "Firma del vault" del CLAUDE.md global.

**Why:** Angel quiere saber qué nota se consultó para rastrearla en Obsidian. Notó (2026-10-17) que no siempre se citaba, así que ahora la exige un hook.

**How to apply:** `~/.claude/hooks/firmas-canario.py` (Stop) detecta las notas leídas con Read dentro del vault (excepto `_CLAUDE.md`, `index.md`, `log.md`, `CRITICAL_FACTS.md`, `SOUL.md`) y bloquea una vez si el nombre no aparece en el texto. Las lecturas por Bash (cat, sed) no las detecta: ahí la regla depende de mí. Relacionado: [[feedback-announce-skill-usage]].
