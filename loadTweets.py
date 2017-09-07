from pymongo import MongoClient
import readConfig
import json
from datetime import datetime
import sys
from pprint import pprint

def main():
    #set up connection
    settings = readConfig.ConfigSettings('config.json')
    client = MongoClient(settings.ConnectionString)
    db = client.furzedowntweets

    #clear down tweets for the day being loaded
    start = datetime(2017, 8, 30, 0, 0, 0)
    end = datetime(2017, 8, 31, 0, 0, 0)
    db.test.delete_many({"created_at": {"$gte": start, "$lt": end}})


    #get tweets out of json file
    data = []
    for line in open('./export/tweet_data_20170830.json','r'):
        data.append(json.loads(line))

    #load tweets into database
    counter = 1
    for rec in data:
        try:
            db.test.insert_one(rec)
            pprint('inserted %d' % (counter))
        except:
            print("Unexpected error: ", sys.exc_info()[0], str(counter))
        counter = counter + 1

    #update string dates to datetime
    for doc in db.test.find({"created_at": { "$type": 2}}):
        db.test.update_one({'_id': doc['_id']},{'$set' : {'created_at' : datetime.strptime(doc['created_at'],"%a %b %d %H:%M:%S +0000 %Y")} })


if __name__ == '__main__':
    main()
