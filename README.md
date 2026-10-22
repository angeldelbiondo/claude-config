# claude-config

Respaldo privado de cómo está armado el Claude Code de Angel: reglas, hooks, skills y memoria. Si se pierde la máquina, con este repo y `restore.ps1` se vuelve a tener todo.

La documentación detallada (por qué se decidió cada cosa) vive en el vault de Obsidian. Esto es la versión corta.

## Qué hay

| Ruta | Qué es |
|---|---|
| `CLAUDE.md` | Reglas globales: comunicación, git, vault, verificación, canario, navegación web, ruteo de skills |
| `settings.json` | Hooks, plugins activos, statusline, output style |
| `hooks/` | Scripts que corren solos (tabla de abajo) |
| `skills/` | Skills locales: las propias, las del orquestador y las que están en prueba |
| `commands/` | Comandos `/obsidian-*` y `/design-research` |
| `skill-patches/` | Cambios locales a los dos forks de GitHub, que `restore.ps1` clona y parchea |
| `projects/*/memory/` | Memoria de Claude por proyecto (lo que recuerda entre sesiones) |
| `memory/` | Memoria vieja de agosto de 2026, guardada como historia |
| `mods-respaldo/` | Copia del mod `mi-verde` |
| `restore.ps1` | Restauración en una máquina nueva |

## Hooks

| Cuándo | Script | Qué hace |
|---|---|---|
| Al arrancar, retomar, limpiar o compactar | `vault-contexto.ps1` | Pega `CRITICAL_FACTS.md` del vault en el contexto |
| En cada mensaje | `vault-autoconsulta.py` + `ruta.py` | Busca notas del vault relacionadas, recuerda las firmas y sugiere la skill de la intención (`[ruta]`) |
| Antes de cada comando Bash | `ponytail-precommit.ps1` | Frena el primer `git commit` para correr `/ponytail-review` |
| Antes de cada comando Bash o PowerShell | `red-sistema-guard.py` | Frena cambios de red o del sistema sin aprobación |
| Al terminar cada respuesta | `firmas-canario.py` | Revisa el canario ("Angel" al inicio) y que se nombren las skills y las notas usadas. Además le muestra a Angel qué skills, skills leídas y subagentes se usaron (`🧰 Este turno usé — …`) |

## Skills: cómo se eligen

- **`orquestar`:** clasifica el pedido y, si usa varias skills, gasta subagentes o es difícil de deshacer, muestra el plan antes de actuar.
- **Nueve intenciones:** `diseno`, `investigar`, `decidir`, `construir`, `depurar`, `revisar`, `recordar`, `escribir` y `datos`. Cada una sabe qué skills específicas usar.
- **Ocultas de la lista para liberar espacio** (`disable-model-invocation: true`): design-dna, design-motion, court, marketing-research, reddit-arctic-shift, obsidian-second-brain y design-research. Se usan con `/nombre` o desde su intención.
- **En prueba hasta el 2026-11-04:** discernment-nudge, grill-me/grilling, interview-me, doubt-driven-development, frontend-design, taste-skill, diagram-design, last30days, research, diagnosing-bugs, verification-before-completion, webapp-testing, handoff, humanizer y doc-coauthoring. Las que no se usen se borran.

## Restaurar en una máquina nueva u otra PC

Guía paso a paso, pensada para que la siga una sesión de Claude Code en esa PC: **[SETUP-OTRA-PC.md](SETUP-OTRA-PC.md)**.

En corto:
1. Respaldar el `~/.claude` que ya exista.
2. Traer este repo encima, sin borrar el login.
3. Correr `restore.ps1`. Corrige las rutas si el usuario de Windows es otro, clona los forks, crea el `.env` de last30days e instala los plugins.
4. Poner el vault en `Documents\Obsidian Vault`.

Lo único que no viaja: `~/.config/obsidian-second-brain/.env`, con las claves que hagan falta. **No se versiona.**

## Bitácora

| Fecha | Cambio |
|---|---|
| 2026-08 | Primer respaldo: settings, CLAUDE.md, memoria y script de restauración |
| 2026-09-23 | CLAUDE.md global normalizado (de 250 a 81 líneas). Hooks de CRITICAL_FACTS y de autoconsulta del vault |
| 2026-09-25 | Respaldo de las skills locales y de los dos forks como patches |
| 2026-09-29 | Poda: comandos muertos fuera, statusline de ponytail |
| 2026-10 | Regla de red y sistema: mostrar el comando y esperar el OK. Hook `red-sistema-guard.py` |
| 2026-10-17 | Canario y firmas (`firmas-canario.py`), sección "Navegación web", skill `court` |
| 2026-10-21 | 15 skills en prueba por 2 semanas. Orquestador más 9 skills por intención. Línea `[ruta]` en el hook. 7 skills ocultas de la lista. La memoria por proyecto entra al repo |
| 2026-10-21 (noche) | En una sesión nueva llegaron 77 skills sin descripción. Se recortaron las descripciones de 7 skills de prueba (−3.098 caracteres) |
| 2026-10-21 (noche) | `skillListingBudgetFraction: 0.02` en `settings.json`: la lista de skills pasa del 1% al 2% del contexto. Respaldo en `backups/settings.json.2026-10-21-pre-budget` |
| 2026-10-22 | Recuento en una sesión nueva: 157 skills, 0 sin descripción. Las skills de intención resuelven los duplicados (obsidian-vault, deep-research, schedule, diagram-design) |
| 2026-10-22 | `ruta.py` ignora el texto pegado (`<pasted_content>`): un reporte pegado ya no dispara intenciones falsas |
| 2026-10-22 | `firmas-canario.py` muestra al final de cada turno qué skills y subagentes se usaron. Lo arma el hook, no Claude. Doble check de todo: 66 chequeos OK |
| 2026-10-22 | Listo para otra PC: `restore.ps1` corrige rutas, avisa si falta el vault, clona los forks solo si faltan, crea el `.env` de last30days e instala los plugins. Guía `SETUP-OTRA-PC.md`. Probado en una carpeta aparte simulando otro usuario |

## Detalle en el vault

- `wiki/concepts/Claude Code — Stack de skills.md`: inventario, criterios y evaluaciones de skills.
- `wiki/projects/Second Brain/ANTES DE TRABAJAR — estado y pendientes.md`: pendientes de esta configuración.
- `wiki/decisions/ADR-2026-09-23 — CLAUDE.md global normalizado.md`: por qué el CLAUDE.md es como es.
