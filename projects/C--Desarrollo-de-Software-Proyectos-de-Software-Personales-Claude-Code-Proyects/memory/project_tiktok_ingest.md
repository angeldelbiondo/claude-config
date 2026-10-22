---
name: project-tiktok-ingest
description: "Regla de ingesta de TikTok al vault de Obsidian — documentada en CLAUDE.md, dos pasos (yt-dlp descarga + claude-video-vision analiza)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9d831f4a-8b53-4f09-aa8f-8e904bd71ffe
  modified: 2026-07-21T02:17:49.482Z
---

Angel pidió (2026-07-20) una skill tipo `/youtube` pero para TikTok, para contenido de software que encuentra ahí y quiere guardar/aplicar. Se verificó en el código fuente de `claude-video-vision` (`video-source.ts:408-410`) que el plugin **bloquea explícitamente** URLs no-YouTube con un `throw new Error`. No hace falta instalar nada nuevo — `yt-dlp` (ya instalado, ver [[project_claude_code_dev_plugins]]) soporta TikTok nativamente.

**Flujo documentado en CLAUDE.md global** (sección "Ingestión automática"):
1. `yt-dlp <url>` descarga el TikTok a local
2. `video_info` → `video_analyze` → `video_watch` (mismas tools de claude-video-vision, backend Gemini) sobre el archivo local
3. Nota AI-first guardada en `Research/TikTok/` (separada de `Research/YouTube/` — metadata distinta: autor/likes vs canal/views)
4. Borrar el video descargado después de procesar

**Why:** TikTok no tiene equivalente a `youtube-transcript-api` — siempre requiere el pipeline de visión completo (Gemini), no hay atajo de solo-texto. Angel usa TikTok para descubrir contenido de software que quiere aprender o aplicar YA, no solo archivar — por eso la regla incluye señalar explícitamente si algo es aplicable de inmediato al proyecto activo, en vez de solo guardarlo pasivamente.

**How to apply:** ante cualquier link de tiktok.com o vm.tiktok.com, seguir el flujo de dos pasos. No intentar pasarle la URL directo a las tools de `claude-video-vision` — va a fallar, hay que descargar primero.
