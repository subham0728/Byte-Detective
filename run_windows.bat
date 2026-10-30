@echo off
title Byte Detective Kids
cd /d "%~dp0"
py -m pip install -r requirements.txt
if errorlevel 1 python -m pip install -r requirements.txt
py app.py
if errorlevel 1 python app.py
pause
