@ECHO OFF
TITLE ghost snakes
ECHO initializing...
wpeinit
powershell Set-ExecutionPolicy RemoteSigned
cmd /k START /MAX X:\tools\python36\python.exe x:\tools\run.py
CLS

:: Put me in X:\Windows\System32\