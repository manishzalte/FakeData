from faker import Faker
import json
import concurrent.futures 
import time


fake = Faker()


def genrate_data(records):
    customer = {}
    for n in range(0, records):
        customer[n] ={}
        customer [n]['Name'] = fake.name()
        customer[n]['Address']= fake.address()
        customer[n]['Country'] = fake.country()
        customer [n]['city']= fake.city()
        customer [n]['IP']= fake.ipv4_private()

    with open('customer.json','w') as fp:
            json.dump(customer, fp)
    print("File has been created")

#import time
nums = [100000]
while True:
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(genrate_data,nums)
    time.sleep(60)