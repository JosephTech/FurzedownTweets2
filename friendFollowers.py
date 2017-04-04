import twitter
import readConfig
import os

def FollowBackNewFollowers(t, settings):
    settings = readConfig.ConfigSettings('config.json')

    # t = twitter.Wrapper(access_token=settings.AccessToken,
    #                         access_token_secret=settings.AccessTokenSecret,
    #                         consumer_key=settings.ConsumerKey,
    #                         consumer_secret=settings.ConsumerSecret)

    try:
        #newFollowers = t.GetNewFollowers()
        newFollowersFollowed = t.BefriendNewFollowers(t.GetNewFollowers(), settings.NewFollowerMessage, settings.LoggingRecipient)
        return newFollowersFollowed
    except Exception as e:
        t.DirectMessage(settings.LoggingRecipient, str(e))
        return 0

if __name__ == '__main__':
    FollowBackNewFollowers()