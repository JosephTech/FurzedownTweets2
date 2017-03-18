import json

class ConfigSettings:

    def __init__(self, configfile):
        self.configFile = configfile

    def getConfigSection(self, section):
        with open(self.configFile) as jsonDataFile:
            return json.load(jsonDataFile)[section]

    #abstract plain string config identifiers away from main.py
    @property
    def SearchQuery(self):
        return self.getConfigSection('search')['query']

    @property
    def ConsumerKey(self):
        return self.getConfigSection('twitter')['consumerKey']

    @property
    def ConsumerSecret(self):
        return self.getConfigSection('twitter')['consumerSecret']

    @property
    def AccessToken(self):
        return self.getConfigSection('twitter')['accessToken']

    @property
    def AccessTokenSecret(self):
        return self.getConfigSection('twitter')['accessTokenSecret']

