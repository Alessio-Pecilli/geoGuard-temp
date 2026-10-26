$pidFile = Join-Path $PSScriptRoot 'geoguard-local.pid'
if (Test-Path -LiteralPath $pidFile) {
    $serverPid = [int](Get-Content -LiteralPath $pidFile)
    $serverProcess = Get-CimInstance Win32_Process -Filter "ProcessId = $serverPid"
    if ($serverProcess -and $serverProcess.CommandLine -like '*marimo*geoguard-e2e.py*') {
        Stop-Process -Id $serverPid
    }
}
