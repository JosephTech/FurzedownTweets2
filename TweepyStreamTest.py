import tweepy
import readConfig


# override tweepy.StreamListener to add logic to on_status


def main():
    settings = readConfig.ConfigSettings('config.json')
    auth = tweepy.OAuthHandler(settings.ConsumerKey, settings.ConsumerSecret)
    auth.set_access_token(settings.AccessToken, settings.AccessTokenSecret)
    api = tweepy.API(auth, wait_on_rate_limit_notify=True)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(api.auth, listener=myStreamListener)
    myStream.filter(track=['#tooting', '#furzedown'])


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_friends(self, friends):
        # is this raised for new followers?
        for friend in friends:
            print(friend)

    # 420 = rate limit exceeded - disconnect - how do we reconnect?
    def on_error(self, status_code):
        if status_code == 420:
            return False


if __name__ == '__main__':
    main()