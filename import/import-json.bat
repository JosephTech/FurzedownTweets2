echo %DATE%_%TIME% >> "./Logs/database-load-%1.log"
echo "Loading to MongoDB Local ..\export\tweet_data_%1.json" >> "./Logs/database-load-%1.log"

mongoimport --db furzedowntweets --collection tweets --file ..\export\tweet_data_%1.json
