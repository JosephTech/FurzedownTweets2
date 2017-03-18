import tweepy

class Wrapper:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)


    def LatestTweets(self, searchString, lastId):
        searchResults = tweepy.Cursor(self.api.search, q=searchString, since_id=lastId, lang='en').items()
        latestTweets = []
        for result in searchResults:
            latestTweets.append(result)
        return latestTweets

