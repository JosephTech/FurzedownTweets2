import json
configFile = 'config.json'

def getConfigSection(section):
    with open('config.json') as json_data_file:
        data = json.load(json_data_file)
    return data[section]


print(getConfigSection('twitter'))