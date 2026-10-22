---
name: claude-config-repo
description: ~/.claude es el repo privado angeldelbiondo/claude-config; cada cambio de configuración va ahí con commit y una fila en la bitácora del README
metadata:
  node_type: memory
  type: project
  originSessionId: 663e45a1-0ae2-48df-998a-6acda3d8c0e2
  modified: 2026-10-22T03:18:38.967Z
---

`~/.claude` es un repo git privado: github.com/angeldelbiondo/claude-config. Respalda CLAUDE.md, settings.json, hooks, skills, commands, skill-patches y `projects/*/memory/`. Los dos forks (obsidian-second-brain y marketing-research) se restauran con `restore.ps1` y su patch.

**Why:** 2026-10-21 Angel pidió que el repo sea su respaldo ("si se me pierde algo, lo tenemos") y que además documente, en versión más básica que el vault. Estaba desactualizado tres semanas.

**How to apply:** al cambiar algo de la configuración de Claude Code, además de anotarlo en el vault ([[claude-code-stack-de-skills]]):
- Sumar una fila a la "Bitácora" de `README.md`.
- Si se tocó un fork, regenerar su patch.
- Hacer commit y push. El commit va en una llamada de Bash aparte: el primero lo frena el hook de ponytail para correr `/ponytail-review`.

Antes del commit, revisar que no entren secretos ni transcripts.
