@echo off
echo wscript.Echo dateadd("d", -1, now()) > "%temp%\yesterday.vbs"
for /F %%a in ('cscript //nologo "%temp%\yesterday.vbs"') do set Yesterday=%%a
echo Yesterday was %Yesterday%