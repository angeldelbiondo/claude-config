---
name: Knowledge Vault — Obsidian
description: Vault local de Obsidian con notas estructuradas capturadas de videos, artículos y conversaciones. Reglas de cuándo consultarlo y skills disponibles.
type: reference
---

# Knowledge Vault — Obsidian

Vault local con conocimiento capturado de múltiples fuentes.

**Ruta:** `C:\Users\angel\Documents\Obsidian Vault\`
**CLAUDE.md del vault:** `C:\Users\angel\Documents\Obsidian Vault\CLAUDE.md`

## Cuándo consultar (NO en cada mensaje — solo cuando es relevante)

Buscar en el vault antes de responder cuando:
- Angel pregunta sobre una herramienta o tecnología específica (ej: "cómo uso Whisper", "qué es RAG")
- Angel está debuggeando un problema técnico que podría haberse visto en un video
- Angel planifica un proyecto nuevo — buscar notas de arquitectura o herramientas relevantes
- Angel dice "tengo algo guardado sobre X" o "¿vi un video de Y?" → siempre buscar
- Angel pregunta sobre HTML, CSS, JS, Python, frameworks, arquitectura, flujos de trabajo

## Cómo consultar

Usar Grep/Glob sobre `Sources/` y `Concepts/` buscando el término.
Leer las secciones `TL;DR` y `Conceptos clave` de los hits para determinar relevancia.
No pedir permiso para leer — es la memoria del usuario.

## Skills disponibles

| Skill | Cuándo usarlo |
|---|---|
| `/ingest [url]` | Angel pasa URL de YouTube o artículo para capturar |
| `/save` | Angel dice "guardá", "salvá", "no quiero perder esto" |
| `/note [texto]` | Angel dicta una idea o aprendizaje directamente |
| `/search [tema]` | Angel pide buscar explícitamente en sus notas |

## Estructura del vault

- `Inbox/` — notas rápidas sin clasificar
- `Sources/` — una nota por fuente (video, artículo, conversación)
- `Knowledge/` — síntesis temáticas permanentes
- `Concepts/` — tecnologías e ideas que aparecen en múltiples fuentes
- `scripts/ingest_youtube.py` — script de descarga y transcripción
