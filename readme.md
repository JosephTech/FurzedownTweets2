Rewrite/Refactor of Furzedown Tweets TwitterBot code

Objectives:
- learn Python coding better
- better/clean code structure
- break down monolithic codeblock and abstract config/twitter api calls etc away to other files/classes

20170312
Started with config settings - looking at alternatives to config.ini which seems quite old school. Reading about JSON and YAML - opted for JSON as it's something widely used across all platforms.

20170313
Wrapped config settings in a class and exposed settings as properties - pass json file name to constructor
Created a basic unit test

20170318
Started wrapper class for Tweepy API
Unit Tests - how to declare setup method
Config - how to update a setting in the config file

TODO
- wrapper round tweepy api
- can we set path variable so we dont need to explicitly state path to config files etc?
- How do we mock tweets for testing twitter API without calling twitter