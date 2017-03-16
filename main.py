import readConfig
import readList


settings = readConfig.ConfigSettings('config.json')
print(settings.SearchQuery)
print(settings.ConsumerKey)

bannedUsers = readList.getList('users.txt')
print(bannedUsers)

bannedWords = readList.getList('words.txt')
print(bannedWords)