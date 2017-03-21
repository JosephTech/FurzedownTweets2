import tweepy

class Wrapper:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)


    def LatestTweets(self, searchString, lastId):
        searchResults = tweepy.Cursor(self.api.search, q=searchString, since_id=lastId, lang='en').items()
        latestTweets = list()
        for result in searchResults:
            latestTweets.append(result)
        return latestTweets

    def FilterReplies(self, tweets):
        return list(filter(lambda status: status.text[0] != "@", tweets))

    def FilterBannedWords(self, tweets, bannedWords):
        return list(filter(lambda status: not any(word in status.text.split() for word in bannedWords), tweets))

    def FilterBannedUsers(self, tweets, bannedUsers):
        return list(filter(lambda status: status.author.screen_name not in bannedUsers, tweets))

    def FilterMultipleHashTags(self, tweets, maxHashTags):
        return list(filter(lambda status: status.text.count('#') <= maxHashTags, tweets))


    def Process(self, tweet):
        # iterate the timeline and retweet
        # only allow tweets with 3 or less hashtags
        print(tweet.text)

    def InitialiseLatestTweetId(self, lastTweetId, searchString):
        """when first running, we dont want to get every tweet since the dawn of time!"""
        if lastTweetId==0:
            searchResults = tweepy.Cursor(self.api.search, q=searchString, lang='en').items(1)
            latestTweets = list()
            for result in searchResults:
                latestTweets.append(result)

            return latestTweets[0].id

        return lastTweetId


