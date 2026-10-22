---
name: datos
description: Trabajar con datos y números. Usar cuando Angel trae un Excel, CSV o base de datos; pide SQL, un gráfico, un dashboard, estadística o un análisis; trabaja con Power BI; o pregunta por resultados, métricas o backtests de Maria.
---

# Datos

| Qué | Skill |
|---|---|
| Excel o CSV (leer, editar, crear) | `xlsx` |
| Escribir SQL (Postgres, Supabase) | `data:sql-queries` / `data:write-query` |
| Conocer una tabla nueva | `data:explore-data` |
| Significancia, outliers, correlaciones | `data:statistical-analysis` |
| Cualquier gráfico | `dataviz` antes de la primera línea; en Python, `data:create-viz` |
| Dashboard publicado | artifact tipo Dashboard (quickstart `other`) |
| Validar un análisis antes de mostrarlo | `data:validate-data` |
| Estrategias de trading de Maria | `quant-strategy-lab`, y todo resultado pasa por `auditar.py` |

Reglas del CLAUDE.md global ("Al analizar datos y números"):
- **Correlaciones:** confirmar que no sea mecánica antes de usarla como prueba.
- **Tendencias:** cortarlas en ventanas, y comparar ventanas iguales.
- **Qué reportar:** la métrica de lo que se usaría de verdad.
- **Sharpe:** corregirlo por autocorrelación (Lo, 2002). Un Sharpe mayor a 3 en un backtest es señal de bug.
- **Si el espacio completo se puede computar, no muestrear.**
