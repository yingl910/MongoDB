
'''This is an example of MongoDB aggregation framework'''
'''This code uses cities infobox dataset and answers question: count the number of tweets for each user'''
'''use $push to accumulate all the tweet texts for each user; limit output to the 5 users with the most tweets'''


# $push is similar to $addToSet. The difference is that rather than accumulating only unique values
# it aggregates all values into an array.

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db


def make_pipeline():
    pipeline = [{'$group': {'_id': '$user.screen_name', 'tweet_texts': {'$push': '$text'}, 'count': {'$sum': 1}}},
                {'$sort': {'count': -1}},
                {'$limit': 5}]
    return pipeline


def aggregate(db, pipeline):
    return [doc for doc in db.twitter.aggregate(pipeline)]


if __name__ == '__main__':
    db = get_db('twitter')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint

    pprint.pprint(result)
    assert len(result) == 5
    assert result[0]["count"] > result[4]["count"]
    sample_tweet_text = u'Take my money! #liesguystell http://movie.sras2.ayorganes.com'
    assert result[4]["tweet_texts"][0] == sample_tweet_text
