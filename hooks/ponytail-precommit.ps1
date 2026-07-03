# Ponytail pre-commit gate.
# Fires on Claude's Bash tool calls. If the command is a `git commit`, it blocks
# the FIRST attempt and tells Claude to run /ponytail-review and strip
# over-engineering. A short-lived marker file lets the immediate retry through,
# so there's no infinite loop. Manual terminal commits are untouched (this only
# sees Claude's tool calls).

$ErrorActionPreference = 'SilentlyContinue'

# Hook payload arrives as JSON on stdin.
$raw = [Console]::In.ReadToEnd()
try { $data = $raw | ConvertFrom-Json } catch { exit 0 }

$cmd = $data.tool_input.command
if (-not $cmd) { exit 0 }
if ($cmd -notmatch 'git\s+commit') { exit 0 }

$marker = Join-Path $env:TEMP 'ponytail-precommit.flag'

if (Test-Path $marker) {
    $age = ((Get-Date) - (Get-Item $marker).LastWriteTime).TotalSeconds
    Remove-Item $marker -Force
    if ($age -lt 300) { exit 0 }  # recent retry -> let the commit through
}

# First attempt: arm the marker and block, handing Claude the instruction.
New-Item -ItemType File -Path $marker -Force | Out-Null

$msg = "Ponytail pre-commit: antes de guardar, corre /ponytail-review sobre el diff y elimina el over-engineering que liste (dependencias innecesarias, abstracciones de mas, codigo que se pueda colapsar). Despues reintenta exactamente el mismo git commit; este chequeo te deja pasar en el reintento."

$out = @{
    hookSpecificOutput = @{
        hookEventName            = 'PreToolUse'
        permissionDecision       = 'deny'
        permissionDecisionReason = $msg
    }
} | ConvertTo-Json -Compress

[Console]::Out.Write($out)
exit 0
