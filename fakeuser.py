import pymongo
import json
from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient('localhost',27017)
db = client.raw_data
collection = db.fake_user
requesting = []

with open(r"customer.json") as f:
    for jsonObj in f:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))

result = collection.bulk_write(requesting)
client.close()