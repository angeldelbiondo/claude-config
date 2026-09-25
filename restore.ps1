# Claude Code — Script de restauración
# Corre esto despues de instalar Claude Code en una maquina nueva
# Usage: powershell -ExecutionPolicy Bypass -File restore.ps1

$skillsDir = "$HOME\.claude\skills"
Write-Host "Creando carpeta de skills..."
New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null

Write-Host "Instalando obsidian-second-brain..."
git clone https://github.com/eugeniughelbur/obsidian-second-brain "$skillsDir\obsidian-second-brain"

Write-Host "Instalando marketing-research..."
git clone https://github.com/ishwarjha/claude-marketing-research-skill "$skillsDir\marketing-research"
# El repo trae el SKILL.md una carpeta más abajo y así Claude Code no lo carga (2026-09-23): subirlo un nivel
git -C "$skillsDir\marketing-research" mv marketing-research/SKILL.md SKILL.md

Write-Host ""
Write-Host "Listo. Reinicia Claude Code para cargar los skills."
Write-Host "Plugins del marketplace (anthropic-skills:*) reinstalalos desde la UI de Claude Code."
