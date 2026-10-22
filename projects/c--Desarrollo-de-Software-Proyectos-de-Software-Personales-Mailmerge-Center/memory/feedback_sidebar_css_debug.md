---
name: Sidebar CSS — causas raíz y solución definitiva
description: Las 3 causas reales de por qué la sidebar mostraba cajas indeseadas y el proceso que impedía ver cambios
type: feedback
---

## Contexto
La sidebar de Mailmerge Center mostraba "cajas" (rounded cards) alrededor del contenido aunque se intentaba sobreescribir el CSS desde `campaign_manager.py`. Los cambios nunca parecían aplicarse.

## Causas raíz confirmadas

### 1. `stVerticalBlockBorderWrapper` global sin excepción para sidebar
`styles.css` tiene esta regla global:
```css
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255, 255, 255, 0.034) !important;
    border: 1px solid rgba(255, 255, 255, 0.082) !important;
    border-radius: var(--r-lg) !important;  /* 16px */
    backdrop-filter: blur(16px) !important;
}
```
Streamlit envuelve el contenido del sidebar en un `stVerticalBlockBorderWrapper`, creando la **caja exterior redondeada** visible alrededor de todo el contenido del sidebar.

**Fix:** Agregar en la sección SIDEBAR de `styles.css`:
```css
[data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] {
    background: transparent !important;
    border: none !important;
    border-radius: 0 !important;
    box-shadow: none !important;
    backdrop-filter: none !important;
}
```

### 2. `.stButton > button[kind="secondary"]` global sin excepción para sidebar
`styles.css` tiene:
```css
.stButton > button[kind="secondary"] {
    background: rgba(255, 255, 255, 0.055) !important;
    border: 1px solid var(--border-med) !important;
}
```
Esto aplica a TODOS los botones secundarios, incluyendo los de la lista de campañas en el sidebar, creando **cajas internas** alrededor de cada botón.

**Fix:** Agregar en `styles.css` (sección SIDEBAR):
```css
[data-testid="stSidebar"] .stButton > button {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}
```

### 3. El launcher mataba `streamlit.exe` pero Streamlit corre como `python.exe`
`launcher.py` tenía:
```python
os.system("taskkill /f /im streamlit.exe >nul 2>&1")
```
El proceso viejo (`python.exe` en puerto 8501) sobrevivía, y el nuevo proceso no podía bindear al mismo puerto. WebView2 siempre conectaba al proceso viejo (con código sin cambios).

**Fix en `launcher.py`:**
```python
os.system(
    'for /f "tokens=5" %a in '
    "('netstat -ano ^| findstr :8501 ^| findstr LISTENING') "
    "do taskkill /f /pid %a >nul 2>&1"
)
```

## Lección aprendida
- **Siempre buscar en `styles.css` primero** cuando los overrides en componentes no funcionan — las reglas globales de botones/contenedores pueden tener precedencia
- **Los cambios en el worktree requieren verificar que el launcher mate el proceso correcto** antes de probar
- **`stVerticalBlockBorderWrapper`** = la "glassmorphic card" de Streamlit — siempre agregar excepción para sidebar si no se quiere ese estilo ahí
- La opción más confiable para testing es `python -m streamlit run app.py --server.port 8502` (puerto diferente, evita conflictos)

## Archivos afectados
- `styles.css` (sección SIDEBAR ~línea 842)
- `launcher.py` (función `main()`, línea ~59)
- `components/campaign_manager.py` (layout de columnas y CSS inline)
