import unittest
import readConfig
import readList

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