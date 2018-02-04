from mailHandler import SendEmail
from datetime import datetime
from datetime import timedelta
from time import strftime
from bson.son import SON

from pymongo import MongoClient

#GitHub Test

client = MongoClient('mongodb://julesjoseph:ftsP93gnEqiEXZPe@cluster0-shard-00-00-rsihj.mongodb.net:27017,cluster0-shard-00-01-rsihj.mongodb.net:27017,cluster0-shard-00-02-rsihj.mongodb.net:27017/furzedowntweets?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')
db = client.furzedowntweets
tweets = db.tweets.find()

yesterday = datetime.now()  + timedelta(days=-1)


start = datetime(yesterday.year, yesterday.month, yesterday.day, 0, 0, 0)
end = datetime(yesterday.year, yesterday.month, datetime.now().day, 0, 0, 0)
json = { 'created_at': { '$gte': start, '$lte' : end } }

yesterdayTweets = db.tweets.find(json)


summaryText = "Total Tweets: {0}".format(tweets.count())
summaryText += '\n'
summaryText += "{0} Tweets: {1}".format(yesterday.strftime('%Y-%m-%d'), yesterdayTweets.count())
summaryText += '\n\n'

#Today's hashtags
pipeline = [
    # last day only
    {'$match': {'created_at': {'$gt': start}}},
    #get all tweets with hashtags
    {'$sort':{'_id':-1}}, {'$match': {'entities.hashtags.text':{'$exists':'true'}}},
    #hashtags are stored in an array, so separate these out
    {'$unwind':'$entities.hashtags'},
    #use the text of the hashtag
    {'$project' : {'entities.hashtags.text':1,'_id':0}},
    #group on the hashtag and add 1 for every occurrence
    {'$group':{'_id':{'$toLower':'$entities.hashtags.text'}, 'count' : {'$sum' : 1 }}},
    #finally sort the result in desdencing order by count
    {'$sort': SON([("count", -1), ("_id", -1)])}
]

summaryText +=('{0} Trending Hashtags'.format(yesterday.strftime('%Y-%m-%d')))
summaryText+='\n'
for hashTag in db.tweets.aggregate(pipeline):
    if(hashTag['count'] > 2 and hashTag['_id'] != 'tooting' and hashTag['_id'] != 'furzedown'):
        summaryText+='{0},{1}'.format(hashTag['_id'],hashTag['count'])
        summaryText+='\n'
summaryText+='\n'

#all time hash tags
pipeline = [
    #get all tweets with hashtags
    {'$sort':{'_id':-1}}, {'$match': {'entities.hashtags.text':{'$exists':'true'}}},
    #hashtags are stored in an array, so separate thiese out
    {'$unwind':'$entities.hashtags'},
    #use the text of the hashtag
    {'$project' : {'entities.hashtags.text':1,'_id':0}},
    #group on the hashtag and add 1 for every occurrence
    {'$group':{'_id':{'$toLower':'$entities.hashtags.text'}, 'count' : {'$sum' : 1 }}},
    #finally sort the result in desdencing order by count
    {'$sort': SON([("count", -1), ("_id", -1)])}
]

summaryText +=('{0} All Time Hashtags'.format(yesterday.strftime('%Y-%m-%d')))
summaryText+='\n'
for hashTag in db.tweets.aggregate(pipeline):
    if(hashTag['count'] > 2 and hashTag['_id'] != 'tooting' and hashTag['_id'] != 'furzedown'):
        summaryText+='{0},{1}'.format(hashTag['_id'],hashTag['count'])
        summaryText+='\n'
summaryText+='\n'


print(summaryText)

SendEmail(summaryText)

