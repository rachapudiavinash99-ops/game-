Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "       Starting GAMEVERSE Full-Stack Platform" -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan

$env:PATH = "C:\Users\Hi\AppData\Local\Programs\Python\Python312;C:\Users\Hi\AppData\Local\Programs\Python\Python312\Scripts;C:\Users\Hi\AppData\Local\Programs\nodejs;C:\Program Files\Git\cmd;" + $env:PATH
$env:PYTHONPATH = "D:\game\backend"

Write-Host "Starting Backend..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "`$env:PATH = '$env:PATH'; `$env:PYTHONPATH = 'D:\game\backend'; cd D:\game\backend; uvicorn app.main:app --host 127.0.0.1 --port 8008 --reload"

Start-Sleep -Seconds 2

Write-Host "Starting Frontend..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "`$env:PATH = '$env:PATH'; cd D:\game\frontend; npm run dev -- --host 127.0.0.1 --port 5174"

Write-Host "GAMEVERSE is active!" -ForegroundColor Magenta
Write-Host "Frontend: http://localhost:5174" -ForegroundColor White
Write-Host "API Docs: http://localhost:8008/docs" -ForegroundColor White
