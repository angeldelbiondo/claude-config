# PreToolUse (Bash|PowerShell): si un comando cambia configuración de red o del sistema, pide la aprobación
# de Angel con la ventana de permisos ("ask" la muestra aunque la sesión esté en modo automático).
# Regla del CLAUDE.md global (2026-09-26). Revisa el comando Y el contenido de los scripts que ejecuta:
# el 2026-07-29 los cambios de servicios iban dentro de .ps1 corridos con -Verb RunAs, invisibles en el comando.
# Las consultas de solo lectura (Get-*, netsh ... show, ipconfig /all, reg query) pasan sin preguntar.
import json, re, sys
from pathlib import Path

REGLAS = [
    ("DNS", r"\b(Set|Register|Add|Remove)-DnsClient\w*|\bClear-DnsClientCache\b|\bipconfig(\.exe)?\s*/\s*(flushdns|registerdns|release6?|renew6?)\b"),
    ("netsh (cambio)", r"\bnetsh(\.exe)?\b[^\n|;&]*\b(set|add|delete|reset|import|install|uninstall|enable|disable)\b"),
    ("proxy", r"\b(HTTPS?|ALL|NO)_PROXY\s*=|SetEnvironmentVariable\(\s*['\"]?(HTTPS?|ALL|NO)_PROXY|\bsetx(\.exe)?\s+['\"]?(HTTPS?|ALL|NO)_PROXY"
              r"|\bgit\s+config\b[^\n]*\b(https?\.proxy)\b|\bnpm\s+config\s+set\s+(https-)?proxy\b|\bpip\s+config\s+set\s+\S*proxy"),
    ("adaptadores/IP/rutas/firewall", r"\b(Set|Disable|Enable|Restart|Rename|Remove|New|Reset)-Net(Adapter|IPAddress|IPInterface|Route|Firewall|ConnectionProfile|Nat|Neighbor|TCPSetting|OffloadGlobalSetting)\w*"
              r"|\broute(\.exe)?\s+(add|delete|change)\b|\b(Disable|Enable)-PnpDevice\b|\bpnputil(\.exe)?\s+/(add-driver|delete-driver|disable-device|enable-device|remove-device|restart-device)\b"
              r"|\bdevcon(\.exe)?\s+(disable|enable|remove|restart|install|update)\b"),
    ("registro de Windows", r"\breg(\.exe)?\s+(add|delete|import|copy|restore|load|unload)\b|\bregedit(\.exe)?\s+/s\b"),
    ("servicios de Windows", r"\b(Set|Stop|Start|Restart|Suspend|Resume|New|Remove)-Service\b|\bsc(\.exe)?\s+(config|stop|start|delete|create|failure|pause|continue)\b|\bnet\s+(start|stop)\s+\S"),
    ("elevación de permisos", r"-Verb\s+['\"]?RunAs\b|\brunas(\.exe)?\s|\bgsudo\b|\bsudo\s"),
    ("arranque/energía/seguridad", r"\bbcdedit(\.exe)?\s+/(set|delete|create|import|deletevalue)\b|\bpowercfg(\.exe)?\s+/(set\w*|change|h|hibernate|delete|import|duplicatescheme)\b"
              r"|\b(Set|Add|Remove)-MpPreference\b|\bSet-ExecutionPolicy\b"),
]
# Ruta y escritura se buscan por separado: en julio la ruta iba en una variable ($runKey = "HKCU:\...")
# y el Set-ItemProperty en otra línea
REGISTRO = re.compile(r"\b(HKLM|HKCU|HKCR|HKU|HKCC):|Registry::|HKEY_(LOCAL_MACHINE|CURRENT_USER)", re.I)
ESCRIBE_REG = re.compile(r"\b(Set|New|Remove|Rename|Clear|Copy|Move)-Item(Property)?\b", re.I)
HOSTS = re.compile(r"drivers[\\/]+etc[\\/]+hosts", re.I)
ESCRIBE = re.compile(r"\b(Set-Content|Add-Content|Out-File|Copy-Item|Move-Item|Remove-Item|New-Item|tee)\b|\bsed\s+-i\b|(^|[^-=>])>>?(?!=)", re.I)
SCRIPT = re.compile(r"""["']?([^"'\s;|&<>]*[^"'\s;|&<>]+\.(?:ps1|psm1|bat|cmd|reg))["']?|["']([^"']+\.(?:ps1|psm1|bat|cmd|reg))["']""", re.I)


def categorias(texto):
    cats = [n for n, rx in REGLAS if re.search(rx, texto, re.I)]
    if REGISTRO.search(texto) and ESCRIBE_REG.search(texto):
        cats.append("registro de Windows")
    if HOSTS.search(texto) and ESCRIBE.search(texto):
        cats.append("archivo hosts")
    return list(dict.fromkeys(cats))


def scripts_de(comando, cwd):
    # contenido de los scripts que el comando ejecuta, si existen en disco
    out = []
    for m in SCRIPT.finditer(comando):
        ruta = Path(m.group(1) or m.group(2))
        p = ruta if ruta.is_absolute() else Path(cwd or ".") / ruta
        try:
            if p.is_file() and p.stat().st_size < 500_000:
                out.append((p.name, p.read_text(encoding="utf-8", errors="ignore")))
        except OSError:
            pass
    return out


def decidir(entrada):
    if entrada.get("tool_name") not in ("Bash", "PowerShell"):
        return None
    comando = (entrada.get("tool_input") or {}).get("command", "")
    cats = categorias(comando)
    for nombre, texto in scripts_de(comando, entrada.get("cwd")):
        cats += [f"{c} (dentro de {nombre})" for c in categorias(texto)]
    if not cats:
        return None
    return {"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": "Este comando cambia configuración de red o del sistema: " + ", ".join(dict.fromkeys(cats))
            + ". Regla del CLAUDE.md: mostrártelo y esperar tu aprobación. Revisa el comando exacto antes de aceptar.",
    }}


def autoprueba():
    pide = [
        'Disable-NetAdapter -Name "Ethernet" -Confirm:$false',            # 2026-09-26
        "Set-Service -Name DoSvc -StartupType Disabled",                   # 2026-07-29
        'Start-Process powershell -Verb RunAs -ArgumentList "-File","x.ps1"',
        'Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" -Name ProxyEnable -Value 1',
        "Set-DnsClientServerAddress -InterfaceAlias Wi-Fi -ServerAddresses 1.1.1.1",
        "ipconfig /flushdns", "netsh winhttp set proxy 127.0.0.1:8080", "netsh interface ip set dns Wi-Fi static 8.8.8.8",
        "setx HTTPS_PROXY http://127.0.0.1:8080", "export HTTP_PROXY=http://localhost:3128", '$env:HTTPS_PROXY = "http://x"',
        'Add-Content "$env:SystemRoot\\System32\\drivers\\etc\\hosts" "127.0.0.1 api.anthropic.com"',
        "reg add HKLM\\SYSTEM\\x /v y /d 1 /f", "sc config DoSvc start= disabled", "New-NetFirewallRule -DisplayName x",
        "git config --global http.proxy http://x",
        '$runKey = "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\StartupApproved\\Run"\nNew-Item -Path $runKey -Force\nSet-ItemProperty -Path $runKey -Name x -Value 1',  # 2026-07-29
    ]
    pasa = [
        "Get-NetAdapter | Select Name, Status", "Get-DnsClientServerAddress -AddressFamily IPv4", "netsh winhttp show proxy",
        "ipconfig /all", "Resolve-DnsName api.anthropic.com; Test-NetConnection api.anthropic.com -Port 443",
        'Get-Content "$env:SystemRoot\\System32\\drivers\\etc\\hosts" | Where-Object { $_ -notmatch "^#" }',
        "[Environment]::GetEnvironmentVariable('HTTP_PROXY', 'User')", "reg query HKCU\\Software\\x", "Get-Service DoSvc",
        "git status && git log --oneline -3", "python script.py > salida.txt", "Get-ScheduledTaskInfo -TaskName 'Maria recolectar'",
    ]
    for c in pide:
        assert decidir({"tool_name": "PowerShell", "tool_input": {"command": c}}), f"debía preguntar: {c}"
    for c in pasa:
        assert decidir({"tool_name": "Bash", "tool_input": {"command": c}}) is None, f"no debía preguntar: {c}"
    # un script inofensivo al llamarlo, que por dentro cambia un servicio (el caso de julio)
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        Path(d, "limpieza.ps1").write_text("Stop-Service -Name DoSvc -Force\n", encoding="utf-8")
        r = decidir({"tool_name": "PowerShell", "cwd": d, "tool_input": {"command": "& .\\limpieza.ps1"}})
        assert r and "dentro de limpieza.ps1" in r["hookSpecificOutput"]["permissionDecisionReason"], r
    print(f"ok: {len(pide)} preguntan, {len(pasa)} pasan, script por dentro detectado")


if __name__ == "__main__":
    if sys.argv[1:] == ["--test"]:
        autoprueba()
        sys.exit(0)
    try:
        r = decidir(json.loads(sys.stdin.buffer.read().decode("utf-8")))
        if r:
            sys.stdout.buffer.write(json.dumps(r, ensure_ascii=False).encode("utf-8"))
    except Exception:
        pass  # ponytail: falla abierta; un bug acá no puede frenar todos los comandos. Riesgo: si se rompe, no protege. Probar con --test.
    sys.exit(0)
