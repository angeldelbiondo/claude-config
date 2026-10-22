---
name: decidir
description: Pensamiento crítico antes de decidir. Usar cuando Angel pregunta si algo es buena idea, qué propones, si vale la pena, pide conclusiones, crítica honesta, abogado del diablo o contras; cuando trae una idea, plan o número de un video; o antes de empezar algo grande con requisitos vagos.
---

# Decidir

Empieza siempre igual: escribe en 2 o 3 líneas las premisas de la pregunta. Lo que se da por cierto también se ataca.

| Situación | Skill | Costo |
|---|---|---|
| El pedido es vago ("quiero algo para…") | `interview-me` | bajo (en prueba) |
| Hay un plan o idea que afinar antes de construir | `grilling` (o `/grill-me`) | bajo (en prueba). Compite con interview-me |
| Contrastar la idea con lo que Angel ya probó | `/obsidian-challenge` | bajo |
| Decisión técnica de alto riesgo (dinero, seguridad, migración) | `doubt-driven-development` | 1 subagente por decisión (en prueba) |
| Decisión grande de negocio o de vida, con contras honestos | court: leer archivo `~/.claude/skills/court/SKILL.md` | 17 subagentes; 11 con `--quick`. Pregúntale a Angel antes |
| Después de recomendar algo que Angel va a ejecutar | `discernment-nudge` | bajo (en prueba) |

Reglas fijas:
- **Retornos, trading o "¿cuánto gano?":** lee `wiki/projects/Trading Algorítmico/Realidad de los retornos.md` antes de responder.
- **Umbrales antes que pronósticos:** responde "¿cuánto haría falta?", no "¿cuánto va a dar?".
- **Vara de comparación:** tiene que ser de la misma categoría que lo medido. Valídala con Angel.
- **Ejes separados:** calidad (%, Sharpe) y escala (dólares). Capital chico no quiere decir "no sirve".
- **Videos o terceros:** si la evidencia los contradice, dilo con el dato. No acompañes el número.
