---
name: construir
description: Escribir código o armar algo que funcione. Usar cuando Angel pide implementar, crear, agregar una funcionalidad, hacer un script, conectar una API, montar una app o un MVP, crear un mod de Claude, o "haz eso" después de un plan.
---

# Construir

ponytail ya está activo por hook: lo mínimo que funcione y un chequeo ejecutable.

| Situación | Skill |
|---|---|
| Requisitos vagos | pasa antes por `decidir` (interview-me o grilling) |
| Hay UI de por medio | pasa antes por `diseno` |
| App con la API de Claude o el SDK | `claude-api` |
| Un mod de Claude (panel, hook, comando) | `plugin-authoring` |
| Levantar la app para ver el cambio | `run` (y las herramientas de preview) |
| Documentación de una librería | Context7 (`mcp__context7__*`) |
| Probar una web local con scripts que se repitan | `webapp-testing` (en prueba); para mirar una vez, el navegador integrado |
| Algo recurrente o programado | `loop` / `schedule` |
| Trabajo largo que no entra en una sesión | `handoff` (`/handoff`) o `/obsidian-save` al cerrar |

Antes de decir "listo":
- `verification-before-completion`: corre el chequeo y pega la salida. En Maria, `auditar.py`.
- Si la tarea creció en el camino, di qué quedó afuera.
- El commit va en una llamada de Bash aparte. El primero lo frena a propósito el hook de ponytail.
