---
name: proyecto-vendinghubpty
description: "VendingHubPTY — plataforma web para invertir en máquinas expendedoras en Panamá. Stack, arquitectura, estado actual, investigación de mercado y pendientes."
metadata: 
  node_type: memory
  type: project
  updatedAt: 2026-06-07
  originSessionId: 5971d93b-092b-4fdb-b8cb-1500f6acce0f
---

**VendingHubPTY** — plataforma de inversión pasiva en máquinas expendedoras en Panamá. El inversor pone el capital; VendingHubPTY instala, repone y monitorea. El inversor ve un dashboard con ventas, stock y alertas en tiempo real.

**Carpeta local:** `C:\Desarrollo de Software\Proyectos de Software Personales\ExpendeMaquinaspty`
**Vault Obsidian (hub completo):** `wiki/projects/VendingHubPTY/VendingHubPTY.md`

---

## Stack (as of 2026-06-07)

- **Next.js 16** (App Router) + TypeScript strict + Tailwind v4 + Motion/React + GSAP 3 + lucide-react
- **Supabase** (Postgres + Auth + RLS) — backend real corriendo local vía Docker
- Estado global: `useReducer + Context` (NO Zustand) en `src/lib/store.tsx` — hidrata desde Supabase
- Acento verde esmeralda `#10b981`. Dark mode via CSS custom properties + clase `.dark` en `<html>`

---

## Estado del producto (as of 2026-06-07)

| Fase | Estado |
|---|---|
| Fase 0 — Auth + DB | ✅ hecho local |
| Fase 1 — Ciclo técnico→cliente (write central `log_visit`) | ✅ hecho local |
| Leads del wizard persistiendo (RPC `create_lead`) | ✅ hecho |
| Acciones admin (convert_lead, create_machine, tickets, facturas) | ✅ hecho |
| Onboarding real (signup crea cliente nuevo) | ✅ hecho |
| Deploy a Supabase Cloud | 🔴 pendiente |
| WhatsApp real | 🟡 pendiente (placeholder `50760000000` en `src/lib/site.ts`) |
| IoT/telemetría real | 🟡 pendiente — hoy los datos dependen del técnico |
| Página "Cómo funciona la inversión" | 🔴 pendiente (crítico para el primer inversor) |
| Split operador/inversor definido formalmente | 🟡 pendiente |

**⚠️ RECORDATORIO CRÍTICO:** La cuenta `angeldelbiondo@gmail.com` (rol admin) tiene password temporal `123456`. Cambiar ANTES de deploy a cloud.

---

## Investigación de mercado (hecha 2026-06-07)

Estudio completo en vault: `wiki/projects/VendingHubPTY/Investigación de mercado.md`

### Números reales del negocio
- Neto real por máquina/mes: **$40–$200** (no $1,600 que prometen los vendedores de humo)
- Margen neto: **15–30%** del ingreso bruto
- Ubicación explica el **70%** del resultado
- Payback realista: **18–30 meses** en buenas ubicaciones

### Modelo de negocio — referente USA: DFY Vending
- Empresa que ejecuta EXACTAMENTE el modelo de Angel (inversor pone capital, ellos operan)
- ~380 máquinas, 10 años, solo USA — LATAM libre
- Su error: overpromising ($1,600/mes). El diferenciador de Angel: ser honesto con los números
- Split típico del mercado: **65–70% inversor / 30–35% operador**

### Competencia en Panamá (investigada)
- **Vending Panamá** (20+ años, grupo GGPA), **Todo Vending** (distribuidor Nayax+MyVend), **Amas Panamá**, **Machine Company** (pide mín. 40 empleados), **Mundo Vending**
- **NINGUNA ofrece inversión pasiva.** Todas hacen comisión tradicional (el local presta el espacio, el operador pone la máquina gratis). Diferenciación de Angel intacta.
- Precios de venta en Panamá (usadas americanas): $1,750–$4,995

### Sourcing de máquinas
- **TCN (Hunan, China)** — fabricante más fiable. Combo desde ~$1,218 FOB. Certif. UL/CE/RoHS.
- Costo landed en Panamá (China directo): ~**$3,000** (incluye flete + arancel 12% + ITBMS 7%)
- **El spread:** máquinas chinas NUEVAS con cashless+IoT ~$3K vs americanas USADAS sin tech $2.7–5K
- **Nayax** (IoT/cashless) tiene distribuidor local en Panamá: Todo Vending — no hay que importar a ciegas
- Estrategia: Fase 1 comprar local o distribuidor LATAM. Fase 2+ importar directo de TCN.

### Lo más crítico para el negocio (fuera del código)
1. Primera ubicación real operando
2. Proveedor de máquinas definido
3. Pricing escrito (split + garantías)
4. Contrato legal inversor↔operador
5. Proveedor mayorista de productos en Panamá

---

## Feedback acumulado de Angel

- **No usar "Co-Authored-By: Claude"** en commits — lo pidió explícitamente
- **No tocar `settings.json` de Claude Code** sin mostrarle primero el cambio exacto — tuvo un problema donde una config rompió las respuestas
- **Respuestas cortas, tablas, bullets** — odia el relleno
- **Léxico del proyecto:** español neutro panameño (tú) en la UI/código, NO argentino (vos)
- **El vault es su memoria** — leerlo al arrancar cada sesión antes de responder

---

## Why
Angel quiere convertir esto en un negocio real en Panamá. El software es el vehículo, el negocio es la meta.

## How to apply
Priorizar lo que acerca al primer inversor real (transparencia del modelo, IoT, deploy) por encima de features de producto. Siempre leer el vault antes de responder sobre este proyecto.
