# Claude Code — Script de restauración
# Corre esto despues de instalar Claude Code en una maquina nueva y clonar claude-config en ~/.claude
# Usage: powershell -ExecutionPolicy Bypass -File restore.ps1
#
# Todo lo demás (skills locales y de prueba, comandos, hooks, memoria por proyecto) viene dentro de este repo.
# Las dos skills de GitHub tienen cambios locales: se clonan, se vuelven al commit sobre el que se
# hicieron los cambios, y se aplica el patch de skill-patches/. Para regenerar un patch despues de
# tocar una skill: git -C skills/<nombre> diff HEAD -M --binary > skill-patches/<nombre>.patch
# (con archivos nuevos, antes: git -C skills/<nombre> add -A; y despues: git -C skills/<nombre> reset)

$skillsDir = "$HOME\.claude\skills"
$patches = "$HOME\.claude\skill-patches"

Write-Host "Instalando obsidian-second-brain (con el fork local: lee OBSIDIAN_VAULT_PATH)..."
git clone https://github.com/eugeniughelbur/obsidian-second-brain "$skillsDir\obsidian-second-brain"
git -C "$skillsDir\obsidian-second-brain" checkout -q 69b9acb40949b1be21dc3461b50d5464808419e6
git -C "$skillsDir\obsidian-second-brain" apply "$patches\obsidian-second-brain.patch"
# 5 comandos propios del fork que git no sigue (el patch no los lleva)
Copy-Item "$patches\untracked-2026-09-29\*.md" "$skillsDir\obsidian-second-brain\commands\"

Write-Host "Instalando marketing-research..."
git clone https://github.com/ishwarjha/claude-marketing-research-skill "$skillsDir\marketing-research"
git -C "$skillsDir\marketing-research" checkout -q 0b31cbde9a51c4a0a1d2ceca68fd39db00f5c558
# El patch incluye subir el SKILL.md un nivel: el repo lo trae una carpeta mas abajo y asi Claude Code no lo carga
git -C "$skillsDir\marketing-research" apply "$patches\marketing-research.patch"

Write-Host ""
Write-Host "Listo. Reinicia Claude Code para cargar los skills."
Write-Host "Plugins del marketplace (anthropic-skills:*) reinstalalos desde la UI de Claude Code."
Write-Host "Fuera de ~/.claude: crea ~/.config/last30days/.env con AGENTCOOKIE=off (ver README)."
