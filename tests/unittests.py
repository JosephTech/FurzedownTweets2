import unittest
import readConfig
import readList

class ReadConfigTests(unittest.TestCase):

    def test_GetSearchQuery(self):
        settings = readConfig.ConfigSettings('../config.json')
        self.assertEqual(settings.SearchQuery,'#furzedown OR #tooting')

class ReadListTests(unittest.TestCase):

   def test_GetUserList(self):
        users = readList.getList('../users.txt')
        self.assertTrue(len(users) > 0)

   def test_GetWordList(self):
        words = readList.getList('../words.txt')
        self.assertTrue(len(words) > 0)