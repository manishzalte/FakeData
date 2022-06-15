
import time
from faker import Faker
from pymongo import MongoClient, InsertOne,collection
import pymongo 
import json

from requests import request

fake = Faker()
customer = []
records = 10000
def genrate_data(records):
   
    for n in range(0, records):
        item ={'_id': n, 'name':fake.name(),'address':fake.address() , 'Country': fake.country(), 'city':fake.city(),'IP':fake.ipv4_private()}
        
        customer.append(item)
    return customer
    
def write_data(document):
    # write data to intake collection
    try:
        uri = "mongodb://localhost:27017"

        client = MongoClient(uri)
        db = client.Raw_Data
        collection = db.fake_user
        db.collection.bulk_write(document)
    except TypeError:
        pass 
    print("File Stored in the database....")
while True:
    
    Data_save = genrate_data(records)
    write_data(Data_save)
    time.sleep(60)   