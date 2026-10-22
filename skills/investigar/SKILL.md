---
name: investigar
description: Buscar y traer información. Usar cuando Angel pide investigar, buscar cómo lo haría un profesional, saber qué dice la gente, leer Reddit o foros, ver un video de YouTube o TikTok, revisar un repo o artículo, entender un mercado o la competencia, o cuando la respuesta puede estar desactualizada (precios, versiones, noticias).
---

# Investigar

| Situación | Skill | Cómo |
|---|---|---|
| Qué dice la gente de un tema en los últimos 30 días | `last30days` | Skill (en prueba). Nunca aceptes leer cookies; no ofrezcas ScrapeCreators |
| Hilos o comentarios de Reddit | reddit-arctic-shift | leer archivo `~/.claude/skills/reddit-arctic-shift/SKILL.md` |
| Video de YouTube | `/obsidian-youtube` | Skill (comando). Si lo visual importa, suma `claude-video-vision` |
| TikTok o video local | `claude-video-vision:watch-video` | Skill. Flujo en el CLAUDE.md global, "Ingesta de links" |
| Artículo web para guardar | `/obsidian-ingest` | Skill (comando) |
| Docs de una librería o API | Context7 (MCP) | herramientas `mcp__context7__*` |
| Dato técnico que hay que citar (spec, doc oficial) | `research` | Skill (en prueba). Compite con last30days: esta es para fuentes primarias |
| Mercado, competidores, cliente ideal, posicionamiento, copy | marketing-research | leer archivo `~/.claude/skills/marketing-research/SKILL.md`; guardar el resultado con `/obsidian-save` |
| Sector o empresas que cotizan en bolsa | `market-researcher:sector-overview`, `competitive-analysis` | Skill |
| Algo que puede haber cambiado en el último año | WebSearch | herramienta |
| Investigación profunda con varios agentes | `anthropic-skills:deep-research` | Solo si Angel lo pide: lanza subagentes. Regla del CLAUDE.md: 3 agentes como máximo, y en secuencia si comparten una API gratis |

Reglas:
- Para elegir entre WebFetch, el navegador integrado o un script, sigue la sección "Navegación web" del CLAUDE.md global.
- Una afirmación que cambia una decisión necesita dos fuentes independientes.
- Al terminar, relee el pedido y di qué parte quedó sin cubrir.
- Si lo encontrado vale la pena, ofrece `/obsidian-save`.
