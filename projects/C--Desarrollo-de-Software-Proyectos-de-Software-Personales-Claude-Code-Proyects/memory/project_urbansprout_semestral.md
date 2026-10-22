---
name: project-urbansprout-semestral
description: "UrbanSprout es el proyecto semestral grupal (Jack, Nico, Angel); sustentación jueves 23 de julio de 2026"
metadata: 
  node_type: memory
  type: project
  originSessionId: 6c235c2c-6950-4f7c-bba1-91ff101a9c4e
  modified: 2026-07-22T01:45:50.176Z
---

Proyecto semestral de Desarrollo de Software IX, grupo **1GS241**: Jack, Nico y Angel.
Repo de Jack (`Stelar0720/2026-1GS241-GARCIA-JACK`), carpeta `parciales/Parcial2`.
El clon local de Angel está en `Claude Code Proyects/UrbanSprout-repo` y suele quedar
atrás de `origin/main` — verificar antes de trabajar.

**Sustentación: jueves 23 de julio de 2026, en clase.** Se presenta desde la app
desplegada, no desde local.

Al 2026-07-21 quedó en 70/70 issues cerrados, 26/26 tools MCP y CI verde.

**Bloqueante abierto: el build del servicio `urbansprout-api` falla en Railway.**

Diagnóstico ya hecho (2026-07-22):
- El CLI de Railway se instalaba sin pin y la versión 5.27.1/5.27.2 salía con
  código 0 **sin subir nada** — de ahí que los deploys "pasaran" sin efecto.
  Pinneado a 5.27.0 en el workflow y con eso los frontends volvieron a desplegar.
- Con el CLI arreglado, el API sí sube pero Railway responde `Deploy failed`
  ~15 s después de `scheduling build on Metal builder`. Eso ya es del lado de
  Railway: hay que abrir el log de build del servicio en el dashboard.
- Sospecha principal: conflicto entre el *Root Directory* configurado en el
  servicio (`/parciales/Parcial2/bun-api`) y el `railway up --path-as-root` que
  ya sube esa carpeta como raíz.

Producción despliega por `git push` a la rama `production` (integración de GitHub),
**no** por `railway up`, así que ese camino puede funcionar aunque staging no.

`curl <api>/version` dice qué commit está corriendo; 404 significa código viejo.

Guion del video en `parciales/Parcial2/PRESENTACION.md`.
