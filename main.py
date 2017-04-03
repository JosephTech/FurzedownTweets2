import readConfig
import readList
import twitter
import filter
import friendFollowers
import os


def main():

    settings = readConfig.ConfigSettings('config.json')

    bannedUsers = readList.getList('users.txt')
    bannedWords = readList.getList('words.txt')
    loggingRecipient = settings.LoggingRecipient

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

    latestTweets = filter.FilterReplies(latestTweets)
    latestTweets = filter.FilterBannedUsers(latestTweets, bannedUsers)
    latestTweets = filter.FilterBannedWords(latestTweets, bannedWords)
    latestTweets = filter.FilterMultipleHashTags(latestTweets, maxHashTags)
    latestTweets.reverse()

    errorCount = 0
    retweetCount = 0
    for tweet in latestTweets:
        try:
            t.Process(tweet)
            retweetCount += 1
        except Exception as e:
            t.DirectMessage(loggingRecipient, str(e))
            errorCount += 1
        continue

    settings.UpdateLastTweetId(latestTweetId)

    #follow back new followers
    newFollowers = friendFollowers.FollowBackNewFollowers()
    message = "{0} retweets, {1} errors, {2} new followers, {3} total followers".format(retweetCount, errorCount, newFollowers, t.GetFollowers_Count())
    print(message)
    t.DirectMessage(loggingRecipient, message)


if __name__ == '__main__':
    main()
