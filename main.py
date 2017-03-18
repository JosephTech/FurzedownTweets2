import readConfig
import readList
import twitter

def main():
    settings = readConfig.ConfigSettings('./config/config.json')

    bannedUsers = readList.getList('./config/users.txt')
    bannedWords = readList.getList('./config/words.txt')

    t = twitter.Wrapper(access_token=settings.AccessToken,
                                access_token_secret=settings.AccessTokenSecret,
                                consumer_key=settings.ConsumerKey,
                                consumer_secret=settings.ConsumerSecret)

    latestTweets = t.LatestTweets(settings.SearchQuery, settings.LastTweetId)

    last_tweet_id = str(latestTweets[0].id)

    latestTweets = t.FilterReplies(latestTweets)
    latestTweets = t.FilterBannedUsers(latestTweets, bannedUsers)
    latestTweets = t.FilterBannedWords(latestTweets, bannedWords)
    latestTweets = t.FilterMultipleHashTags(latestTweets, 3)
    latestTweets.reverse()

    for tweet in latestTweets:
        t.Process(tweet)

if __name__ == '__main__':
    main()