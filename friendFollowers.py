import twitter
import readConfig

def FollowBackNewFollowers():
    settings = readConfig.ConfigSettings('./config/config.json')

    t = twitter.Wrapper(access_token=settings.AccessToken,
                            access_token_secret=settings.AccessTokenSecret,
                            consumer_key=settings.ConsumerKey,
                            consumer_secret=settings.ConsumerSecret)

    try:
        newFollowers = t.GetNewFollowers()
        t.BefriendNewFollowers(newFollowers)
        return len(newFollowers)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    FollowBackNewFollowers()