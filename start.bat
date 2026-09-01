@echo off
echo ===================================================
echo        Starting GAMEVERSE Full-Stack Platform
echo ===================================================

echo [1/2] Launching FastAPI Backend on http://localhost:8008...
start cmd /k "set PATH=C:\Users\Hi\AppData\Local\Programs\Python\Python312;C:\Users\Hi\AppData\Local\Programs\Python\Python312\Scripts;%PATH% && set PYTHONPATH=D:\game\backend && cd /d D:\game\backend && uvicorn app.main:app --host 127.0.0.1 --port 8008 --reload"

timeout /t 2 >nul

echo [2/2] Launching React Frontend on http://localhost:5174...
start cmd /k "set PATH=C:\Users\Hi\AppData\Local\Programs\nodejs;%PATH% && cd /d D:\game\frontend && npm run dev -- --host 127.0.0.1 --port 5174"

echo.
echo ===================================================
echo GAMEVERSE is running!
echo Frontend: http://localhost:5174
echo API Docs: http://localhost:8008/docs
echo ===================================================
pause
