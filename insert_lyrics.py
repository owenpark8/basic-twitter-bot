import os
import sys
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
import csv
from dotenv import load_dotenv
import certifi

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

# Read posts from CSV file
if len(sys.argv) < 2:
    print('Usage: python3 inser_lyrics.py <csv_file>')
    sys.exit(1)


csv_filename = sys.argv[1]

with open(csv_filename, 'r') as csv_file:
    reader = csv.reader(csv_file)
    posts = [row[0] for row in reader]

# Insert posts into MongoDB
for post in posts:
    if collection.count_documents({'post': post}) > 0:
        print(f'Skipped duplicate post: {post}')
    else:
        collection.insert_one({'post': post})
        print(f'Inserted post: {post}')
