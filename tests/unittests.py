import unittest
import readConfig
import readList
import twitter
from tests import mocks


class ReadConfigTests(unittest.TestCase):

    def test_GetSearchQuery(self):
        settings = readConfig.ConfigSettings('../config/config.json')
        self.assertEqual(settings.SearchQuery,'#furzedown OR #tooting')

    def test_UpdateLastTweetId(self):
        settings = readConfig.ConfigSettings('../config/config.json')
        lastTweetId = settings.LastTweetId
        updatedId = lastTweetId + 1
        settings.UpdateLastTweetId(updatedId)
        updatedId = settings.LastTweetId
        self.assertTrue(updatedId == lastTweetId + 1)


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
        cls._twitter = twitter.Wrapper(access_token=settings.AccessToken,
                                       access_token_secret=settings.AccessTokenSecret,
                                       consumer_key=settings.ConsumerKey,
                                       consumer_secret=settings.ConsumerSecret)


    def test_TwitterConnectivity(self):
        user = self._twitter.api.me()
        print(user.screen_name)
        print(user.followers_count)
        self.assertTrue(user.followers_count > 0)

    #def test_TwitterSearch(self):
    #    tweets = self._twitter.LatestTweets('#furzedown OR #tooting', 843125330013569025)
    #    for tweet in tweets:
    #        print(tweet.text)
    #    self.assertTrue(len(tweets) > 0)

    def test_InitialiseLatestTweetId(self):
        id = self._twitter.InitialiseLatestTweetId(1, '#furzedown OR #tooting')
        print(id)

    def test_FilterReplies(self):
        tweets = list()
        tweets.append(mocks.status('@this is a reply', 'jules'))
        tweets.append(mocks.status('this is not a reply', 'jules'))

        latestTweets = self._twitter.FilterReplies(tweets)

        self.assertTrue(len(latestTweets) == 1)
        self.assertTrue(latestTweets[0].text == 'this is not a reply')

    def test_FilterBannedUsers(self):
        tweets = list()
        tweets.append(mocks.status('this is a reply', 'jules'))
        tweets.append(mocks.status('this is not a reply', 'lucifer'))

        bannedUsers = list()
        bannedUsers.append('lucifer')

        latestTweets = self._twitter.FilterBannedUsers(tweets, bannedUsers)

        self.assertTrue(len(latestTweets) == 1)
        self.assertTrue(latestTweets[0].author.screen_name == 'jules')
        for tweet in latestTweets:
            print(tweet.author.screen_name)

    def test_FilterBannedWords(self):
        tweets = list()
        tweets.append(mocks.status('what a load of bollocks', 'jules'))
        tweets.append(mocks.status('this is not a reply', 'lucifer'))

        bannedWords = list()
        bannedWords.append('bollocks')

        latestTweets = self._twitter.FilterBannedWords(tweets, bannedWords)

        self.assertTrue(len(latestTweets) == 1)
        self.assertTrue(latestTweets[0].text == 'this is not a reply')
        for tweet in latestTweets:
            print(tweet.text)

    def test_FilterMultipleHashTags(self):
        tweets = list()
        tweets.append(mocks.status('#tooting #furzedown #paris #boston', 'jules'))
        tweets.append(mocks.status('#tooting #hello', 'lucifer'))

        latestTweets = self._twitter.FilterMultipleHashTags(tweets, 3)

        self.assertTrue(len(latestTweets) == 1)
        self.assertTrue(latestTweets[0].text == '#tooting #hello')
        for tweet in latestTweets:
            print(tweet.text)







