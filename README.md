# Basic Twitter Bot
A basic Python Twitter bot that will post a random post from a MongoDB database.

### Installing modules <br />
```console
$ pip install pymongo python-dotenv schedule tweepy certifi
```

### insert_lyrics.py <br />
```console
$ python3 insert_lyrics.py <csv_file>
```
Parses a csv file with song lyrics and automatically adds it to the database while checking for duplicates.

### twitter_bot.py <br />
```console
$ python3 twitter_bot.py
```
Every day at noon, pulls a random post from the database and posts it. Also marks the post as tweeted in the database.

### .env
```
MONGO_USERNAME=''
MONGO_PASSWORD=''
MONGO_CLUSTER=''
MONGO_AUTH_SOURCE=''
MONGO_AUTH_MECHANISM=''
MONGO_DB_NAME=''
MONGO_COLL_NAME=''
TWITTER_CONSUMER_KEY=''
TWITTER_CONSUMER_SECRET=''
TWITTER_BEARER_TOKEN=''
TWITTER_ACCESS_TOKEN=''
TWITTER_ACCESS_TOKEN_SECRET=''
TWITTER_CLIENT_ID=''
TWITTER_CLIENT_SECRET=''
```
