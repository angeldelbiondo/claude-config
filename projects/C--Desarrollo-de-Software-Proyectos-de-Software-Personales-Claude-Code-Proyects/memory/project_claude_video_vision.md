---
name: project-claude-video-vision
description: "Angel instaló el plugin claude-video-vision para que Claude pueda \"ver\" videos de YouTube (frames + audio), no solo leer transcript"
metadata: 
  node_type: memory
  type: project
  originSessionId: 9d831f4a-8b53-4f09-aa8f-8e904bd71ffe
  modified: 2026-07-20T04:08:32.976Z
---

Angel instaló el plugin de Claude Code [jordanrendric/claude-video-vision](https://github.com/jordanrendric/claude-video-vision) (v1.2.0) para complementar su comando `/youtube` existente de la skill `obsidian-second-brain`, que solo extrae transcript + metadata + comments vía Grok (sin visión real del video).

**Estado de instalación (2026-07-19):**
- Plugin instalado y habilitado: `claude-video-vision@claude-video-vision`
- Backend configurado: **Gemini API** (no Whisper local — whisper-cpp no tiene instalador oficial para Windows, sin winget/choco disponible; Angel eligió Gemini como alternativa cuando se le presentó el trade-off)
- Config en `~/.claude-video-vision/config.json` — backend `gemini`, resto en default (frame_resolution 512, max_frames 100, frame_mode images)
- `GEMINI_API_KEY` seteada como variable de entorno de usuario en Windows (persistente, vía `setx`/`SetEnvironmentVariable`)
- Comando disponible tras reiniciar sesión: `/watch-video <url> "<pregunta>"`

**Why:** Angel había armado un flujo previo en Claude Chat evaluando esto porque su `/youtube` (que él pensaba que se llamaba `/ingest`) solo procesa texto — quería que Claude entienda lo visual (demos, UI, gráficos) de los videos técnicos que ingiere al vault de Obsidian.

**How to apply:** Si Angel pide "mirá este video" o quiere ingerir un video técnico con contenido visual relevante (demos, código en pantalla, UI), sugerir `/watch-video` en vez de (o además de) `/youtube`. Pendiente no resuelto: integrar el output de `/watch-video` al flujo de guardado AI-first en el vault (`Research/YouTube/`) — todavía no está conectado, solo el `/youtube` original guarda automáticamente. Ver [[project_gsap_learning]] para cómo se estructuran las notas de video en el vault.

**Arreglo 2026-10-17:** la config tenía `"backend": "gemini"`; el plugin actual espera `gemini-api` y, si no lo reconoce, cae en whisper-cli local (no instalado). Además a `@google/genai` le faltaba `ws` en `%LOCALAPPDATA%\npm-cache\_npx\f77f3cf974d7b3fb` (instalado con `npm install ws`). El servidor MCP guarda la falla de import hasta que se reinicia Claude Code. Si vuelve a fallar: ffmpeg (frames) + faster-whisper `medium` en CPU (CUDA falla por `cublas64_12.dll`). Instagram: yt-dlp baja Reels públicos sin cookies; los carruseles de fotos sin sesión solo muestran la portada.
