@echo off
setlocal
cd /d "%~dp0"
call "%~dp0ABRIR_APP_OFICIAL.bat"
exit /b %errorlevel%
