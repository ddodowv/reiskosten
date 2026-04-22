@echo off
cd /d "%~dp0"

:: Controleer of de server al draait op poort 8765
netstat -ano | findstr ":8765" | findstr "LISTENING" >nul 2>&1
if %errorlevel%==0 (
    start http://localhost:8765/reiskosten.html
) else (
    :: Open browser na korte vertraging
    start /b cmd /c "timeout /t 1 >nul && start http://localhost:8765/reiskosten.html"
    python server.py
)
