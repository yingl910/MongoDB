from pymongo import MongoClient

client = MongoClient(‘mongoldb://localhost:27017/')
#create a client object and specify a connection string (connect to any mongod that we have access to)

tesla_s = {}
#dictionary here

#speicify we want to use example database
db = client.examples
#insert tesla_s document into autos collection in examples database
db.autos.insert(tesla_s)

#find, running in this way, will simply give us a cursor for all of the documents,
# in this case, autos collection (we specify)
for a in db.autos.find():
    pprint.pprint(a)


#another example of insert
client = MongoClinet('')
db = client.examples
num_autos = db.myautos.find().count()
print("num_autos before:", num_autos)

for a in autos:
    db.myautos.insert(a)
# passing in a python dictionary, pymongo will translate it into BSON encoding and send it to database

num_autos = db.myautos.find().count()
print("num_autos after:", num_autos)
