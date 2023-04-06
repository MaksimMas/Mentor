@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5892365212:AAELYsxonLoApk5H28Lsc9ins2OoxdXiy2g
python bot_telegram.py

pause 