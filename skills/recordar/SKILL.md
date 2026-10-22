---
name: recordar
description: Guardar o recuperar algo del vault de Obsidian (el segundo cerebro de Angel). Usar cuando Angel dice guarda, salva, anota, no quiero perder esto, registra la decisión o la sesión, retomemos, ¿qué teníamos de…?, busca en mis notas; o al cerrar un bloque de trabajo que produjo una decisión o un aprendizaje.
---

# Recordar

Para el vault se usan los comandos de esta tabla, no `desktop-commander:obsidian-vault` (es de otro plugin y no conoce las reglas de Angel).

Antes de la primera escritura de la sesión: lee `_CLAUDE.md` del vault. Para el manual completo de operación, lee `~/.claude/skills/obsidian-second-brain/SKILL.md`.

| Situación | Comando |
|---|---|
| Guardar lo valioso de la conversación | `/obsidian-save` |
| Registrar una decisión | `/obsidian-decide` |
| Registrar la sesión de trabajo | `/obsidian-log` |
| Idea al vuelo | `/obsidian-capture` |
| Tarea | `/obsidian-task` |
| Buscar en el vault | `/obsidian-find` (o Grep sobre `wiki/` y `raw/`) |
| Retomar un proyecto | su nota de conclusiones → `RUTA` → `ANTES DE TRABAJAR` |
| Resumen de un período | `/obsidian-recap` |
| Atacar una idea con el historial | `/obsidian-challenge` (está también en `decidir`) |
| Ingerir un video, artículo o link | pasa a `investigar` |
| Ordenar la memoria de Claude Code (no el vault) | `consolidate-memory` |

Reglas del vault (las completas, en `_CLAUDE.md` y en el CLAUDE.md global):
- Nunca `:` en un nombre de archivo.
- Releer después de escribir. Obsidian puede pisar en silencio lo escrito desde afuera.
- Al cerrar un bloque, actualizar `ANTES DE TRABAJAR` y `RUTA` del proyecto.
- Citar cada nota leída con `📓 (nombre)`.
