
'''This is an example of MongoDB aggregation framework and $group $avg operator'''
'''This code uses Tweets data and answers question:
a. calculate the average# of retweets for any tweets using a particular hashtag
b. find all unique hashtags for each user
'''

# $group operator: aggregate input in someway based on the operators
# $sum, $first (select 1st documented group), $last, $max, $min, $avg
# $push, $addToSet: operators deal with arrays
# $addToSet: add unique value to the array(treats it as set)

from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017')
db = client.examples


def hashtag_retweet_avg():
    result = db.tweets.aggregate([
        {'$unwind': '$entities.hashtags'},
        {'$group': {
            '_id': '$entities.hashtags.text', 'retweet_avg': {'$avg': '$retweet_count'}
        }},
        {'$sort': {'retweet_avg': -1}}
    ])
    return result


def unique_hashtag_by_user():
    result = db.tweets.aggregate([
        {'$unwind': '$entities.hashtags'},
        {'$group': {
            '_id': '$entities.screen_name', 'unique_hashtags': {'$addToSet': '$entities.hashtags.text'}
        }},
        {'$sort': {'_id': -1}}
    ])
    return result

if __name__ == '__main__':
    result = hashtag_retweet_avg()
    result2 = unique_hashtag_by_user()
    pprint.pprint(result)
    pprint.pprint(result2)