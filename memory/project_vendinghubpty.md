---
name: project-vendinghubpty
description: VendingHubPTY — SaaS de gestión de máquinas expendedoras en Panamá. Proyecto principal activo de Angel.
metadata:
  type: project
---

Plataforma SaaS para inversores en máquinas expendedoras en Panamá. La propuesta: el inversor pone el dinero, la plataforma opera y reporta todo.

**Ruta local:** `C:\Desarrollo de Software\Proyectos de Software Personales\ExpendeMaquinaspty`

**Stack:** Next.js 16 (App Router), TypeScript strict, Tailwind CSS v4, Supabase (Postgres + Auth + RLS), GSAP + Framer Motion, Docker (Supabase local).

**4 roles del sistema:**
- Visitante/Prospecto → completa wizard de diagnóstico → genera un Lead
- Cliente (inversor) → dashboard con sus máquinas, ingresos, stock, alertas
- Técnico → app móvil-first para registrar visitas, reposición, fallas
- Admin (Angel) → gestión global: leads, clientes, máquinas, técnicos, finanzas

**Estado a junio 2026:**
- Auth real + DB (Supabase local) ✅
- Write central del técnico (`log_visit` RPC) ✅
- Landing + wizard + dashboards shell ✅
- Persistir leads del wizard → próximo paso
- Deploy a Supabase Cloud → pendiente

**Why:** Negocio propio de Angel — combina software SaaS con operación física de máquinas en Panamá. El research de mercado es una prioridad para nutrir el sistema (catálogo, ROI calculator, copy de la landing).

**How to apply:** Cuando Angel trabaje en este proyecto, conocer el stack y el modelo de negocio para no hacer preguntas básicas. El técnico es la fuente de verdad de los datos operativos.
