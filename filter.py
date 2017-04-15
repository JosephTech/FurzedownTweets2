
def FilterReplies(tweets):
    return list(filter(lambda status: status.text[0] != "@", tweets))

def FilterBannedWords(tweets, bannedWords):
    return list(filter(lambda status: not any(word in status.text.split() for word in bannedWords), tweets))

def FilterBannedUsers(tweets, bannedUsers):
    return list(filter(lambda status: status.author.screen_name not in bannedUsers, tweets))

def FilterMultipleHashTags(tweets, maxHashTags):
    return list(filter(lambda status: status.text.count('#') <= maxHashTags, tweets))

def FilterRetweets(tweets):
    return list(filter(lambda status: status.text.count('RT') == 0, tweets))
