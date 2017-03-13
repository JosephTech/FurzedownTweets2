import readConfig


settings = readConfig.ConfigSettings('config.json')
print(settings.SearchQuery)
print(settings.ConsumerKey)
