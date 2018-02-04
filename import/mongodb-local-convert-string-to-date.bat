echo echo %DATE%_%TIME% >> "./Logs/database-load-%1.log"
echo "Converting MongoDB Local created_at strings to dates" >> "./Logs/database-load-%1.log"
mongo < convert-string-to-date.js >> "./Logs/database-load-%1.log"