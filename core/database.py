from pymongo import MongoClient
import os

client = MongoClient(os.environ.get("MONGODB_URL"))
db = client[os.environ.get("MONGO_INITDB_DATABASE")]
