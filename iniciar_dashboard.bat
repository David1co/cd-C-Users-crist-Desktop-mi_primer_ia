@echo off
color 0a
echo =======================================================
echo    INICIANDO EL DASHBOARD INSTITUCIONAL DE INVERSION
echo =======================================================
echo.
echo 1. Levantando el servidor de Inteligencia Artificial...

cd /d "%~dp0"
start http://127.0.0.1:8000
python server.py

echo.
echo [!] El servidor se ha cerrado.
pause
