from pymongo import MongoClient
from .config import MONGO_URI, MONGO_DB_NAME
from .responses import TrendItem

def get_mongo_client():
    return MongoClient(MONGO_URI)

def get_trends():
    client = get_mongo_client()
    db = client[MONGO_DB_NAME]
    collection = db.trends
    trends = collection.find()
    return [TrendItem(name=trend['name'], url=trend['url'], tweet_volume=trend['tweet_volume']) for trend in trends]

def save_trends():
    client = get_mongo_client()
    db = client[MONGO_DB_NAME]
    collection = db.trends
   
    trends = [
        {"name": "#Python", "url": "https://twitter.com/hashtag/Python", "tweet_volume": 100000},
        {"name": "#FastAPI", "url": "https://twitter.com/hashtag/FastAPI", "tweet_volume": 50000},
    ]
    collection.insert_many(trends)
