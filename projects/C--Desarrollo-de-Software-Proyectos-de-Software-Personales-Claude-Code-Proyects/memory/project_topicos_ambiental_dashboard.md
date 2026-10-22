---
name: project-topicos-ambiental-dashboard
description: "Dashboard Power BI del proyecto de monitoreo ambiental (Grupo 6, curso Tópicos Especiales/Gestión de la Información, UTP) — repo de Nico, Angel mejorando el .pbix"
metadata: 
  node_type: memory
  type: project
  originSessionId: 41ecdd59-f523-46e9-9283-b2382ed1f0ff
  modified: 2026-07-22T04:12:21.544Z
---

## Qué es

"Plataforma Inteligente de Monitoreo Ambiental" — Grupo 6, curso de Gestión de la
Información / Tópicos Especiales, I Semestre 2026, Universidad Tecnológica de Panamá.
Repo: https://github.com/Nicodraco/air-quality-analytics-platform (de Nico — el mismo
Nico de [[project_urbansprout_semestral]], pero este es un curso y grupo distinto,
no asumir que comparten fecha de entrega).

Arquitectura Medallion (AEMET + MITECO → Bronze JSON → Silver Parquet → Gold
PostgreSQL modelo estrella) con dashboard Streamlit, ML (Random Forest + K-Means),
alertas OMS y resúmenes LLM. Datos de España (Barcelona incluida), no Panamá.

**Angel no hizo la parte del dashboard Power BI** — está poniéndose al día y
mejorándolo, arrancó por el diseño visual.

## Modelo de datos para Power BI

Power BI NO lee las tablas físicas — solo 6 vistas semánticas `v_pbi_*` sobre
PostgreSQL (doc completa: `docs/POWER_BI.md` del repo):
- `v_pbi_fact_weather` — temperature, humidity, precipitation, wind_speed
- `v_pbi_fact_air_quality` — concentration, aqi_index, exceeds_limit (unpivoted por contaminante)
- `v_pbi_dim_date`, `v_pbi_dim_station`, `v_pbi_dim_location`, `v_pbi_dim_pollutant`

Contaminantes con límite legal (µg/m³): pm10=45, pm25=15, no2=25, so2=40, o3=100, co=4000.
Medidas DAX ya sugeridas en el doc: Avg Temperature/Humidity/Precipitation/Wind Speed,
Avg Concentration, Avg AQI, % Exceeds Limit, Readings Count Air.

## Estado del .pbix

El `.pbix` NO está versionado en el repo (binario). Angel lo tiene local en
`Downloads\dashboard_Topicos.pbix.pbix` (doble extensión porque llegó comprimido en
zip — hay que sacarle el `.zip`/segunda extensión sobrante, no descomprimirlo).

6 páginas actuales: Page 1 (4 slicers, portada/filtro), Resumen Ejecutivo (cards+línea+columnas),
Calidad del Aire (clustered column+column+línea+tabla), Clima (cards+línea+combo+columnas),
Mapa (Azure Maps), Page 2 (Esri — mapa alternativo). Los dos mapas casi seguro son
experimentación Azure vs ArcGIS (el doc del repo sugiere elegir uno, no dejar ambos).

Usaba el tema default de Power BI sin personalizar. Angel ya generó (2026-07-21) un
tema custom `Tema_Topicos_Dashboard.json` en Downloads con paleta ambiental (teal/verde/
azul + rojo/ámbar reservados para estado `exceeds_limit`/AQI), fondo gris claro,
cards con sombra/bordes redondeados — pendiente de importar y aplicar en Power BI
Desktop (Vista → Temas → Explorar temas).

## Por qué importa

**How to apply:** antes de sugerir cambios de visuales o KPIs en este dashboard,
alinear con el modelo estrella real (campos `exceeds_limit`, `aqi_index`, límites OMS
por contaminante) en vez de inventar métricas — el repo ya documenta qué medidas DAX
y qué páginas se esperan (`docs/POWER_BI.md` sección 9, "Ideas de páginas de informe").
No confundir con [[project_urbansprout_semestral]] — proyectos y entregas separadas.
