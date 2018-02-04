#test
from pymongo import MongoClient
client = MongoClient('mongodb://julesjoseph:ftsP93gnEqiEXZPe@cluster0-shard-00-00-rsihj.mongodb.net:27017,cluster0-shard-00-01-rsihj.mongodb.net:27017,cluster0-shard-00-02-rsihj.mongodb.net:27017/furzedowntweets?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')
db = client['furzedowntweets']
collection = db['tweets']

pipe = [{'$group': {'_id': '$mvid', 'count': {'$sum': 1}}}]

# Notice the below line
TestOutput = collection.aggregate(pipeline=pipe)
print(list(TestOutput))
client.close()


'''
db.foos.aggregate(
    [   
        {   $project : { day : {$substr: ["$TimeStamp", 0, 10] }}},        
        {   $group   : { _id : "$day",  number : { $sum : 1 }}},
        {   $sort    : { _id : 1 }}        
    ]
)
'''