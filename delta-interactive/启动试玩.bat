@echo off
cd /d "%~dp0"
start "delta-proto-server" /min "C:\Users\publi\.dsh\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe" -m http.server 8787
timeout /t 2 >nul
start "" "http://127.0.0.1:8787/index.html"