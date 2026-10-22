---
name: project-skill-tree-audit
description: "Árbol completo de skills documentado — artifact visual + nota en Obsidian vault; 3 skills de animación instaladas (gsap-skills, design-dna, motion-design); criterio de instalación establecido"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9d831f4a-8b53-4f09-aa8f-8e904bd71ffe
  modified: 2026-07-21T23:29:36.900Z
---

Angel pidió (2026-07-20) un árbol visual de TODAS sus skills de Claude Code (locales + cloud), documentado en Obsidian, con criterio de "quedarme con lo mejor de cada una, sin que choquen". Se ejecutó en 4 pasos:

1. **Instaladas 3 skills de animación** encontradas en un post de TikTok (@rifqieh, verificado que los repos son reales antes de instalar):
   - `greensock/gsap-skills` (plugin, marketplace, 12k★, oficial de GreenSock) — 8 sub-skills
   - `zanwei/design-dna` (skill standalone en `~/.claude/skills/design-dna/`, 1.1k★) — extrae tokens de diseño de referencias visuales
   - `lottiefiles/motion-design-skill` (skill standalone en `~/.claude/skills/motion-design/`, 706★) — principios de timing/easing
   - Descartadas del mismo post: `CloudAI-X/threejs-skills` (sin caso de uso) y `AThevon/genjutsu` (redundante, 60★ vs miles)

2. **Artifact visual publicado**: árbol colapsable, dark UI inspirado en Railway/Signal (no genérico), en https://claude.ai/code/artifact/e37e972b-1184-48c2-ab43-ea30f4a380fa — 5 ramas (Plugins/Cloud/Skills sueltas/Nativas/Descartadas), leyenda de trigger type (auto-hook vs manual vs MCP vs descartada).

3. **Nota en el vault**: [[wiki/concepts/Claude Code — Stack de skills]] — versión Mermaid del árbol + tablas de detalle + el criterio de instalación de 5 preguntas (¿llena vacío? ¿choca filosóficamente? ¿es redundante? ¿hay caso de uso real? ¿la fuente es confiable?).

**Why:** Angel consume mucho contenido (YouTube, TikTok) sobre skills de Claude Code y quiere evitar instalar por instalar — pidió explícitamente un filtro de calidad, no acumulación. El criterio de 5 preguntas queda como estándar reusable para futuras skills que aparezcan en contenido que consuma.

**v2 (2026-07-20, mismo día):** Angel notó que la v1 solo cubría lo que él instaló activamente, omitiendo ~59 ítems de fábrica que aparecen en su autocomplete (comandos nativos del CLI como `/model`, `/fork`, `/rewind`, `/batch`, `/effort`, etc. + paquetes de skills sin instalar: `design:*`, `data:*`, `anthropic-skills:*`, `market-researcher:*`, utilidades sueltas). Se usó el agente `claude-code-guide` para verificar los comandos de sistema contra documentación real en vez de inventar — algunos no se pudieron confirmar (`/agents`, `/rename`, `/extra-usage`, `/__remote-workflow`, `/design-revoke`) y quedaron marcados explícitamente como no confirmados, tanto en el artifact como en la nota del vault. Artifact v2 agregó filtro por nombre y expandir/colapsar todo dado el volumen.

**How to apply:** Ante cualquier nueva skill/plugin que Angel encuentre (video, TikTok, X), aplicar el mismo criterio de 5 preguntas antes de instalar. Actualizar tanto esta memoria como la nota del vault cuando el stack cambie — son complementarias: esta memoria es para Claude Code entre sesiones, la nota del vault es la que Angel lee directamente. Ver también [[project_claude_code_dev_plugins]] (audit anterior de hooks/triggers) y [[project_tiktok_ingest]] (pipeline de descarga que se usó para leer el post de TikTok, aunque este caso fue un carrusel de fotos, no video, así que se usó descarga directa de imágenes en vez de yt-dlp).

**Evaluadas 2026-09-23 (criterio de 5 preguntas):** `last30days` (mvanhorn, 62,7k★) queda como candidata solo con OK de Angel y nunca en modo X por cookies; `deep-research` (coreyhaines31) y `Agent_Research` no se instalan. Hallazgo: las skills de investigación de obsidian-second-brain (`x-read`, `x-pulse`, `research`, `research-deep`) necesitan `XAI_API_KEY`/`PERPLEXITY_API_KEY` en `~/.config/obsidian-second-brain/.env`, que no existe: nunca funcionaron. Detalle en la nota del vault `Claude Code — Stack de skills`.
**Configurado 2026-09-23:** `.env` creado (falta que Angel pegue `XAI_API_KEY`), `VAULT_PATH` corregido en el fork local (apuntaba al vault del autor y lo creaba), `GROK_MODEL=grok-4.7`, prueba sin costo en `~/.config/obsidian-second-brain/probar_clave.py`. Perplexity descartada: su API de chat muere el 2026-09-27.

**Evaluadas 2026-10-17 (lote de 8 posts de Instagram):** nada instalado. ECC, tribunal de 12 Claudes, Ultimate Web Scraper, Impeccable/Hallmark/UI-UX Pro Max, Diagram Design, I Have ADHD y Security Audit quedan ❌. Pendientes de Angel: canario en el CLAUDE.md, last30days (más relevante desde que murió /obsidian-research) y que `claude-chat-bubbles` no figura en claude-mods.com. Tabla en la nota del vault, sección "Evaluadas el 2026-10-17".

**Segunda pasada 2026-10-17 (lo autollamable manda):** el listado de skills tiene un tope del 1% del contexto. Con 53 de 139 skills sin descripción, el de Angel ya se desborda, así que antes de sumar skills hay que liberar presupuesto. `skillOverrides` no toca las skills de plugins, y los plugins sincronizados de la app (data, design, market-researcher, animatedwebs, pdf-viewer, desktop-commander, cowork) no están en settings.json. Instalado: `court` (alexyc9381/court-skill) en ~/.claude/skills/court, con ajustes locales (python, español, premisas). Canario y firmas: `~/.claude/hooks/firmas-canario.py` + test; el registro como Stop hook en settings.json esperaba el OK de Angel.
**2026-10-17 (cierre):** Stop hook `firmas-canario.py` registrado en settings.json con OK de Angel (respaldo en ~/.claude/backups/settings.json.2026-10-17-pre-stop-hook). Los paquetes que entrega la app (data, design, market-researcher, animatedwebs, pdf-viewer, desktop-commander, cowork-plugin-management) no tienen carpeta synced ni se pueden apagar (issue anthropics/claude-code#91440); la palanca es `skillListingBudgetFraction`. Pendientes de Angel en el ANTES DE TRABAJAR del Second Brain (vault).
