# SessionStart: pega CRITICAL_FACTS.md del vault en el contexto (al arrancar, tras /clear y tras compactar).
[Console]::OutputEncoding = [Text.Encoding]::UTF8
$f = 'C:\Users\angel\Documents\Obsidian Vault\CRITICAL_FACTS.md'
if (-not (Test-Path $f)) { exit 0 }
$t = Get-Content $f -Raw -Encoding UTF8
# ponytail: tope de 9000 caracteres para no inflar cada sesión; si se recorta, toca adelgazar CRITICAL_FACTS.
if ($t.Length -gt 9000) { $t = $t.Substring(0, 9000) + "`n`n[...recortado por el hook: leer el archivo completo]" }
"CRITICAL_FACTS.md del vault, inyectado por hook ($f):`n`n$t"
