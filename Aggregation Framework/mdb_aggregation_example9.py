
'''This is an example of MongoDb aggregation framework and multiple $group stages'''
'''This code uses Tweets data and answers question: Who has mentioned the most unique users?'''

from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017')
db = client.examples

def unique_user_mentions():
    # in first grouping, we're accumulating a unique set of users mentioned in tweets produced by each user
    result = db.tweets.aggregate([
        {'$unwind': '$entities.user_mentions'},
        {'$group': {'_id': '$user.screen_name', 'mset': {'$addToSet': '$entities.user_mentions.screen_name'}}},
        {'$unwind': '$mset'},
        {'$group': {'_id': '$_id','count':{'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ])
    return result


if __name == '__main__':
    result = unique_user_mentions()
    pprint.pprint(result)
