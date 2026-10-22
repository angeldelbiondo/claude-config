---
name: project-ponytail-precommit-hook
description: Hook global que bloquea el primer git commit para forzar revisión de over-engineering con ponytail
metadata: 
  node_type: memory
  type: project
  originSessionId: 4fc115ac-d159-4312-a851-68dcb2016d8b
---

Angel instaló (o está instalando) el plugin **ponytail** en Claude Code para combatir el over-engineering del vibe coding. Modo por defecto `lite` en `%APPDATA%\ponytail\config.json`.

Hay un **hook PreToolUse global** en `~/.claude/settings.json` (matcher `Bash`, script `~/.claude/hooks/ponytail-precommit.ps1`) que intercepta los `git commit` que hace Claude:
- **Primer intento de un commit → se bloquea** (deny) con instrucción de correr `/ponytail-review` y eliminar over-engineering.
- Un marcador temporal (`%TEMP%\ponytail-precommit.flag`, ventana 300s) deja pasar el **reintento** del mismo commit. No es loop ni bug.

**How to apply:** si un `git commit` se rechaza con el mensaje de ponytail, es lo esperado — correr `/ponytail-review`, aplicar la lista de borrado, y reintentar el mismo commit (esta vez pasa). Solo afecta commits hechos por Claude, no los manuales de Angel en terminal.
