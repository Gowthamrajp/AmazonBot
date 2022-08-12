@echo off
set mypath=%cd%
:body
python %mypath%/AmazonBot.py
TIMEOUT /T 3600 /NOBREAK
goto body
