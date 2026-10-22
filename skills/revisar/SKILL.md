---
name: revisar
description: Revisar trabajo hecho antes de darlo por bueno. Usar cuando Angel pide revisar código o un cambio, chequear seguridad, buscar sobre-ingeniería, asegurar que funciona para una demo, hacer testing, o pregunta "¿está bien esto?" sobre algo construido.
---

# Revisar

| Qué revisar | Skill |
|---|---|
| Bugs en el diff o en un PR | `/code-review` |
| Qué se puede borrar o simplificar | `/ponytail-review` (más agresivo) o `simplify` |
| Seguridad | `/security-review`. `security-guidance` ya corre solo en cada edición |
| ¿Funciona de verdad? | `verification-before-completion` (en prueba): correrlo, no suponerlo |
| Que aguante una demo | flujo completo en el navegador integrado, o `webapp-testing` (en prueba) |
| Un diseño o una pantalla | `design:design-critique` y `design:accessibility-review` |
| Un plan o una decisión, no código | pasa a `decidir` |

Reporta los hallazgos ordenados por gravedad, con archivo y línea. Si no hay nada grave, dilo en una línea. No rellenes.
