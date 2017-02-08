
'''This is an example of MongoDB aggregation framework and $unwind operator'''
'''This code uses Tweets data and answers question: Who included the most user mentions?'''

from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017')
db = client.examples

def user_mentions():
    # $unwind creates a copy of the containing document for any array field
    # it duplicates all fields except for the item in the array
    # and it will create one copy for each element in the array and
    # the only difference between all copies will be that this field ($entities.user_mentions in this example)
    # will take on each of the different values in the array in the documents that are produced
    # in this example, the user mentions field in the $unwind output documents of will have a single document as
    # its value in each copies while other fields will be same for that user
    result = db.tweets.aggregate([
        {'$unwind': '$entities.user_mentions'},
        {'$group': {'_id': '$user.screen_name', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 1}
    ])
    return result

if __name__ == '__main__':
    result = user_mentions()
    pprint.pprint(result)