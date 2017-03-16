import readConfig
import readList


settings = readConfig.ConfigSettings('./config/config.json')
print(settings.SearchQuery)
print(settings.ConsumerKey)

bannedUsers = readList.getList('./config/users.txt')
print(bannedUsers)

bannedWords = readList.getList('./config/words.txt')
print(bannedWords)