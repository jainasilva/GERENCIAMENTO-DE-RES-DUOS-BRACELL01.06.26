@echo off
setlocal
cd /d "%~dp0"
if exist "%~dp0..\ABRIR_APP_OFICIAL.bat" (
  call "%~dp0..\ABRIR_APP_OFICIAL.bat"
) else (
  start "" "%~dp0..\app\index.html"
)
exit /b %errorlevel%
