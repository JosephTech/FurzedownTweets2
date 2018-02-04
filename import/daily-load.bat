@echo off
echo wscript.Echo dateadd("d", -1, now()) > "%temp%\yesterday.vbs"
for /F %%a in ('cscript //nologo "%temp%\yesterday.vbs"') do set Yesterday=%%a

set Yesterday=%Yesterday:~6,4%%Yesterday:~3,2%%Yesterday:~0,2%
echo %Yesterday%


call file-transfer.bat %Yesterday%
call import-json.bat %Yesterday%
call import-json-atlas.bat %Yesterday%
call mongodb-atlas-convert-string-to-date.bat %Yesterday%
call mongodb-local-convert-string-to-date.bat %Yesterday%
call send-daily-summary.bat