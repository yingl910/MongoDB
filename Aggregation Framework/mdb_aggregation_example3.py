
'''This is an example MongoDB aggregation framework and uses $match and $project operator'''
'''This code uses Tweets data and answers question: Who has the highest followers to following ratio'''

from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017')
db = client.examples

def highest_ratio():
    # $match is a filtering operator
    # for the value of $match, you use same syntax as find operation

    '''usage of $project'''
    # a. include fields from the original documents
    # project works with a single document at a time and we're essentially doing a shaping task
    # selecting the fields we want to pass to next stage
    # b. insert computed fields, like ratio
    # c. rename fields
    # d. create fields that hold subdocuments (substantial reshaping)


    # '$user.followers_count': $ indicates that we want the value of that field
    # instead of treating the '$user.followers_count' as a literal string
    # the result of $divide operator is the value of field 'ratio'
    # $limit line: limit to just very first document we see

    result = db.tweets.aggregate([
        {'$match': {
            'user.friends_count':{'$gt': 0}, 'user.followers_count': {'$gt': 0}}},
        {'$project': {'ratio': {'$divide': ['$user.followers_count', '$user.friends_count']},
                      'screen_name':'$user.screen_name'}},
        {'$sort': {'ratio': -1}},
        {'$limit': 1}
    ])
    return result

if __name__ == '__main__':
    result = highest_ratio()
