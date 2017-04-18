db.tweets.aggregate(
  [
    {$match: {"lang": {$in: ["en"]}}},
    {$project: {"entities.hashtags": 1, _id: 0}},
    {$unwind: "$entities.hashtags"},
    {$group: {_id: "$entities.hashtags.text", count: {$sum: 1}}},
    {$sort: {count: -1}},
    {$project: {"hashtag": "$_id", "count": 1, "_id": 0}},
    {$out: "hashtag_dist_en"}
  ]
)


DBQuery.shellBatchSize = 300
db.hashtag_dist_en.count()
db.hashtag_dist_en.find()
