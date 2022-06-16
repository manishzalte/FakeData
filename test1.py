
import time
from faker import Faker
from pymongo import MongoClient ,WriteConcern
import pymongo 


fake = Faker()

customer = []
records = 1000000
#Genrating fake Data 
def genrate_data(records):
   
    for n in range(0, records):
        #iter on the range for indivial element
        item ={'name':fake.name(),'address':fake.address() , 'Country': fake.country(), 'city':fake.city(),'IP':fake.ipv4_private()}
        #dict of name ,add, country, city, IP
        customer.append(item)
    return customer
    
def write_data(document):
    
    # write data to intake collection
    uri = "mongodb://localhost:27017"

    client = MongoClient(uri)
    db = client.Raw_Data
    collection = db.fake_user
        #db.collection.bulk_write(document)


    db.collection.with_options(write_concern=WriteConcern(w=0)).insert_many(document, ordered=False)
    print("File Stored in the database....")
      
while True:
    
    Data_save = genrate_data(records)
    write_data(Data_save)
    time.sleep(25)   