import json
import os
import sys

class ConfigSettings:

    def __init__(self, configfile):
        configFilePath = os.path.join(sys.path[0], 'config', configfile)
        self.configFile = configFilePath

    def getConfigSection(self, section):
        with open(self.configFile, 'r') as jsonDataFile:
            return json.load(jsonDataFile)[section]

    #abstract plain string config identifiers away from main.py
    @property
    def SearchQuery(self):
        return self.getConfigSection('search')['query']

    @property
    def MaxHashTags(self):
        return self.getConfigSection('search')['maxHashTags']

    @property
    def LoggingRecipient(self):
        return self.getConfigSection('logging')['recipient']

    @property
    def NewFollowerMessage(self):
        return self.getConfigSection('logging')['newFollowerMessage']

    @property
    def SaveJsonToFile(self):
        return self.getConfigSection('logging')['saveJsonToFile']

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

    @property
    def LastTweetId(self):
        return self.getConfigSection('twitter')['lastTweetId']

    @property
    def ConfigPath(self):
        return os.path.join(os.getcwd(),'config')

    @property
    def ConnectionString(self):
        return "mongodb://julesjoseph:ftsP93gnEqiEXZPe@cluster0-shard-00-00-rsihj.mongodb.net:27017,cluster0-shard-00-01-rsihj.mongodb.net:27017,cluster0-shard-00-02-rsihj.mongodb.net:27017/furzedowntweets?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"

    def getConfigFilePath(self, fileName):
        return os.path.join(self.ConfigPath, fileName)



    def UpdateLastTweetId(self, lastTweetId):
        with open(self.configFile, "r+") as jsonDataFile:
            config = json.load(jsonDataFile)
            config['twitter']['lastTweetId'] = lastTweetId
            jsonDataFile.write(json.dumps(config))
        with open(self.configFile, "w") as jsonFile:
            json.dump(config, jsonFile)

