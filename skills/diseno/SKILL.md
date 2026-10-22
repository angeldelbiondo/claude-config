---
name: diseno
description: Todo lo visual. Usar cuando Angel pide diseñar o mejorar una pantalla, UI, landing, componente, página o artifact; dice que algo se ve feo, genérico o "hecho por IA"; trae una referencia visual (imagen, URL, screenshot); o pide animaciones, colores, tipografía o diagramas.
---

# Diseñar

Elige según la situación. Puedes combinar varias, en este orden.

| Situación | Skill | Cómo |
|---|---|---|
| Antes de proponer cualquier UI nueva (regla de Angel) | design-research | leer archivo `~/.claude/commands/design-research.md` |
| Si el proyecto tiene nota en el vault (`wiki/projects/`) | — | leerla antes de proponer |
| Angel trae una imagen, URL o screenshot de referencia | design-dna | leer archivo `~/.claude/skills/design-dna/SKILL.md` |
| Dirección estética de una app, pantalla o dashboard | `frontend-design` | Skill (en prueba hasta el 2026-11-04) |
| Landing, sitio de marketing o portafolio que tiene que lucir | `design-taste-frontend` (taste-skill) | Skill (en prueba). Compite con frontend-design: usa una sola |
| Animación: timing, easing, coreografía | design-motion | leer archivo `~/.claude/skills/design-motion/SKILL.md` |
| Animación con GSAP | `gsap-skills:gsap-core`, `gsap-timeline`, `gsap-scrolltrigger`, `gsap-react`… | Skill por nombre |
| Criticar un diseño o un screenshot | `design:design-critique` | Skill |
| Accesibilidad (WCAG) | `design:accessibility-review` | Skill |
| Textos de botones, errores, estados vacíos | `design:ux-copy` | Skill |
| Spec para pasarle a otro dev | `design:design-handoff` | Skill |
| Diagrama para entender algo | `artifact-diagramming` | Skill (nativa) |
| Diagrama para mostrarle a otros (sustentación, inversor) | `diagram-design` | Skill (en prueba) |
| Página publicada como artifact | `artifact-design` | Skill (nativa) |

Si en la misma tarea hay que escribir el código, pasa después a `construir`.
