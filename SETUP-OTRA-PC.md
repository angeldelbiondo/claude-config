# Setup en otra PC de Angel

Guía para la sesión de Claude Code de otra computadora: dejarla con la misma configuración que la principal. Seguir los pasos en orden.

## Antes de empezar

- Instalado: Claude Code (con la sesión iniciada en la cuenta de Angel), `git`, `python` 3.12 o más nuevo y PowerShell.
- El repo es **privado**: la PC tiene que poder entrar a GitHub como `angeldelbiondo` (Git Credential Manager pide el login en el primer `git fetch`, o `gh auth login`).

## 1. Respaldar lo que ya haya en `~/.claude`

```powershell
if (Test-Path "$HOME\.claude") { Copy-Item "$HOME\.claude" "$HOME\.claude-respaldo-$(Get-Date -Format yyyyMMdd-HHmm)" -Recurse }
```

## 2. Traer el repo encima, sin borrar el login ni las sesiones de esta PC

Si `~/.claude` **no existe**:
```powershell
git clone https://github.com/angeldelbiondo/claude-config "$HOME\.claude"
```

Si **ya existe** (lo normal, porque Claude Code ya se usó ahí):
```powershell
cd "$HOME\.claude"
git init
git remote add origin https://github.com/angeldelbiondo/claude-config
git fetch origin
git checkout -f -B main origin/main
```
`checkout -f` pisa solo los archivos que están en el repo. El login (`.credentials.json`), las sesiones y la caché quedan como estaban porque el repo los ignora.

## 3. Correr la restauración

```powershell
powershell -ExecutionPolicy Bypass -File "$HOME\.claude\restore.ps1"
```

Qué hace:
- **Rutas:** si el usuario de Windows de esta PC no es `angel`, corrige las rutas de `settings.json` y de los hooks.
- **Forks:** clona y parchea los dos forks (`obsidian-second-brain` y `marketing-research`).
- **last30days:** crea `~/.config/last30days/.env` con `AGENTCOOKIE=off`, para que nunca lea cookies del navegador.
- **Plugins:** agrega los 7 marketplaces e instala los 8 plugins de `settings.json`.

## 4. El vault de Obsidian (no viaja en este repo)

Tiene que estar en `$HOME\Documents\Obsidian Vault`, con `CRITICAL_FACTS.md` adentro. Sin el vault, los hooks del vault quedan en silencio, sin romper nada, y la skill `recordar` no tiene dónde escribir. Cómo sincronizarlo entre las dos PC lo decide Angel (Obsidian Sync, OneDrive, git…).

## 5. Reiniciar Claude Code y verificar

```powershell
cd "$HOME\.claude\hooks"
python ruta.py
python test_firmas_canario.py
python red-sistema-guard.py --test
```
Las tres tienen que decir `ok`. Después, en una sesión nueva, pedir **"revisa la lista de skills"**:
- Tienen que aparecer `orquestar` y las 9 skills por intención (diseno, investigar, decidir, construir, depurar, revisar, recordar, escribir, datos).
- No tienen que aparecer las 7 ocultas (court, design-dna, design-motion, design-research, marketing-research, reddit-arctic-shift, obsidian-second-brain).
- Ninguna skill tiene que llegar sin descripción.

## Reglas para esta PC

- **No hacer commit de `settings.json` ni de `hooks/` si `restore.ps1` les corrigió las rutas.** Llevan las rutas de esta PC y romperían la principal.
- **Para traer cambios nuevos de la principal:**
  ```powershell
  cd "$HOME\.claude"
  git pull
  ```
  Si hubo rutas corregidas, primero `git stash`, después `git pull`, `git stash pop` y volver a correr `restore.ps1`.
- **La memoria por proyecto** (`projects/*/memory/`) solo aplica si los proyectos están en las mismas rutas que en la PC principal (`C:\Desarrollo de Software\...`).
