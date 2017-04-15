import io
import json
import time
import os
import sys


def saveTweetJsonToFile(tweet):
    try:
        fileName = os.path.join(sys.path[0],'export','tweet_data_{0}.json'.format(getDailyFileName()))
        print(fileName)

        json_str = json.dumps(tweet._json)
        json_str = json_str.replace('\"id_str\"','\"_id\"', 1)

        with open(fileName, 'a') as jsonFile:
            jsonFile.write(str(json_str))
            jsonFile.write("\n")
            jsonFile.close()
    except Exception as e:
        print(str(e))
        pass

def getDailyFileName():
    ## dd/mm/yyyy format
    return time.strftime("%Y%m%d")
