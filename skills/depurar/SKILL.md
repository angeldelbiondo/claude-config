---
name: depurar
description: Encontrar por qué algo falla. Usar cuando Angel dice que algo no funciona, da error, se bloqueó, se congela o microcongela, va lento, no arranca o se cae; cuando un test o un build falla; o pregunta "¿por qué pasa esto?" sobre su código, su app, su PC o Windows.
---

# Depurar

| Situación | Skill o regla |
|---|---|
| Bug de código difícil, intermitente o regresión | `diagnosing-bugs` (en prueba): primero un comando que falle con este bug, después las hipótesis |
| Error en una app web | herramientas de preview: consola, red, `read_page` |
| PC o Windows: rendimiento, drivers, GPU, procesos | diagnóstico solo de lectura primero (Get-Process, Get-CimInstance, visor de eventos) |
| Red, DNS, proxy, firewall, registro o servicios | **regla del CLAUDE.md:** mostrar el comando exacto y esperar el OK de Angel (hook `red-sistema-guard.py`) |

Método:
1. **Reproducir:** un comando o unos pasos que muestren la falla hoy. Sin eso, no hay arreglo.
2. **Hipótesis:** las que haya, ordenadas por probabilidad y costo de probarlas. Pruébalas de una en una.
3. **Si la misma prueba falla dos veces igual:** para y cambia de hipótesis. No la repitas.
4. **Arreglo:** el cambio mínimo, más un chequeo que falle si vuelve el bug.
5. **Cierre:** `verification-before-completion`. Reproduce el síntoma original y muestra que ya no aparece.

Para borrar archivos o cachés del sistema, di qué y cuánto pesa antes de borrar.
