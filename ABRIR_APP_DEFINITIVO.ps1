$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$app = Join-Path $root "app\index.html"
if (Test-Path $app) {
  Start-Process $app
  Write-Host "Aplicativo aberto: $app"
  exit 0
}
Write-Host "Arquivo nao encontrado: $app"
exit 1
