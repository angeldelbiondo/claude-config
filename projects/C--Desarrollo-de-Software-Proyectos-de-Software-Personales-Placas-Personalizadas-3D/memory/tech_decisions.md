---
name: PlacasPTY tech decisions
description: Key architectural and tooling decisions made during the build
type: project
originSessionId: e845170f-9c24-4fd4-9700-043d7e3af5e1
---
## For future Claude
These are non-obvious decisions with important reasons — don't change them without understanding the why.

## Barlow Condensed instead of Space Grotesk
Space Grotesk maxes at weight 700 — not heavy enough for the brutalist headline style needed.
Barlow Condensed supports 900 (Black) which is the correct weight for the big DISEÑÁ/ROTÁ/RECIBÍ words.
The CSS variable is named `--font-space-grotesk` for backward compat with Tailwind classes.

## CSS animations for Hero entrance, NOT GSAP
**Why:** React Strict Mode double-mounts components in dev. GSAP timelines in useEffect get killed by the cleanup on the first mount, then restart on remount — causing the animation to fail. CSS animations are browser-native and unaffected by React lifecycle.
**How to apply:** Keep hero entrance animations (`heroWordReveal`, `heroFadeUp`, `heroScaleIn`, etc.) as CSS. GSAP is fine for scroll-triggered and event-driven animations (Nav smooth scroll, Marquee, HowItWorks, Features scroll reveals).

## reactStrictMode: false (next.config.ts)
Set because Strict Mode's double-mount was causing GSAP timeline issues. Even with CSS animations for entrance, keep this off for cleaner dev behavior.

## GSAP plugin registration in lib/gsap.ts
All GSAP plugins registered in one place (`lib/gsap.ts`). `GSAPProvider` just imports this file to ensure it runs client-side. Never import GSAP plugins directly in components — always use `@/lib/gsap`.

## Plate texture via Canvas API (not images)
The 3D plate texture is generated programmatically via `buildPlateTexture()` in PlateModel.tsx.
**Why:** Avoids hosting image assets, allows future dynamic customization (user text, colors).
**How to apply:** When building the editor, extend `buildPlateTexture()` to accept user input params.

## ScrollToPlugin for smooth scroll
Added to GSAP plugins. The Nav's useEffect installs a global `document.click` interceptor that catches all `a[href^="#"]` clicks and runs GSAP smooth scroll. No per-link handlers needed.

## Mobile cursor hidden
CSS rule: `@media (hover: none) { body { cursor: auto; } .cursor-dot, .cursor-ring { display: none; } }` — hides custom cursor on touch devices where it doesn't make sense.
