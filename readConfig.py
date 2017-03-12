import json
configFile = 'config.json'

def getConfigSection(section):
    with open(configFile) as jsonDataFile:
        return json.load(jsonDataFile)[section]



print(getConfigSection('twitter'))