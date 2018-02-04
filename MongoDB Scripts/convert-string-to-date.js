use furzedowntweets;
var cursor = db.tweets.find({created_at: { $type: 2}});	
while (cursor.hasNext()) {
	var doc = cursor.next();
	db.tweets.update({_id : doc._id}, {$set : {created_at : new Date(doc.created_at)}});
}
db.tweets.aggregate(
	{$group : {_id: 
				{year:{$year : "$created_at"},
				month:{$month : "$created_at"},
				day:{$dayOfMonth : "$created_at"}
				}, 
			count:{$sum:1}}},
	{$sort:{"_id.year":-1, "_id.month":-1, "_id.day":-1}}
);
db.tweets.find({},{created_at: 1, text: 1}).sort({created_at: -1}).limit(1);
