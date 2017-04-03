import twitter
import readConfig
import os

def FollowBackNewFollowers():
    settings = readConfig.ConfigSettings('config.json')

    t = twitter.Wrapper(access_token=settings.AccessToken,
                            access_token_secret=settings.AccessTokenSecret,
                            consumer_key=settings.ConsumerKey,
                            consumer_secret=settings.ConsumerSecret)

    try:
        newFollowers = t.GetNewFollowers()
        t.BefriendNewFollowers(newFollowers, settings.NewFollowerMessage)
        return len(newFollowers)
    except Exception as e:
        t.DirectMessage(settings.LoggingRecipient, str(e))
        print(e)

if __name__ == '__main__':
    FollowBackNewFollowers()