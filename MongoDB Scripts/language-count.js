db.tweets.aggregate([
{ $group: {
_id: '$lang',
count: {$sum: 1}
}},

{ $match: {
count: { $gt: 1 }
}},

{ $sort: {
count: -1
}},

{ $project: {
language: '$_id',
count: 1,
_id: 0
}}
]);