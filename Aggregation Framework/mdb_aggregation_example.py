
'''This is an example of MongoDB aggregation framework'''
'''This code uses Tweets data and answers question: calculate the number of tweets for each user'''

from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017')
db = client.twitter

def most_tweets():
    #'aggregate' command issues aggregation query
    # aggregation is done with a pipeline (a series of stages that included as elements of an array
    # that's passed through aggregate as a parameter)

    # $group : group operator; in this example, we group by user's screen_name field
    # $user.screen_name: the '$' sign here is not an operator;
    # also, even though it's in quotes, don't interpret it as string
    # Rather, group together all documents where the value of screen name for the user sub document
    # this is what dollar says here where the value of user.screen_name is the same
    # so all tweets that have same value for user.screen_name field will be group together
    # $sum: accumulate operator; for every document that has the same value for user.screen_name field,
    # increment 'count' by 1

    # $sort: sort based on 'count' field, in descending order
    # pipeline: the input documents of $sort stage is the output document of $group stage

    result = db.tweets.aggregate([
        {'$group': {'_id': '$user.screen_name', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}}
    ])

    return result

if __name__ == '__main__':
    result = most_tweets()
    pprint.pprint(result)

# the result of aggregation query is always a single document
# it's the 'result' field (an array valued field)of that return document that we're interested in (tweet_result.png)
