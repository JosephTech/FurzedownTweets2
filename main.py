import readConfig

settings = readConfig.getConfigSection('twitter')
print(settings['consumerKey'])
