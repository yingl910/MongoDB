
'''This is an example of MongoDB aggregation framework'''
'''This code uses Tweets data and answers question:
Of the users in the "Brasilia" timezone who have tweeted 100 times or more, who has the largest number of followers?'''



def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():

    pipeline = [{'$match': {'user.time_zone': "Brasilia", "user.statuses_count": {'$gte': 100}}},
                {'$project': {'tweets': '$user.statuses_count', 'followers': '$user.followers_count',
                              'screen_name':'$user.screen_name'}},
                {'$sort': {'followers': -1}},
                {'$limit': 1}]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.tweets.aggregate(pipeline)]


if __name__ == '__main__':
    db = get_db('twitter')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    pprint.pprint(result)
    assert len(result) == 1
    assert result[0]["followers"] == 17209

