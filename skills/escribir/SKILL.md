---
name: escribir
description: Producir textos y documentos. Usar cuando Angel pide un documento, informe, propuesta, presentación, PDF, Word, PowerPoint, correo o plantilla HTML de email, un README o copy público (lanzamiento, post); o pide que un texto suene menos a IA.
---

# Escribir

| Qué | Skill |
|---|---|
| Documento para leer o editar en conjunto | artifact tipo Docs (quickstart `document`), o `doc-coauthoring` (en prueba) para armarlo por secciones |
| Archivo Word | `docx` |
| Presentación | artifact tipo Slides; `pptx` si pide el archivo |
| PDF (leer, unir, llenar) | `pdf`; para ver o anotar, `pdf-viewer:*` |
| Correo HTML, Outlook | `html-para-correos`; responsive, `email-html-mjml` |
| Comunicado interno | `internal-comms` |
| Textos de una interfaz | `design:ux-copy` |
| Copy público (README, lanzamiento, posts) | escribir y después pasar por `humanizer` (en prueba). Para posicionamiento, antes por `investigar` (marketing-research) |

Reglas:
- Español neutro (tú) con léxico panameño, salvo que Angel pida otro idioma.
- Los commits y mensajes a terceros van sin la palabra canario.
- Para enviar o publicar algo, pide el OK explícito antes.
