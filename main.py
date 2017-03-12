import readConfig as config

settings = config.getConfigSection('twitter')
print(settings['consumerKey'])
