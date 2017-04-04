TwitterBot written in Python, using Tweepy API

Main Functionality:

Retweet:
- Searches for and retweets statuses that match specified search criteria
- Retweets can be restricted by:
  - key words
  - user name
  - number of hash tags

Follow:
- Checks for new followers and follows them back
- Sends a welcome Direct Message to new followers

Logging
- Status updates and errors are sent to specified Twitter user via DM

Getting Started
This code was originally written for running on a Raspberry Pi, but could be run on any platform that runs Python

Example implementation: @furzedowntweets https://twitter.com/furzedowntweets

Twitter App:
Set up via https://apps.twitter.com/ - you will need consumer key, consumer secret, access token and access token secret to allow you to send tweets via the Twitter API

Tweepy
This is not part of the standard Python distribution - installation details here https://github.com/tweepy/tweepy

Upload the following files to your platform:
- filter.py
- friendFollowers.py
- main.py
- readConfig.py
- readList.py
- twitter.py
- /config/config.json
- /config/users.txt
- /config/words.txt

main.py is the entry point (ie sudo python main.py)
You must have a config subfolder within your main folder.

You must set the following in /config/config.json
- logging/recipient
- logging/newFollowerMessage
- search/query
- search/maxHashTags
- twitter/consumerKey
- twitter/consumerSecret
- twitter/accessToken
- twitter/accessTokenSecret
- twitter/lastTweetId

Create a crontab to run main.py at regular intervals.
