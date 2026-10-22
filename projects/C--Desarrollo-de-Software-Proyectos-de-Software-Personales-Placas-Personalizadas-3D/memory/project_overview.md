---
name: PlacasPTY project overview
description: Stack, file structure, design tokens, and current build state for placaspty.com
type: project
originSessionId: e845170f-9c24-4fd4-9700-043d7e3af5e1
---
## For future Claude
Landing page for placaspty.com — custom 3D license plates in Panama. Full Next.js web app located at `web/` inside the working directory. The dev server runs on localhost:3000.

## Current state (as of 2026-05-06)
Landing page is built and running. All sections are done. The editor (the actual plate customizer) is NOT built yet — the `#editor` anchor just scrolls to the CTA section.

**Why:** Landing page was prioritized as v1 to establish brand presence before building the editor.
**How to apply:** When picking up work, focus on building the actual 3D editor next. It will live at `/editor` route.

## Stack
- Next.js (App Router, Turbopack dev)
- React 19 (Strict Mode disabled via `reactStrictMode: false` in next.config.ts)
- Tailwind CSS v4 (config via `@theme` in globals.css — NO tailwind.config.ts)
- GSAP 3.15 + @gsap/react + ScrollTrigger, ScrollToPlugin, Observer, Flip
- React Three Fiber + @react-three/drei (Canvas, OrbitControls, Environment, ContactShadows, RoundedBox)
- Three.js (CanvasTexture, meshPhysicalMaterial)

## Design tokens (globals.css)
- `--color-ink: #0A0A0A` (dark background)
- `--color-paper: #FAFAFA` (light text/elements)
- `--color-signal: #E8FF00` (yellow accent — the brand color)
- `--font-display`: Barlow Condensed (variable `--font-space-grotesk` kept for Tailwind compat)
- `--font-body`: Inter
- `--font-mono`: JetBrains Mono

## File structure (key files)
```
web/src/
  app/
    layout.tsx      — Root layout with fonts + GSAPProvider
    page.tsx        — Assembles all sections
    globals.css     — Tailwind theme + keyframes (heroWordReveal etc.)
  components/
    layout/
      Nav.tsx       — Fixed nav, scroll-aware, hamburger on mobile, GSAP smooth scroll
      GSAPProvider.tsx — Client boundary that imports lib/gsap to register plugins
    sections/
      Hero.tsx      — CSS entrance animations (words clip-reveal, overlay wipe)
      Marquee.tsx   — GSAP infinite scroll marquee
      HowItWorks.tsx — 3-step process, GSAP scroll reveals
      Features.tsx  — 6-card grid, scroll stagger (id="galeria")
      CTASection.tsx — Big CTA with decorative "3D" text (id="editor")
      Footer.tsx    — 3-col links + copyright
    three/
      PlateScene.tsx — R3F Canvas wrapper, camera, lights, OrbitControls
      PlateModel.tsx — Plate mesh with canvas texture, auto-rotation, float
    ui/
      Button.tsx    — Primary/secondary/ghost variants, rounded-none brutalism
      Cursor.tsx    — GSAP magnetic cursor dot + ring
  lib/
    gsap.ts         — Central plugin registration (ScrollTrigger, ScrollToPlugin, etc.)
    utils.ts        — cn() with clsx + tailwind-merge
```

## Section IDs
- Hero: no ID (no nav link)
- `#como-funciona` → HowItWorks
- `#galeria` → Features
- `#editor` → CTASection (placeholder until real editor is built)
