---
name: feedback-avoid-trial-error
description: "Angel quiere que razone y batchee cambios, no iterar en vivo con ensayo-error"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9a90e921-3361-40c9-8eb2-86f496cf6553
---

Evitar el ciclo de ensayo-error en la mayoría de los casos. En vez de editar → reiniciar server → verificar → encontrar un problema → re-editar → reiniciar (una y otra vez), razonar el cambio completo de antemano (diseño, edge cases, valores), hacer todas las ediciones relacionadas en UNA pasada deliberada, y verificar una sola vez.

**Why:** Angel notó que el loop de prueba-y-error es ineficiente y poco pulido — pidió "evitemos el ensayo error en su mayoría de casos".

**How to apply:** pensar antes de tocar código (leer las zonas exactas, decidir valores/curvas/estructura de una); batchear ediciones; correr una sola verificación al final en lugar de varias intermedias. Aplica sobre todo al trabajo en Sophia ([[project_ia_local_sophia]]) donde cada verificación implica reiniciar el server. Nota práctica: el screenshot del preview se cuelga con el orb WebGL — verificar por DOM/estilos computados, no por captura.
