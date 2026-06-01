@echo off
setlocal
cd /d "%~dp0"
title Abrir App Bracell (Oficial)

set "APP_FILE=%~dp0app\index.html"
if not exist "%APP_FILE%" (
  echo Arquivo nao encontrado:
  echo %APP_FILE%
  pause
  exit /b 1
)

start "" "%APP_FILE%"
exit /b 0
