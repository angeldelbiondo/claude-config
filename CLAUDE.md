# Instrucciones globales — Angel

Aplican a todos los proyectos. Cada regla lleva su porqué en una línea. Los incidentes completos que las originaron están en el vault, en `wiki/decisions/ADR-2026-09-23 — CLAUDE.md global normalizado.md`. Leerlo solo si una regla no se entiende o parece no aplicar.

## Comunicación

- Español neutro (tú). También en el código y la UI de sus proyectos, con léxico panameño.
- Directo, sin preámbulos ni relleno.
- Tablas y bullets antes que párrafos; code blocks para lo técnico.
- Al usar una skill, nombrar el comando (`/obsidian-save`, etc.) para que Angel las vaya aprendiendo.

## Git y configuración

- Commits de git sin la línea "Co-Authored-By: Claude".
- El `git commit` va en una llamada de Bash aparte: si el hook de ponytail lo bloquea, bloquea la llamada entera y no corre nada de lo encadenado.
- Antes de tocar `~/.claude/settings.json`, mostrar qué cambia y por qué: una configuración ya rompió las respuestas una vez.
- Nunca modificar la configuración de red ni del sistema (DNS, proxy, variables `HTTP_PROXY`/`HTTPS_PROXY`, archivo `hosts`, firewall, adaptadores, `winhttp`, registro de Windows, servicios de Windows) sin mostrar antes el comando exacto y esperar la aprobación explícita de Angel: un fallo de DNS dejó a Claude Code sin conexión (`ECONNREFUSED` en el login) mientras el navegador funcionaba, y costó horas diagnosticarlo.

## Vault de Obsidian: la memoria externa de Angel

Ruta: `C:\Users\angel\Documents\Obsidian Vault\`, operado con la skill `obsidian-second-brain`. Manual de escritura (carpetas, esquemas, nombres): `_CLAUDE.md` del vault.

### Qué se lee y cuándo (de lo general a lo específico)

1. **Siempre:** un hook de SessionStart pega `CRITICAL_FACTS.md` al arrancar, al retomar una sesión, después de `/clear` y después de cada compactación. Si no ves ese bloque en el contexto, leer el archivo a mano.
2. **En cada mensaje (autoconsulta):** un hook de UserPromptSubmit busca en el vault y agrega un bloque `[autoconsulta del vault]` con las notas candidatas. Es el "déjame ver si tengo apuntes de esto": abrir las que apliquen antes de responder e ignorar las demás. El buscador es por palabras: si aparece una nota no quiere decir que sirva, y si no aparece nada no quiere decir que no haya notas.
3. **Si la autoconsulta no alcanza** (preguntas técnicas o temas que Angel ya trabajó): `index.md` → la nota que corresponda, y si no, Grep/Glob sobre `wiki/` y `raw/`. **Leer** lo encontrado antes de proponer: encontrar una nota no es leerla. Si no hay nada, responder desde conocimiento general sin mencionar la búsqueda.
4. **Al retomar un proyecto:** su nota de conclusiones → `RUTA` → `ANTES DE TRABAJAR`. En Maria están en `wiki/projects/Trading Algorítmico/`. Antes de proponer un camino nuevo, fijarse si ya está escrito ahí.

- En la primera respuesta de la sesión, una línea diciendo qué contexto se cargó.
- No consultar el vault para small talk ni comandos del sistema.
- Al responder con una nota del vault, citarla al final: `(nombre-del-archivo)`.

### Mantenerlo vivo (escribir no es usar: el ciclo se cierra leyendo)

- `ANTES DE TRABAJAR` es la única lista de pendientes de cada proyecto. Los "próximos pasos" de otras notas son historia. Al cerrar un bloque de trabajo, mover lo resuelto a ✅ o 💀.
- `RUTA` tiene la secuencia: cada fase con un criterio de salida verificable. Al cerrar un bloque, actualizar la fase. Si lista algo ya cerrado o una fase lleva semanas quieta, arreglarla o borrarla.
- "Guardá", "salvá", "no quiero perder esto" → `/obsidian-save`. Si la conversación produjo una decisión, un aprendizaje o un concepto nuevo, proponerlo antes de cerrar.

### Al escribir en el vault

- Antes de la primera escritura de la sesión, leer `_CLAUDE.md` del vault: formato AI-first, carpetas, tipos de nota y nombres.
- Nunca `:` en un nombre de archivo. En Windows crea un stream oculto: la nota queda en 0 bytes, invisible para Obsidian, y releerla por la misma ruta no lo detecta. Verificar que el `.md` aparezca en la carpeta y pese más de 0.
- Releer después de escribir. Si Obsidian tiene la nota abierta, pisa en silencio lo escrito desde afuera; un "ok" del script no prueba nada.

## Verificar antes de reportar

El patrón a evitar: reportar un resultado con entusiasmo y encontrar la falla en el turno siguiente.

- Correr la verificación en el mismo turno y pegar la salida. Si el proyecto tiene un chequeo agrupado (en Maria, `auditar.py`), usarlo.
- Si el espacio completo es computable, no muestrear.

### Al analizar datos y números

- Antes de usar una correlación como prueba, confirmar que no sea mecánica: dos medidas del mismo estadístico correlacionan solas. Probarlo con datos donde el efecto no existe.
- Reportar la métrica de lo que se usaría de verdad, no el número más impresionante del fenómeno crudo.
- Cortar las tendencias en ventanas. Si el signo o la magnitud cambian al mover el punto de arranque, la tendencia es de un subperiodo: decir cuál.
- Comparar ventanas iguales, nunca un promedio de N meses contra un valor instantáneo. "Hoy" se mide con la ventana más reciente; el año describe el año.
- Preferir "¿cuánto haría falta para X?" a "¿cuánto va a ser X?": un umbral no depende de un pronóstico.
- La vara de comparación tiene que ser de la misma categoría que lo medido, y se valida con Angel antes de sacar conclusiones con ella.
- Separar calidad (%, Sharpe: no dependen del capital) de escala (dólares). No concluir "no sirve" porque da pocos dólares sobre un capital chico.
- Corregir el Sharpe de una serie autocorrelacionada (Lo, 2002) antes de reportarlo. Un Sharpe mayor a 3 en un backtest es señal de bug.

## Agentes y orquestación

- Un panel o debate de agentes hereda las premisas de quien lo arma. Antes de lanzarlo, escribir las premisas y pedirle a un agente que ataque las premisas, no solo las conclusiones.
- Para investigar: 3 agentes como máximo, y en secuencia si comparten una API gratis. Si se puede hacer en línea, en línea.
- Si un `Workflow` muere, rescatar las transcripciones `agent-*.jsonl` antes de reintentar: reintentar igual quema lo mismo otra vez.

## Ingesta de links

- **YouTube:** `/obsidian-youtube` (transcripción). Si lo visual importa (UI, código en pantalla, diseño, animación), sumar frames con `claude-video-vision` (`video_info` → `video_analyze` → `video_watch`) a la misma nota. Sin captions: `python "C:\Users\angel\Documents\Obsidian Vault\scripts\ingest_youtube.py" "<URL>"`. No disparar `/watch-video` por una URL de YouTube: queda para archivos locales o si Angel lo pide.
- **TikTok:** `yt-dlp` a una carpeta temporal → `video_info` → `video_analyze` → `video_watch` → nota en `Research/TikTok/YYYY-MM-DD — título.md` → borrar el video. Si muestra una herramienta que Angel puede usar ya, preguntarle si se aplica al proyecto activo.
- **Artículo web:** `/obsidian-ingest` con WebFetch.
- **X/Twitter:** `/obsidian-x-read` y `/obsidian-x-pulse` no funcionan: falta `XAI_API_KEY` y Angel decidió no pagar claves (no volver a ofrecerlo). Usar WebFetch/WebSearch y avisar.
- `/obsidian-research` y `/obsidian-research-deep` dependen de la API de chat de Perplexity, que cierra el 2026-09-27.
- El crudo va a `raw/videos/YYYY-MM-DD — Título.md` (inmutable); lo destilado, a `wiki/concepts/`, `wiki/entities/` o `wiki/projects/`.

## Research previo automático

- **UI** (pantalla, componente, layout, crítica de un screenshot): correr `/design-research` antes de proponer, y leer la nota del proyecto en `wiki/projects/` si existe. Sin anunciar el research. No aplica a backend, refactor ni configuración.
- **Negocio** (mercado, competidores, cliente ideal, posicionamiento, copy): `/marketing-research`, y guardar el resultado con `/obsidian-save`.
