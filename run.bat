@echo off
setlocal

REM Move to repo root (important in Jenkins)
cd /d "%~dp0"

REM Create reports folder if missing
if not exist "reports" mkdir reports

REM Create virtual environment
if not exist "venv\Scripts\python.exe" (
    py -m venv venv
)

REM Install dependencies
venv\Scripts\python.exe -m pip install --upgrade pip
venv\Scripts\python.exe -m pip install -r requirements.txt

REM Run pytest (NO activate, NO PATH issues)
venv\Scripts\python.exe -m pytest -s -v -m "sanity" --browser chrome --html=reports\test_reports.html

pause
endlocal
