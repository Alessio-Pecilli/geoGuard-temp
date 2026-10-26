@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Prima esegui Installa-GeoGuard.cmd.
  pause
  exit /b 1
)
".venv\Scripts\python.exe" avvia_geoguard.py
if errorlevel 1 pause
