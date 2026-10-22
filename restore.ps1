# Claude Code — restauración en una PC nueva (o en otra PC de Angel)
# Antes: traer este repo a ~/.claude (pasos en SETUP-OTRA-PC.md).
# Uso:    powershell -ExecutionPolicy Bypass -File "$HOME\.claude\restore.ps1"
# Prueba sin tocar la instalación real: -Casa <carpeta> -SinPlugins (Casa hace de $HOME, con el repo en <carpeta>\.claude)
#
# Los dos forks de GitHub tienen cambios locales: se clonan, se vuelven al commit sobre el que se hicieron
# los cambios y se aplica el patch de skill-patches/. Para regenerar un patch después de tocar una skill:
#   git -C skills/<nombre> diff HEAD -M --binary > skill-patches/<nombre>.patch
# Todo lo demás (skills locales y de prueba, comandos, hooks, memoria por proyecto) viene dentro de este repo.
param([string]$Casa = $HOME, [switch]$SinPlugins)

$claude = "$Casa\.claude"; $skillsDir = "$claude\skills"; $patches = "$claude\skill-patches"
$utf8 = New-Object Text.UTF8Encoding $false  # sin BOM: settings.json con BOM no lo lee Python

# 0. Requisitos
foreach ($c in "git", "python", "claude") {
    if (-not (Get-Command $c -ErrorAction SilentlyContinue)) { Write-Warning "Falta '$c' en el PATH. Instálalo y vuelve a correr este script." }
}

# 1. Rutas: settings.json y los hooks traen C:\Users\angel. Si esta PC tiene otro usuario, se corrigen.
# ponytail: reemplazo de texto plano; si algún día hay más rutas fijas, agregarlas acá.
$viejo = 'C:\Users\angel'
if ($Casa -ne $viejo) {
    $archivos = @("$claude\settings.json") + (Get-ChildItem "$claude\hooks" -File | Where-Object Extension -in ".py", ".ps1").FullName
    foreach ($f in $archivos) {
        $t = [IO.File]::ReadAllText($f)
        $t2 = $t.Replace($viejo.Replace('\', '\\'), $Casa.Replace('\', '\\')).Replace($viejo, $Casa)
        if ($t2 -ne $t) { [IO.File]::WriteAllText($f, $t2, $utf8); Write-Host "Rutas corregidas: $f" }
    }
    Write-Host "OJO: no hagas commit de settings.json ni de hooks/ desde esta PC: llevan las rutas de esta PC."
}

# 2. Vault de Obsidian: no viaja en este repo
$vault = "$Casa\Documents\Obsidian Vault"
if (-not (Test-Path "$vault\CRITICAL_FACTS.md")) {
    Write-Warning "No encuentro el vault en $vault. Los hooks del vault quedan en silencio (no rompen nada) hasta que esté ahí."
}

# 3. Los dos forks (solo si faltan)
if (-not (Test-Path "$skillsDir\obsidian-second-brain")) {
    Write-Host "Instalando obsidian-second-brain (fork local: lee OBSIDIAN_VAULT_PATH)..."
    git clone -q https://github.com/eugeniughelbur/obsidian-second-brain "$skillsDir\obsidian-second-brain"
    git -C "$skillsDir\obsidian-second-brain" checkout -q 69b9acb40949b1be21dc3461b50d5464808419e6
    git -C "$skillsDir\obsidian-second-brain" apply "$patches\obsidian-second-brain.patch"
    # 5 comandos propios del fork que git no sigue (el patch no los lleva)
    Copy-Item "$patches\untracked-2026-09-29\*.md" "$skillsDir\obsidian-second-brain\commands\"
}
if (-not (Test-Path "$skillsDir\marketing-research")) {
    Write-Host "Instalando marketing-research..."
    git clone -q https://github.com/ishwarjha/claude-marketing-research-skill "$skillsDir\marketing-research"
    git -C "$skillsDir\marketing-research" checkout -q 0b31cbde9a51c4a0a1d2ceca68fd39db00f5c558
    # El patch sube el SKILL.md un nivel (el repo lo trae una carpeta más abajo) y lo oculta de la lista
    git -C "$skillsDir\marketing-research" apply "$patches\marketing-research.patch"
}

# 4. Fuera de ~/.claude: last30days nunca lee cookies del navegador
$env30 = "$Casa\.config\last30days\.env"
if (-not (Test-Path $env30)) {
    New-Item -ItemType Directory -Force (Split-Path $env30) | Out-Null
    [IO.File]::WriteAllText($env30, "# Angel 2026-10-21: nunca leer cookies del navegador (X/agentcookie)`nAGENTCOOKIE=off`n", $utf8)
    Write-Host "Creado $env30"
}

# 5. Plugins: los marketplaces y plugins que settings.json ya declara
if (-not $SinPlugins) {
    $s = Get-Content "$claude\settings.json" -Raw | ConvertFrom-Json
    foreach ($m in $s.extraKnownMarketplaces.PSObject.Properties) {
        $src = if ($m.Value.source.repo) { $m.Value.source.repo } else { $m.Value.source.url }
        Write-Host "Marketplace $($m.Name)..."; claude plugin marketplace add $src
    }
    foreach ($p in $s.enabledPlugins.PSObject.Properties.Name) { Write-Host "Plugin $p..."; claude plugin install $p }
}

Write-Host ""
Write-Host "Listo. Reinicia Claude Code para cargar skills, hooks y plugins."
Write-Host "Los paquetes de la app (anthropic-skills, data, design...) llegan solos con tu cuenta."
Write-Host "Chequeo: cd `"$claude\hooks`"; python ruta.py; python test_firmas_canario.py; python red-sistema-guard.py --test"
