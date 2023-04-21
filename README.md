# Basic Twitter Bot
A basic Python Twitter bot that will post a random post from a MongoDB database.

### insert_lyrics.py <br />
'Usage: python3 insert_lyrics.py <csv_file>' <br />
Parses a csv file with song lyrics and automatically adds it to the database while checking for duplicates.

### twitter_bot.py <br />
'Usage: python3 twitter_bot.py' <br />
Every day at noon, pulls a random post from the database and posts it. Also marks the post as tweeted in the database.

### .env <br />
MONGO_USERNAME='' <br />
MONGO_PASSWORD='' <br />
MONGO_CLUSTER='' <br />
MONGO_AUTH_SOURCE='' <br />
MONGO_AUTH_MECHANISM='' <br />
MONGO_DB_NAME='' <br />
MONGO_COLL_NAME='' <br />
TWITTER_CONSUMER_KEY='' <br />
TWITTER_CONSUMER_SECRET='' <br />
TWITTER_BEARER_TOKEN='' <br />
TWITTER_ACCESS_TOKEN='' <br />
TWITTER_ACCESS_TOKEN_SECRET='' <br />
TWITTER_CLIENT_ID='' <br />
TWITTER_CLIENT_SECRET='' <br />
