import tweepy

class Wrapper:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit_notify=True)


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
        #self.api.retweet(tweet.id)

    def InitialiseLatestTweetId(self, lastTweetId, searchString):
        """when first running, we dont want to get every tweet since the dawn of time!"""
        if lastTweetId==0:
            searchResults = tweepy.Cursor(self.api.search, q=searchString, lang='en').items(1)
            latestTweets = list()

            for result in searchResults:
                latestTweets.append(result)

            if(latestTweets):
                return latestTweets[0].id

        return lastTweetId

    def DirectMessage(self, userId, messageText):
        self.api.send_direct_message(screen_name=userId, text=messageText)


