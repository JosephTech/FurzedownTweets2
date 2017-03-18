import unittest
import readConfig
import readList
import twitter


class ReadConfigTests(unittest.TestCase):

    def test_GetSearchQuery(self):
        settings = readConfig.ConfigSettings('../config/config.json')
        self.assertEqual(settings.SearchQuery,'#furzedown OR #tooting')

class ReadListTests(unittest.TestCase):

   def test_GetUserList(self):
        users = readList.getList('../config/users.txt')
        self.assertTrue(len(users) > 0)

   def test_GetWordList(self):
        words = readList.getList('../config/words.txt')
        self.assertTrue(len(words) > 0)

class TwitterInterfaceTests(unittest.TestCase):

    @classmethod
    def setUp(cls):
        settings = readConfig.ConfigSettings('../config/config.json')
        cls._twitter = twitter.Twitter(access_token=settings.AccessToken,
                             access_token_secret=settings.AccessTokenSecret,
                             consumer_key=settings.ConsumerKey,
                             consumer_secret=settings.ConsumerSecret)


    def test_TwitterConnectivity(self):
        user = self._twitter.api.me()
        print(user.screen_name)
        print(user.followers_count)
        self.assertTrue(user.followers_count > 0)

    def test_TwitterSearch(self):
        tweets = self._twitter.LatestTweets('#tooting', 843125330013569025)
        for tweet in tweets:
            print(tweet.text)


