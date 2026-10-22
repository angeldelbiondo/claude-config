---
name: project-trading-algoritmico
description: Proyecto de bot de trading arrancado 2026-08-23; regla obligatoria de contrastar toda expectativa de retorno contra datos reales antes de responder
metadata: 
  node_type: memory
  type: project
  originSessionId: d26e80c9-af4b-433d-b513-2708932ccb15
  modified: 2026-08-23T21:23:22.600Z
---

Angel arrancó el **2026-08-23** el pack `wiki/projects/Trading Algorítmico/` en su vault de Obsidian: investigar end-to-end sistemas de trading públicos (código, papers, resultados) y construir un bot híbrido propio. Arranca de cero en quant — definir términos técnicos la primera vez.

Decisiones cerradas: **cripto** (no forex), **DeepSeek API + Sophia local** como motor LLM, **research antes que código**, **cero plata real hasta terminar la Fase 4 de paper trading**.

⚠️ **Regla que no se negocia:** ante cualquier expectativa de retorno — venga de Angel, de un video o de un repo — leer `wiki/projects/Trading Algorítmico/Realidad de los retornos.md` antes de responder. Los datos 2026: **15-25% ANUAL** para algo-traders experimentados. El proyecto nació de un video que reclamaba **27% MENSUAL** con una estrategia de martingala/grid (agrandar la posición perdedora), el patrón que da meses buenos hasta que revienta la cuenta.

**Why:** Angel llegó con expectativa de "20-40%" tomada de ese video. Si Claude acompaña ese número en vez de traer el dato, el proyecto entero se construye sobre una premisa falsa y Angel puede perder plata real.

**How to apply:** cuando aparezca una cifra de rentabilidad, contrastarla explícitamente contra el rango anual real y decir si es plausible. No refutar el interés en el proyecto — el proyecto es legítimo y está bien planteado; refutar solo el número. Ver también [[project-claude-video-vision]] y [[feedback-vault-source-citation]].

**Actualización 2026-08-25:** Angel declaró el objetivo real — **segunda fuente de ingresos** — y el capital: **$20, que es matrícula, no inversión** (+20% anual son $4; nunca presentar retornos como ingreso a ese capital). Restricción nueva puesta por él: **evaluabilidad** — estrategias que operan poco no se pueden validar ni mantener (el momento en oro necesitaría 204 años). Bifurcación resuelta: Camino A (ganarle a comprar y esperar) vía rotación multi-activo. Interfaz: Hermes. Metas de graduación de los $20 escritas en `El norte — segunda fuente de ingresos y qué es realista.md` del vault.

~~**Actualización 2026-09-12 — el ancla del plazo fijo** (con margen segregado el carry necesita BTC +18,3%/trimestre para empatarle a un plazo fijo panameño).~~ **RETIRADA el 2026-09-13: era un error de categoría.** Angel lo señaló: *"¿cómo vamos a competir con un plazo fijo? ... es una vergüenza para lo que hemos estado haciendo"*.

**Actualización 2026-09-13 — el ADN corregido.** Capital declarado: **menos de $1.000**. Ambición en palabras de Angel: *"apostar grandes cantidades de manera muy segura y obtener pocos porcentajes, pero esos porcentajes son bastante dinero"* — o sea riesgo bajo × apalancamiento × capital grande, que es como gana la industria.

- **Calidad y escala son dos ejes distintos.** Calidad = Sharpe del **exceso sobre la financiación** (letra a 13 semanas) cuando la estrategia inmoviliza capital, como el carry — ~~sin restar tasa libre~~ (eso vale solo para auto-financiadas) —, derrumbe, Calmar, años de historia. Escala = dólares. ~~Segregado 1,41 = unificado 1,40~~: restando la financiación, **0,65 vs 0,92** — cuando el capital cuesta, la eficiencia de capital sí es calidad.
- Calidad medida con `python -m maria.validacion.vara` (P&L real spot/perp menos letra, Sharpe mensual corregido por Lo 2002): **carry Hyperliquid 1,54 (viable), vault HLP 1,41 (viable), carry Binance 0,92 (descartar)**. Timing, transversal y multiactivo no agregaron edge. El exceso de Hyperliquid por año: 2024 +18,4%, 2026 +0,3% — cíclico; ~~hoy dormido~~ **muerto feb-may 2026 y de vuelta desde julio** (+3 a +5% sobre la letra por mes, medido 2026-09-17). La laptop cubre ~17% de las corridas del forward test: plata real exige máquina siempre prendida.
- Apalancamiento verificado: Hyperliquid portfolio margin netea pero LTV BTC 0,5 → tope 2×; préstamo USDC 5% hasta 80% de utilización, 52,5% a 90%.
- Capital: tres motores — aportes, compuesto, y **capital de terceros vía vault de Hyperliquid** (líder 10% de ganancias, historial on-chain verificable).

**Why:** medir bien y encuadrar mal produjo días de conclusiones deprimentes que no correspondían a la ambición del proyecto, y un debate de agentes que "confirmó" la premisa que yo mismo les di.

**How to apply:** nunca juzgar una estrategia market-neutral contra un depósito o tasa libre, ni reportar calidad en dólares. Al retomar Maria leer primero `ADN de Maria — la vara correcta y el mapa completo` del vault (manda sobre las demás notas), después `RUTA`. Ver [[feedback-vault-source-citation]].

**Actualización 2026-10-09 (b).** Angel decidió: regla de cierre al 2027-09-30 (`maria/validacion/cierre.py`: se cierra como proyecto de ingresos si la persona da NO VIVE y el carry no confirma) y respaldo automático diario de `user_data/` desde el recolector. Sin decisiones pendientes.

**Actualización 2026-10-09.** Chequeo a 9 días de la ventana: persona simulada ~$21,50/día (41% del sueldo, igual que letras); ventana EN CURSO sin cortes. Pendientes de Angel: regla de cierre y respaldo de la evidencia (solo en la laptop). La ventana se corre con `.venv/Scripts/python.exe`.

**Actualización 2026-09-29.** Maria en piloto automático: persona simulada con reporte diario (6 días ≈ lo mismo que letras). Angel preguntó si vale la pena; se propuso una regla de cierre al 2027-09-30 (pendiente). Entrada al retomar: ANTES → "📍 Dónde estamos" (traspaso estructurado). Preguntas recurrentes de Angel: nota `Angel's recurring questions — answered with data`.

**Actualización 2026-09-26 (c).** Angel decidió la puerta "contra 0 + tamaño" (vara.py, dcd6c2b) y aprobó la persona simulada con reporte DIARIO: corre con el recolector ($200k nocionales, 73% HLP sin rescate + 27% letras, veredicto VIVE/NO VIVE al 2027-09-30). Nota del vault: `Simulated trader — daily report`.

**Actualización 2026-09-26 (b).** Caza del clavo (nota `Hunting the nail`): sobreviven lote impar y HODLer. H28 (HLP+carry) pre-registrada en 017258a y DESCARTADA en muestra (1991f25). Con JELLY deshecho, HLP desde 2025 = Sharpe 0,72. La puerta de años de la vara mide contra 1 (HLP pide 22,9 años): decisión de Angel pendiente. Angel rechazó "el capital sale de tu trabajo": quiere proceso automático; propuesta "la persona simulada" sin aprobar.

**Actualización 2026-09-26.** Angel pidió "producto millonario" con 2 agentes. Debate + verificación: ninguna idea de vender la verificación sobrevive (existe y no vendió, lo gratis la cubre, CTA, difamación, pasarelas). El expediente contaminó el debate (2ª vez: el inventario de hechos también es premisa). Quedan 3 familias sin probar y 5 preguntas para Angel. Nota: `Maria as a product — two-agent debate and verification`.

**Actualización 2026-09-25 (b).** Ventana fuera de muestra del carry pre-registrada como código (`maria/validacion/ventana_carry.py`, commit 5162840): 2026-10-01 → 2027-09-30. Hasta el veredicto el carry es "candidato en prueba", nunca "viable". Angel puede objetar los umbrales hasta el 2026-10-01. Nota del vault (en inglés): `Carry out-of-sample window — pre-registration`.

**Actualización 2026-09-25.** El premio de mercado solo no paga sobre la letra (todo el exceso es la tasa fija del protocolo). El ADL ya está en la serie y en la vara (`carry_real.con_adl`): con el evento del 10-oct-2025 (recorte 5%, 24 h) y costos, HL 90% da 0,90 (descartar) y HL 55% 0,41; ninguna pasa auditar. Recorte con 0% da un falso 'pasa' (compra de la caída regalada).

**Actualización 2026-09-23.** Angel no gasta plata en claves de API (xAI/Perplexity): no volver a ofrecerlo. La tasa fija de Hyperliquid (0,00125%/h) no cambió nunca en 3,3 años (medido). H27 (rotación transversal de tendencia, réplica de Zarattini 2025 con 677 pares incluidas las muertas) **CERRADA: falla los 6 criterios** (Sharpe 0,49, caída −46%, −8,5% fuera de muestra). Señal real pero la rotación diaria cuesta 6%/año; sin costos Sharpe 0,67. Frente direccional cerrado con datos honestos. Variantes registradas: 198.

**Actualización 2026-09-21 — el número principal estaba mal encuadrado.** El Sharpe 1,54 del carry de Hyperliquid es la configuración de margen unificado, que exige cuenta de $10.000. La accesible con <$1.000 da 0,88-1,04 (descartar), y ninguna pasa `vara.veredicto()` por años de historia (pide 13,2, hay 3,3). Además el premio de mercado del funding es negativo desde hace 12 meses: todo el ingreso es la tasa fija del protocolo (10,95%), así que el riesgo es de gobernanza. Lo encontró un agente al que se le pidió atacar nuestra propia posición. Nota: `La auditoria adversarial — el 1,54 no era el numero de Angel`.

**Actualización 2026-09-17 — la puerta de entrada.** Al retomar Maria, leer primero `LO QUE SABEMOS — las conclusiones de Maria` en el vault (14 conclusiones con fuente), después RUTA y ANTES. Angel decidió: **todavía no invertir, sin servidor por ahora**. Seis notas de Research/YouTube estaban invisibles por tener ":" en el nombre (streams NTFS); recuperadas. Nunca ":" en nombres de archivo.
