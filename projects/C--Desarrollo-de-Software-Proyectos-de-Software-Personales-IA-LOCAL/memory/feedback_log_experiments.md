---
name: feedback-log-experiments
description: "Angel wants every hands-on experiment/test result logged in project docs, not just planned or remembered informally"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0d4a5453-a762-42a3-84fc-45732760fb73
---

Log every real experiment (model test, install step, benchmark) in the project's documentation as it happens — result, numbers, and conclusion — not just the plan. Never re-run a test whose result is already documented; check the log first.

**Why:** Angel confirmed this explicitly on 2026-06-30 while building [[project-ia-local-sophia]]: "Recuerda, por supuesto, ir como que guardando el histórico de estos experimentos para, por supuesto, no volverlo a repetir." He was pointing at the pattern already in use in `documentation/brain_storming.md` — a running "Log de instalación" / experiment table with real numbers (e.g., timing comparisons between model configs) — and asked for it to continue. This is his working style, not a one-off request.

**How to apply:** Whenever a hands-on test produces a real result (timing, success/fail, a config that worked or didn't) in any project, write it into that project's documentation immediately, with enough detail (exact numbers, exact config) that neither Angel nor a future Claude session would need to re-run it to know the outcome. Applies beyond IA LOCAL — general collaboration preference.

**Reinforced 2026-07-06:** Angel widened this explicitly — "todo lo que hagas, ve documentándolo donde sea pertinente, y recuérdate también de consultar ahí". Two-way rule: (1) document EVERYTHING (not just experiments — decisions, builds, findings) in the pertinent project doc as it happens; (2) CONSULT those docs before acting — check the experiment log before re-running anything, check decision records before re-deciding.
