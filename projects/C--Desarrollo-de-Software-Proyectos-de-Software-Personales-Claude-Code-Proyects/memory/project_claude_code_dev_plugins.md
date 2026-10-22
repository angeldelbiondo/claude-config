---
name: project-claude-code-dev-plugins
description: "Plugins y MCP servers instalados en Claude Code de Angel para desarrollo (TypeScript LSP, Security Guidance, Context7) — evitar reinstalar o recomendar de nuevo"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9d831f4a-8b53-4f09-aa8f-8e904bd71ffe
  modified: 2026-07-20T04:44:51.012Z
---

Angel instaló estos plugins/MCP servers en Claude Code (2026-07-19), a partir de un ranking de skills vistas en un video de YouTube analizado con [[project_claude_video_vision]]:

- **`security-guidance@claude-plugins-official`** (v2.0.6) — linter de seguridad en tiempo real (inyección, auth, OWASP Top 10), corre automático en cada Write/Edit y en git commit. Instalado porque VendingHubPTY maneja plata real de inversores + RLS multi-tenant.
- **`typescript-lsp@claude-plugins-official`** (v1.0.0) — LSP real para TypeScript/JS (go-to-definition, find references, type errors en vivo). Directo a su stack Next.js 16 + Supabase. REQUIERE el binario global `typescript-language-server` + `typescript` (instalado vía `npm i -g` el 2026-07-19 — sin eso el plugin es cáscara vacía). Habilita el LSP tool nativo de Claude Code, se usa automático al navegar/editar TS.
- **`context7`** — MCP server (`npx -y @upstash/context7-mcp`, scope user, sin API key todavía → rate limit básico). Da docs live de librerías en vez de depender del conocimiento entrenado, útil para Next.js 16 / Tailwind v4 que son versiones nuevas.

**Marketplaces agregados:** `claude-video-vision`, `anthropic-agent-skills` (`anthropics/skills` — no tenía lo que buscaba), `claude-plugins-official` (`anthropics/claude-plugins-official` — acá SÍ estaban security-guidance y typescript-lsp).

**Why:** el video rankeaba 12 skills por instalaciones pero mezclaba links mal (decía que security-guidance y typescript-lsp estaban en `anthropics/skills`, en realidad están en `anthropics/claude-plugins-official`). Se verificó cada repo antes de instalar en vez de confiar en los links del video.

**Descartadas explícitamente** (no volver a sugerir salvo que cambie el contexto): Frontend Design (se pisa con `/design-research` propio de Angel), Code Simplifier (redundante con `ponytail` ya instalado), Claude.md Management (Angel gestiona su CLAUDE.md a mano), Superpowers (choca filosóficamente con `ponytail`/YAGNI).

**How to apply:** si Angel pregunta por security/types/docs de librerías en cualquier proyecto TS, ya tiene las herramientas activas — no reinstalar. Si Context7 empieza a rate-limitear, ofrecer agregar `--api-key` (gratis en context7.com/dashboard).

**Cómo se dispara cada uno (verificado leyendo hooks/skills reales):**
- `ponytail` → SessionStart hook, modo persistente (activo toda la sesión)
- `security-guidance` → 100% hooks automáticos (SessionStart, UserPromptSubmit, PostToolUse en Edit/Write/MultiEdit, y en Bash git commit/push). Corre un LLM call (Opus por defecto) en cada Stop y cada commit vía `asyncRewake` → me re-despierta con findings. NO tiene slash command. Costo/latencia real en cada commit.
- `typescript-lsp` → habilita el LSP tool nativo, uso automático al tocar TS
- `context7` → MCP server, YO llamo sus tools (`resolve-library-id`, `get-library-docs`) según juicio cuando necesito docs de librería
- `claude-video-vision` → skill `video-perception` auto-triggerable ante URL de YouTube/archivo de video + comando `/watch-video`

**COLISIÓN DE TRIGGER — RESUELTA (2026-07-19):** ante una URL de YouTube se disparaban DOS cosas (`/youtube` transcript+vault vs skill `video-perception` frames+audio, sin guardar). Angel decidió **unificar todo bajo `/youtube`** — es el punto de entrada ÚNICO para URLs de YouTube. Se documentó en el CLAUDE.md global (sección "Ingestión automática"): `/youtube` por default saca transcript y guarda al vault; si el contenido es VISUAL (demo UI, código en pantalla, diseño, animación) escala dentro del mismo flujo capturando frames con las tools de claude-video-vision (`video_info`→`video_analyze`→`video_watch`) e incorpora la visión a la MISMA nota. `/watch-video` y la skill `video-perception` NO deben auto-dispararse por URLs de YouTube — quedan reservadas para archivos de video locales (.mp4 etc.) o pedido explícito "mirá este video".
