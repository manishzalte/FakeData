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
    n=100
    for i in range (1, n+1):
        customer["name"]=f"#{i}" 
        with open(f'{i}.json','w') as fp:
            json.dump(customer, fp)
        print("File has been created")



#import time
nums = [1000]
while True:
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(genrate_data,nums)
        
    time.sleep(60)