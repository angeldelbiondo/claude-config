---
name: project-claude-chat-bubbles
description: "Mod público angeldelbiondo/claude-chat-bubbles (fork de theme-studio, v0.1.8): dónde está, cómo publicar/actualizar y las reglas del motor de mods en escritorio"
metadata:
  node_type: memory
  type: project
  originSessionId: f88c0984-8485-443e-97e3-7730d9277c59
  modified: 2026-10-05T15:25:12.480Z
---

Mod de Claude Code, público en GitHub (`angeldelbiondo/claude-chat-bubbles`), fork de Theme Studio (Alliance Optima, MIT) hecho el 2026-10-04. Burbuja del usuario a la derecha en color rival, Claude a la izquierda, comando `/bubbles`. Angel lo quiere popular. Repo local: `C:\Desarrollo de Software\Proyectos de Software Personales\Claude Code Proyects\claude-chat-bubbles` (remotes: `origin` suyo, `upstream` allianceoptima).

**Why:** Angel quería una lectura tipo mensajería en la app de escritorio; Claude no puede ver esa pantalla, así que todo se verificó con capturas suyas y un mod de diagnóstico (borrado).

**How to apply** al tocar el mod:
- Leer `CHANGELOG.md` y `README.md` del repo antes: ahí están los modos `bubble|frame|native` y sus límites.
- Publicar: subir la versión en `chat-bubbles/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` y `package.json` (si no, `plugin update` no refresca), push, y luego `claude plugin marketplace update claude-chat-bubbles` + `claude plugin update chat-bubbles@claude-chat-bubbles`. Angel corre `/reload-plugins`.
- Usar el binario de la app (`%APPDATA%\Claude\claude-code\<versión>\<hash>\claude.exe`): el `claude` de WinGet era 2.1.161, sin mods.
- Reglas del motor (descubiertas midiendo): `next(e)` en `UserMessage` devuelve un nodo `{type:'engine'}` que NO puede estar bajo un Box con `width`, `minWidth`, `height`, `minHeight`, `overflow` ni `position` (el motor descarta el árbol sin avisar y dibuja el suyo), se dibuja UNA vez por árbol, y colapsa a ancho cero bajo un Box que se ajusta al contenido. Los tests deben simularlo con `{ type: 'engine', ref: 0 }`, no con un `Text`.
- Para ver rechazos del motor: la carpeta hot-reload de la sesión (`~/.claude/dev-mods/<session>`) los imprime en el chat como `refused: …`.
- Hook de ponytail: `git add` en una llamada, `git commit` en otra, y reintentar el mismo commit.
- Adjuntos (0.1.4): la fila nativa trae texto + imágenes/archivos y el motor la dibuja UNA vez por mensaje (aunque se llame `next` varias veces). El modo `bubble` dibuja el texto propio y la fila nativa con `text: ''` encima (solo adjuntos), SIN caja alrededor: cualquier Box que la envuelva la encoge y rompe su alineación a la derecha (imagen al centro, píldora a la izquierda; medido con capturas). Deja una píldora gris vacía (~23px, 12px bajo la imagen): se tapa subiendo la burbuja `marginTop={-4.7}` con `position="relative"` y puesta sobre una PLACA del color del lienzo (`look.canvas`): la mancha gris en la esquina superior derecha NO era la píldora pintada encima sino vista a través de la esquina redondeada transparente de la burbuja (crecía al separar la burbuja de la imagen: 5px→pequeña, 10px→grande) (unidad de margen = 16px en escritorio; -5 dejaba la burbuja a 5px de la imagen, pegada; el motor acepta decimales; `position` solo en esa rama, porque `frame` mete la fila nativa dentro del mismo Box). Qué mensajes traen adjuntos se sabe por el hook `session.append` (doors `prompt` y `command`: los comandos con barra entran por `command` y sin anotarlos mostraban una mancha gris; un prompt de texto plano llega como cadena, no como bloques), guardado en el átomo `media` (uuid→sí/no, también en `$.store`; nunca texto). `requestId` del render == `uuid` VERIFICADO en la app real (0.1.6: los comandos con barra, anotados solo por id, salieron limpios), así que se borró la clave por texto. Un mensaje nunca visto (anterior a la instalación) se deja a la app (`next(e)`); en terminal siempre es solo la burbuja.
- Tests (0.1.6): el host no tiene fondo para `session.append`, pero llamar `$.session.append(...)` y tragarse el rechazo (`.catch(() => undefined)`) basta: el hook real del mod ya anotó la fila. Así se prueba todo el camino guardar→dibujar (helper `store` en `tests/helpers.ts`). El plugin corre aislado: un módulo importado por el test es otra copia, y `$.state` no está en el `$` de los tests.
- Capturas: Angel manda capturas de la app; para comparar layouts se usó un mod de diagnóstico en la carpeta hot-reload (borrar después) con el modo de prompts del mod principal en `native` para que no se apilen.

Pendiente (2026-10-05): confirmar con captura 0.1.7 (con imagen: sin la oreja gris en la esquina de la burbuja; si el color de la placa se nota contra el fondo de la app, hacerlo configurable o usar `#141414`; historial intacto tras reiniciar). Alternativas descartadas: `Client` (código propio en la app, rompe "solo dibuja"), `Svg`/Markdown con imágenes (límites de tamaño, sin data:). Captura en el README y darlo a conocer (el topic `claude-code-mod` hace que el catálogo karanb192 lo descubra solo). Relacionado: [[project-claude-code-dev-plugins]].

**claude-mods.com (2026-10-17):** el mod no figura en el directorio. No es por fork (no lo es), ni por indexación (la búsqueda de código de GitHub encuentra `chat-bubbles/hooks/hooks.json`), ni por estructura (igual a `nateherkai/claude-code-mods`, que sí figura). Faltan también los 12 de OneWave → probablemente revisión manual del directorio, que no tiene vía de envío.
