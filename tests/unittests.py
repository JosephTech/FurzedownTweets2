import unittest
import readConfig
import sys, os

class ReadConfigTests(unittest.TestCase):

    def test_GetSearchQuery(self):
        settings = readConfig.ConfigSettings('../config.json')
        self.assertEqual(settings.SearchQuery,'#furzedown OR #tooting')

