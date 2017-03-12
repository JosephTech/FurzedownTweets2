import json
configFile = 'config.json'

with open(configFile, "r") as jsonDataFile:
    data = json.load(jsonDataFile)
print(data)

#data2 = json.loads(data)

#for element in data2['twitter']:
 #   print(element)
