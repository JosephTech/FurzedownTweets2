use furzedowntweets;
db.tweets.find( { created_at: { $gte: new Date('2017-05-20') } } ).count()

db.tweets.aggregate({$sort:{"_id":-1}}, {$match: {"entities.hashtags.text":{$exists:true}}}, {$limit:10000},{$unwind:"$entities.hashtags"}, {$project : {"entities.hashtags.text":1,"_id":0}}, {$group:{"_id":{$toLower:"$entities.hashtags.text"}, count : { $sum : 1 }}}, {$sort:{"count":-1}}, {$limit:100})