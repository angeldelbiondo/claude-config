---
description: Design research gratis — busca referencias UI reales en Screenlane, UX Movement, NN Group y más. Modo inspiración o modo critique de tu propio diseño.
disable-model-invocation: true
---

Ejecutá `/design-research [brief]`:

## Argumentos

- `[brief]` — qué estás diseñando. Ej: "fitness app onboarding", "SaaS dashboard", "landing page para herramienta dev", "formulario de login", "empty state". Si no hay argumento, preguntar: "¿Qué estás diseñando?"
- Flag `--critique` — si está presente, el usuario adjuntó un screenshot de SU diseño y quiere feedback. En este caso, además de buscar referencias, critiquear su diseño contra ellas.
- Flag `--save` — guardar los resultados en el vault de Obsidian.

---

## Flujo de ejecución

### Paso 1 — Identificar modo

- Sin `--critique`: **modo inspiración** → buscar referencias externas y sintetizar patrones
- Con `--critique` + imagen adjunta: **modo critique** → buscar referencias Y analizar su diseño contra ellas

### Paso 2 — Buscar referencias (siempre)

Hacer WebSearch y WebFetch sobre los siguientes recursos gratuitos, adaptando la query al brief:

**Búsquedas a realizar (combinar según relevancia):**

```
WebSearch: "[brief] UI design patterns best practices"
WebSearch: "[brief] app design examples site:uxmovement.com OR site:nngroup.com OR site:smashingmagazine.com"
WebSearch: "[brief] UX patterns what works"
WebSearch: "[brief] mobile app design inspiration"
```

**Sites confiables para WebFetch (tienen contenido real sin JS):**
- `https://uxmovement.com` — artículos sobre patrones UI con explicaciones
- `https://www.nngroup.com/articles/` — Nielsen Norman, research-backed
- `https://www.smashingmagazine.com` — artículos técnicos de diseño
- `https://screenlane.com` — galerías de pantallas reales (intentar, puede fallar por JS)
- `https://www.goodui.org` — A/B tests de UI que funcionan
- `https://pttrns.com` — mobile patterns

Fetchear 3-5 resultados relevantes. Si una página falla por JS, skipear y seguir con la siguiente.

### Paso 3 — Sintetizar análisis

Producir un análisis estructurado con este formato:

```
## 🎯 Brief analizado
[reformular el brief en 1 línea para confirmar que entendiste]

## 📱 Referencias encontradas
[3-5 referencias reales con URL, descripción de qué hace bien cada una]

## ✅ Patrones que funcionan
[5-8 patrones concretos con explicación de POR QUÉ funcionan — basados en las referencias + conocimiento de UI]

## ❌ Anti-patrones a evitar
[3-5 cosas que no funcionan en este tipo de UI, con razón]

## 🧩 Elementos clave para este tipo de UI
[componentes específicos que no podés omitir: botones, jerarquía, copy, estados vacíos, etc.]

## 💡 Recomendación concreta
[1-3 párrafos: si yo fuera a diseñar esto desde cero, haría... — directo, accionable]
```

### Paso 4 — Si modo `--critique`

ADEMÁS del análisis anterior, agregar:

```
## 🔍 Critique de tu diseño

### Lo que funciona
[Bullet list — ser específico, no vago]

### Lo que no funciona / podría mejorar
[Bullet list — con razón concreta para cada punto]

### Prioridad de cambios
1. [Cambio más impactante — el que mejora más con menos esfuerzo]
2. [...]
3. [...]

### Comparación con referencias
[Cómo tu diseño se compara específicamente con los mejores ejemplos encontrados]
```

### Paso 5 — Si flag `--save`

Guardar en el vault:
- Archivo: `C:\Users\angel\Documents\Obsidian Vault\wiki\concepts\Design Research — [brief slug].md`
- Frontmatter: `type: design-research`, `date`, `tags: [design, ui, [brief-keywords]]`, `ai-first: true`
- Incluir `## For future Claude` preamble
- Agregar al `index.md`

---

## Triggers en lenguaje natural

Activar este skill cuando el usuario diga:
- "buscame referencias de diseño para..."
- "inspiración UI para..."
- "qué patrones funcionan para [tipo de pantalla]"
- "criticá mi diseño" (+ imagen adjunta)
- "cómo debería verse un/una [elemento UI]"
- "referencias para diseñar [X]"
- "qué hace bien [tipo de app] en cuanto a diseño"

---

## Notas operativas

- **Si WebFetch falla** en un site por JS/CORS → no mencionar el error al usuario, simplemente usar el siguiente. Compensar con conocimiento propio de UI.
- **Ser específico**, no genérico. "Usá tipografía grande" no sirve. "El headline del hero debería ser ≥48px en desktop, con font-weight ≥700 y line-height tight (~1.1) para competir con Strava y Gymshark" sí sirve.
- **Citar fuentes** cuando se extraen patrones de artículos reales.
- **El output es para un desarrollador/diseñador** que va a implementar esto. Pensar en qué necesita saber para empezar a trabajar.

---

## AI-first rule

Si se guarda en el vault, seguir `~/.claude/skills/obsidian-second-brain/references/ai-first-rules.md`:
- `## For future Claude` preamble
- Frontmatter rico con `ai-first: true`
- `[[wikilinks]]` para proyectos/conceptos referenciados
- Recency markers en claims externos
