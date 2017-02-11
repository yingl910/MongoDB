
'''These are examples of MongoDB example codes of save and update, two methods for updating'''

'''update method one: save'''
# a method on collection objects
# find_one just returns the first document it finds
city = db.cities.find_one({'name':"munchen",'country':'Germany'})
city['isoCountryCode'] = 'DEU'
db.cities.save(city)
# a method on collection objcects
#if the object we pass already have a _id and a document with that id already in the collection ->replacement
#if there is no document with _id or the object we're passing does not have _id -> create

'''update method two: update'''
#update : a method on collection objects; a query document as 1st parameter
#2nd parameter: an update document: specify what operations mongodb should perform on the document matching this query
#by default, update operates on just one document(first found)
#if the field is not exsit -> create; exist -> update
city = db.cities.update({'name':"munchen",'country':'Germany'},
                        {'$set':{
                            'isoCountryCode':'DEU'
                        }})

'''inverse of $set: $unset'''
# if the field is not exsit -> no effect; exist -> remove
city = db.cities.update({'name':"munchen",'country':'Germany'},
                        {'$unset':{
                            'isoCountryCode':''

                        }})

'''PAY ATTENTION: IT'S REALLY EASY TO FORGET $SET AND $UNSET OPERATOR'''
# what happens here is the document matching this query will be replaced so that it contains the _id and
#'iscountrycode' field ONLY

city = db.cities.update({'name':"munchen",'country':'Germany'},
                        {'isoCountryCode':'DEU'})


'''update multiple documents at once'''
db.cities.update({'country': 'Germany'},
                 {'$set': {
                     'isoCountryCode': "DEU"
                 }
                 },
                 multi = True)