import io
import json
import time
import os
import sys
from pprint import pprint


def saveTweetJsonToFile(tweet):
    try:
        fileName = os.path.join(sys.path[0],'export','tweet_data_{0}.json'.format(getDailyFileName()))
        print(fileName)

        json_str = json.dumps(tweet._json)
        json_str = addDatabaseId(json_str)

        with open(fileName, 'a') as jsonFile:
            jsonFile.write(str(json_str))
            jsonFile.write("\n")
            jsonFile.close()
    except Exception as e:
        print(str(e))
        pass

def addDatabaseId(tweet_json):
    db_id = tweet_json['id_str']
    tweet_json['_id'] = db_id
    return tweet_json


def getDailyFileName():
    ## dd/mm/yyyy format
    return time.strftime("%Y%m%d")

def loadjson():
    jsonFile = os.path.join(sys.path[0],'export','tweet_data_{0}.json'.format(getDailyFileName()))

    with open(jsonFile) as data_file:
        data = json.load(data_file)

        data = addDatabaseId(data)
        pprint(data)



if __name__ == '__main__':
    loadjson()
