---
name: orquestar
description: Elige qué skills usar según lo que Angel necesita y muestra el plan antes de ejecutar. Usar cuando el pedido mezcla varias intenciones (investigar y después construir, diseñar y escribir), es grande o ambiguo, va a gastar subagentes o es difícil de deshacer, o cuando Angel dice "/orquestar", "arma un plan", "qué usarías", "cómo lo atacamos".
---

# Orquestar

Angel no tiene que acordarse de qué skill existe. Tu trabajo es elegirla, decir por qué y, cuando vale la pena, mostrar el plan antes de actuar.

## 1. Clasifica el pedido

| Intención | Señales en el pedido | Skill |
|---|---|---|
| Diseñar | pantalla, UI, landing, se ve feo, animación, diagrama, colores, referencia visual | `diseno` |
| Investigar | busca, qué dice la gente, Reddit, YouTube, video, repo, mercado, competencia, ¿existe…? | `investigar` |
| Decidir | ¿es buena idea?, qué propones, critícame, conclusiones, ¿vale la pena?, plan | `decidir` |
| Construir | implementa, crea, haz un script, agrega, conecta, app, funcionalidad, mod | `construir` |
| Depurar | error, no funciona, se bloqueó, se congela, lento, falla, ¿por qué pasa? | `depurar` |
| Revisar | revisa, ¿está bien?, seguridad, sobre-ingeniería, asegura que funcione, testing | `revisar` |
| Recordar | guarda, nota, vault, no quiero perder esto, ¿qué teníamos de…?, retomemos | `recordar` |
| Escribir | documento, Word, PPT, PDF, correo, informe, propuesta, copy, README | `escribir` |
| Datos | Excel, CSV, SQL, gráfico, dashboard, Power BI, estadística, números de Maria | `datos` |

- Una sola intención y bajo costo: carga esa skill y sigue. Basta la línea de firma.
- Si no encaja ninguna (charla, una pregunta rápida, explicar algo), responde sin skills. No fuerces una.
- Si son varias, ordénalas: casi siempre investigar o decidir va antes que construir, y revisar va al final.

## 2. Muestra el plan (preview) solo cuando hace falta

Muéstralo si se da al menos una de estas condiciones:
- Usa 2 o más skills.
- Gasta subagentes o tiempo largo: `court`, `last30days`, `doubt-driven-development`, `research`, workflows.
- Es difícil de deshacer: borrar, instalar, tocar configuración, commit o push, enviar algo.
- El pedido admite dos lecturas que llevan a trabajos distintos.

Formato:

```
🧭 Plan
- Entiendo que quieres: <una línea, en palabras de Angel>
- Voy con: <skill> (por qué) → <skill> (por qué)
- Descarté: <skill o camino>, porque <razón concreta>
- Supuestos: 1) … 2) …
- Riesgo principal: <qué puede salir mal y cómo lo vería>
→ ¿Sigo así o cambias algo?
```

Si hay una elección real entre caminos, usa AskUserQuestion con 2 o 3 opciones, la recomendada primero y con `preview` cuando ayude a comparar. Si nada es riesgoso, muestra el plan y sigue sin esperar: Angel trabaja en modo proactivo.

## 3. Pensamiento crítico (siempre, no solo en el plan)

- **Premisas:** antes de recomendar, escribe en una línea qué estás dando por cierto. Si una premisa sale del mismo Angel o de un video, pregúntate qué la invalidaría.
- **Umbrales antes que pronósticos:** responde "¿cuánto haría falta para X?" antes que "¿cuánto va a dar X?".
- **Retornos o trading:** antes de responder, lee `wiki/projects/Trading Algorítmico/Realidad de los retornos.md`.
- **No acompañes un número que la evidencia contradice.** Trae el dato.
- **Al cerrar:** `verification-before-completion` antes de decir "listo". Si la respuesta es una recomendación que Angel va a ejecutar, `discernment-nudge`.

## 4. Al ejecutar

- Antes de cada skill, una línea `⚙️ /nombre — para qué` (la exige el hook `firmas-canario.py`).
- Las skills marcadas "leer archivo" en cada intención no se llaman con la herramienta Skill: lee su `SKILL.md` con Read y síguelo. Están fuera de la lista a propósito, para liberar espacio.
- Si una skill no da el resultado esperado, dilo y propón la alternativa. No insistas con la misma.
