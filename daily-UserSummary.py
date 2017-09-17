from datetime import datetime
import twitter
import readConfig

from pymongo import MongoClient

settings = readConfig.ConfigSettings('config.json')

t = twitter.Wrapper(access_token=settings.AccessToken,
					access_token_secret=settings.AccessTokenSecret,
					consumer_key=settings.ConsumerKey,
					consumer_secret=settings.ConsumerSecret)

dailyCount = t.GetFollowers_Count()
print(t.GetFollowers_Count())


client = MongoClient('mongodb://julesjoseph:ftsP93gnEqiEXZPe@cluster0-shard-00-00-rsihj.mongodb.net:27017,cluster0-shard-00-01-rsihj.mongodb.net:27017,cluster0-shard-00-02-rsihj.mongodb.net:27017/furzedowntweets?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')
db = client.furzedowntweets

dailyCountRecord = { "count" : dailyCount, "date" : datetime.now()}

result = db.followers.insert_one(dailyCountRecord).inserted_id
print(result)

