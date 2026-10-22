---
name: feedback-herramientas-propias-primero
description: "Antes de proponerle a Angel gastar plata o infraestructura externa, revisar qué puede hacer Claude Code con lo que ya tiene (rutinas en la nube, skills instaladas)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b0def374-0290-49fa-9ba3-56d81e89f195
  modified: 2026-09-24T03:01:21.283Z
---

Antes de proponer una solución que cuesta plata o infraestructura externa (VPS, claves de API pagas), revisar primero lo que ya existe en el stack de Claude Code: rutinas en la nube (`/schedule`), skills instaladas, herramientas del plan.

**Why:** El 2026-09-17 detecté que la laptop no sirve como servidor para el forward test de Maria y propuse alquilar un VPS; Angel lo rechazó por costo. Recién el 2026-09-23 él mismo preguntó si no se podía con las rutinas en la nube de Claude, y sí se podía. Dijo: "me hubiera gustado que me hubieras propuesto eso antes". Angel no gasta plata en infraestructura ni claves (decisión 2026-09-23).

**How to apply:** Ante cualquier necesidad de "algo que corra siempre", "una API", "un servidor": primero listar qué cubre el plan actual (rutinas en la nube, WebSearch/WebFetch, skills), y solo después, si no alcanza, mencionar opciones pagas. Relacionado: [[project-trading-algoritmico]].
