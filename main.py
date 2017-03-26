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

    maxHashTags = settings.MaxHashTags

    lastTweetId = t.InitialiseLatestTweetId(settings.LastTweetId, settings.SearchQuery)
    print('lastTweetId: {0}'.format(lastTweetId))

    latestTweets = t.LatestTweets(settings.SearchQuery, lastTweetId)

    if(latestTweets):
        latestTweetId = str(latestTweets[0].id)
    else:
        latestTweetId = lastTweetId

    latestTweets = t.FilterReplies(latestTweets)
    latestTweets = t.FilterBannedUsers(latestTweets, bannedUsers)
    latestTweets = t.FilterBannedWords(latestTweets, bannedWords)
    latestTweets = t.FilterMultipleHashTags(latestTweets, maxHashTags)
    latestTweets.reverse()

    errorCount = 0
    retweetCount = 0
    for tweet in latestTweets:
        try:
            t.Process(tweet)
            retweetCount += 1
        except Exception as e:
            errorCount += 1
        continue

    message = "ReTweeter Log: %d Tweets retweeted, %d errors occured." % (retweetCount, errorCount)
    print(message)
    t.DirectMessage("josephtech", message)

    settings.UpdateLastTweetId(latestTweetId)


if __name__ == '__main__':
    main()
