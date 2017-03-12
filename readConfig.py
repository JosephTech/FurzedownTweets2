import json
configFile = 'config.json'

def getConfigSection(section):
    with open(configFile) as jsonDataFile:
        return json.load(jsonDataFile)[section]

#abstract plain string config identifiers away from main.py
def SearchQuery():
    return getConfigSection('search')['query']


print(SearchQuery())