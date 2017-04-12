import io
import json


def saveTweetJsonToFile(tweet):
    savefile = io.open('tweet_data.json', 'a', encoding='utf-8')

    json_str = json.dumps(tweet._json)

    savefile.write(str(json_str))
    savefile.write(",\n")
    savefile.close()