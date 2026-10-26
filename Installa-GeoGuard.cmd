@echo off
cd /d "%~dp0"
python --version >nul 2>&1
if errorlevel 1 (
  echo Installa Python 3.12 o successivo da https://www.python.org/downloads/
  pause
  exit /b 1
)
python -m pip install uv
if errorlevel 1 goto errore
python -m uv sync --locked
if errorlevel 1 goto errore
if not exist .env copy .env.example .env >nul
echo Installazione completata. Apri Avvia-GeoGuard.cmd.
pause
exit /b 0
:errore
echo Installazione non riuscita. Leggi il messaggio sopra.
pause
exit /b 1
