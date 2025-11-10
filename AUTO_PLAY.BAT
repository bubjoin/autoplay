@echo off
chcp 65001
cd /d "%~dp0"
set PYTHON=.\winpython64_314\python\python.exe
"%PYTHON%" main.py

echo [종료] 아무 키나 누르면 닫힙니다...
pause >nul