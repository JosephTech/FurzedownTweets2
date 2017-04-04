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

    def Process(self, tweet):
        print(tweet.text)
        #self.api.retweet(tweet.id)


    def InitialiseLatestTweetId(self, lastTweetId, searchString):
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

    def GetNewFollowers(self):
        newFollowers = list()
        for follower in tweepy.Cursor(self.api.followers).items(100):
            if not follower.following:
                print(follower.screen_name)
                newFollowers.append(follower)
        return newFollowers

    def BefriendNewFollowers(self, newFollowers, newFollowerMessage, loggingRecipient):
        newFollowers = 0
        for follower in newFollowers:
            try:
                self.api.create_friendship(follower.screen_name)
                if newFollowerMessage:
                    self.DirectMessage(follower.screen_name, newFollowerMessage)
                newFollowers += 1
            except Exception as e:
                self.DirectMessage(loggingRecipient, str(e))

        return newFollowers


    def GetFollowers_Count(self):
        return self.api.me().followers_count


