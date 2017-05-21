echo %DATE%_%TIME% >> "./Logs/database-load-%1.log"
echo "Loading to MongoDB Atlas ..\export\tweet_data_%1.json" >> "./Logs/database-load-%1.log"

mongoimport --host "cluster0-shard-00-00-rsihj.mongodb.net:27017,cluster0-shard-00-01-rsihj.mongodb.net:27017,cluster0-shard-00-02-rsihj.mongodb.net:27017" --authenticationDatabase admin --ssl --username julesjoseph --password ftsP93gnEqiEXZPe --db furzedowntweets --collection tweets --file ..\export\tweet_data_%1.json
