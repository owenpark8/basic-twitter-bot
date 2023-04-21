import os
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
import tweepy
from dotenv import load_dotenv
import certifi
import schedule
import time

ca = certifi.where()

# Load environment variables from .env file
load_dotenv()

# MongoDB configuration
username = quote_plus(os.environ.get('MONGO_USERNAME').encode('utf-8'))
password = quote_plus(os.environ.get('MONGO_PASSWORD').encode('utf-8'))
cluster = os.environ.get('MONGO_CLUSTER')
auth_source = os.environ.get('MONGO_AUTH_SOURCE')
auth_mechanism = os.environ.get('MONGO_AUTH_MECHANISM')
db_name = os.environ.get('MONGO_DB_NAME')
coll_name = os.environ.get('MONGO_COLL_NAME')

uri = "mongodb+srv://" + username + ":" + password + "@" + cluster + ".e3v7hi4.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=ca)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client[db_name]
collection = db[coll_name]

# Twitter configuration
consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('TWITTER_BEARER_TOKEN')
# Authenticate with Twitter API
client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def post_tweet():
    # Retrieve a random post from MongoDB
    post = collection.aggregate([{ '$sample': { 'size': 1 } }]).next()['post']

    # Check if the post has already been tweeted
    if collection.count_documents({'post': post, 'tweeted': True}) > 0:
        print('Post already tweeted')
    else:
        # Tweet the post
        client.create_tweet(text=post)
        print('Tweeted:', post)

        # Mark the post as tweeted in MongoDB
        collection.update_one({'post': post}, {'$set': {'tweeted': True}})
        print('Marked as tweeted:', post)

# Schedule the post to run every day at noon
schedule.every().day.at("11:59").do(post_tweet)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)