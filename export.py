import io
import json
import time
import os
import sys


def saveTweetJsonToFile(tweet):
    fileName = os.path.join(sys.path[0],'export','tweet_data_{0}.json'.format(getDailyFileName()))
    print(fileName)

    savefile = io.open(fileName, 'a', encoding='utf-8')

    json_str = json.dumps(tweet._json)
    json_str = json_str.replace('\"id_str\"','\"_id\"', 1)
    #print(json_str)

    savefile.write(str(json_str))
    savefile.write("\n")
    savefile.close()

def getDailyFileName():
    ## dd/mm/yyyy format
    return time.strftime("%Y%m%d")
