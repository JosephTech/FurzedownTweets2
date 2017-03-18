import tweepy

class Twitter:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)


    def LatestTweets(self, searchString, lastId):
        latestTweets = tweepy.Cursor(self.api.search, q=searchString, since_id=lastId, lang='en').items()
        return latestTweets



#timelineIterator = tweepy.Cursor(api.search, q=hashtag, since_id=lastid, lang=tweetLanguage).items()

#https://twitter.com/TootingEaters/status/843125330013569025