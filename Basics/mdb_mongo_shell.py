'''These are example codes in Mongo shell'''

'''$exists'''
use examples #switch to example database
db.cities.find()

#contain the field
db.cities.find({"governmentType":{'$exists':1}})
#do not contain the field
db.cities.find({"governmentType":{'$exists':0}})
#more human readable
db.cities.find({"governmentType":{'$exists':1}}).pretty()
#could use this to compare how many contain a particular field and how many don't
db.cities.find({"governmentType":{'$exists':1}}).count()


'''$regex'''
db.cities.find({'motto':{'$regex':'[Ff]riendship'}})
db.cities.find({'motto':{'$regex':'[Ff]riendship|[Pp]ride'}})


'''query within array'''
# an example of using a scalar value in query document for an array value field
#mongodb search inside array value fields for individual values that match
db.autos.find({'modelYears':1980}).pretty()


#second way for querying array
"""$in"""
db.autos.find({'modelYears':{'$in':[1965,1966,1967]}})
#retreieve all documents for which the model years field contains any of the values in this array here
#each document in result contains at least one value in the $in array

'''.(dot notation)'''
#dig into 'dimensions' field uisng dot notation and accessing the weight field of this dimension sub-document
db.autos.find({'dimensions.weight':{'$gt':5000}}) #retreieve all autos with the weight greater than 5000


#find all tweets where the hashtags value for the entities sub-document is not equal to an empty array
#projection part: just want to see all hashtags text; for hashtags have multiple text values, all will print
#use dot notation not only find but also projection
db.tweets.find({'entities.hashtags':{'$ne':[]}},{'entities.hashtags.text':1,'_id':0})

#remove all documents in cities collection, one by one
db.cities.remove()

# same thing, more efficient, remove the entire collection and any metadata, like index
db.cities.drop()

db.cities.remove({'name':'Chicago'})

# an additional example of find
# cities that do not have name
db.cities.find({'name':{'$exist':0}})

# $size: length 3
db.tweets.find({'entities.user_mentions':{'$size':3}}).pretty()